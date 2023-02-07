import json
import pathlib
import jwt
from datetime import datetime, timedelta
from pathlib import Path
import requests
from netsuite.NetsuiteToken import NetsuiteToken
from netsuite.swagger_client.rest_client import RestClient, QueryClient
from netsuite.settings import APISettings
from netsuite.storages import BaseStorage, JSONStorage


class Netsuite:
    app_name: str = None
    storage: BaseStorage = None
    api_settings: APISettings
    rest_client = None
    query_client = None

    def __init__(self, config: dict = None, config_file: Path = None):
        if config and config_file:
            raise ValueError("You can only load settings from one source")
        if config_file:
            with open(config_file, 'r') as f:
                config = json.load(f)
        if config is None and config_file is None:
            try:
                with open(pathlib.Path(APISettings().defaults.get("CREDENTIALS_PATH")), 'r') as f:
                    config = json.load(f)
            except Exception as e:
                raise Exception("No Configuration Present. Try Generating one.")

        self.api_settings = APISettings(config)
        if not self.api_settings.CLIENT_ID:
            raise Exception("Missing Client Id")
        if not self.api_settings.NETSUITE_APP_NAME:
            raise Exception("Missing Netsuite App Name")
        if not self.api_settings.NETSUITE_KEY_FILE:
            raise Exception("Missing Netsuite Certificate path.")
        if not self.api_settings.CERT_ID:
            raise Exception("Missing Netsuite Certificate ID.")

        self.app_name = self.api_settings.APP_NAME
        self.netsuite_app_name = self.api_settings.NETSUITE_APP_NAME
        self.netsuite_key_path = self.api_settings.NETSUITE_KEY_FILE
        self.netsuite_cert_id = self.api_settings.CERT_ID

        self.storage = self.api_settings.STORAGE_CLASS()
        if isinstance(self.api_settings.STORAGE_CLASS(), JSONStorage):
            if not self.api_settings.JSON_STORAGE_PATH:
                raise Exception("JSON_STORAGE_PATH must be defined for JSONStorage")
            self.storage.storage_path = self.api_settings.JSON_STORAGE_PATH
        self.rest_url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest" \
                        f"/record/v1/ "
        self.access_token_url = f"https://{self.api_settings.NETSUITE_APP_NAME}.suitetalk.api.netsuite.com/services/rest/auth/oauth2/v1/token",

    @property
    def REST_CLIENT(self):
        if not self.rest_client:
            self.rest_client = RestClient(self)
        return self.rest_client

    @property
    def QUERY_CLIENT(self):
        if not self.query_client:
            self.query_client=QueryClient(self)
        return self.query_client

    @property
    def token(self) -> NetsuiteToken:
        return self.storage.get_token(self.app_name)

    def save_token(self, token):
        self.storage.save_token(self.app_name, token)

    def get_jwt(self):
        private_key = ""
        with open(self.netsuite_key_path, "rb") as pemfile:
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
            "kid": f"{self.netsuite_cert_id}"
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
        # self.rest_v1 = REST_V1(self)
        self.rest_client = RestClient(self)

    def get_token(self):
        if not self.token.is_expired:
            return self.token
        else:
            return self.request_access_token()
