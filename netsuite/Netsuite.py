import json
import os
import pathlib

import jwt
from datetime import datetime, timedelta
from pathlib import Path
import requests
from netsuite_python.netsuite.NetsuiteToken import NetsuiteToken
from netsuite_python.netsuite.REST.REST_V1 import REST_V1
from netsuite_python.netsuite.settings import APISettings
from netsuite_python.netsuite.storages import BaseStorage, JSONStorage

NETSUITE_CERT_ID = "WCyIgdF_ThGFPTX_V18lep0VXSsqvvvhabv8MQzrGDw"
BASE_DIR = str(pathlib.Path(__file__).parent.resolve())
NETSUITE_KEY_FILENAME = "auth-key.pem"
NETSUITE_KEY_PATH = (os.path.join(BASE_DIR, "keys", f"{NETSUITE_KEY_FILENAME}"))


class Netsuite:
    # authorize_url = 'https://signin.infusionsoft.com/app/oauth/authorize'
    # access_token_url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token",
    app_name: str = None
    storage: BaseStorage = None
    api_settings: APISettings
    # xml_client = None
    rest_v1 = None

    def __init__(self, config: dict = None, config_file: Path = None):
        if config and config_file:
            raise ValueError("You can only load settings from one source")
        if config_file:
            with open(config_file, 'r') as f:
                config = json.load(f)
        self.api_settings = APISettings(config)
        if not self.api_settings.CLIENT_ID:
            raise Exception("Missing Client Id")
        if not self.api_settings.NETSUITE_APP_NAME:
            raise Exception("Missing Netsuite App Name")

        self.app_name = self.api_settings.APP_NAME

        self.storage = self.api_settings.STORAGE_CLASS()
        if isinstance(self.api_settings.STORAGE_CLASS(), JSONStorage):
            if not self.api_settings.JSON_STORAGE_PATH:
                raise Exception("JSON_STORAGE_PATH must be defined for JSONStorage")
            self.storage.storage_path = self.api_settings.JSON_STORAGE_PATH
        self.rest_url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest" \
                        f"/record/v1/ "
        self.access_token_url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token",

    @property
    def REST_V1(self):
        if not self.rest_v1:
            self.rest_v1 = REST_V1(self)
        return self.rest_v1

    @property
    def token(self) -> NetsuiteToken:
        return self.storage.get_token(self.app_name)

    def save_token(self, token):
        self.storage.save_token(self.app_name, token)

    def get_jwt(self):
        private_key = ""
        with open(NETSUITE_KEY_PATH, "rb") as pemfile:
            private_key = pemfile.read()

        payload = {
            "iss": f"{self.api_settings.CLIENT_ID}",
            "scope": "rest_webservices",
            "aud": f"{self.access_token_url}",
            "exp": (datetime.now() + timedelta(seconds=3600)).timestamp(),
            "iat": datetime.now().timestamp()
        }

        headers = {
            "typ": "JWT",
            "alg": "RS256",
            "kid": f"{NETSUITE_CERT_ID}"
        }

        jwt_token = jwt.encode(payload=payload, key=private_key, algorithm='RS256', headers=headers)

        return jwt_token

    def request_access_token(self):
        json_web_token = self.get_jwt()

        data = {
            'grant_type': 'client_credentials',
            'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
            'client_assertion': f'{json_web_token}'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token"
        response = requests.post(url, data=data, headers=headers)
        token = NetsuiteToken(**response.json())
        self.save_token(token)
        return self.token

    def change_app(self, app_name):
        self.app_name = app_name
        if not self.token.access_token:
            raise Exception(f"{app_name} does not have a token in storage, please authenticate")
        self.rest_v1 = REST_V1(self)
