# README #


This library makes it easy to set up a Netsuite authorization without needing a frontend client using CLI utilities.

### Docs ###
[Netsuite API Documentation](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_158022624537.html)

## What do I need to get set up? ##
* Run `pip install netsuite-python`
* Activate your python VENV
* If using virtual environment 
  * Activate your virtual environment
  * `netsuite = python venv/bin/keap`

# QUICK START #

## Prerequisite  Setup ##
    1. Enable Services
        * Restlets
        * Rest Web Services
        * OAUTH 2.0
    2. Create a role for the integration with the following permissions:
        * Access Token Management
        * Log in using Access Tokens	
        * Log in using OAuth 2.0 Access Tokens	
        * OAuth 2.0 Authorized Applications Management	
        * REST Web Services	
        * SuiteApp Deployment	
        * SuiteScript
        * User Access Tokens	
    3. Create an integration record 
        * Check Client Credentials ( MAchine to Machine Grant)
        * Under Scope Select 
            * Restlets
            * Rest Web Services
        * STORE THE CLIENT ID 
    4. Create and upload the certificate
        * with dev environment setup, run ```netsuite generate-certificate```
        * upload the public cert to Netsuite under Setup -> Integrations -> Manage Oauth 2.0


## Setup The Easy Way  ##
run ``` netsuite initialize ```
* Follow the prompts

* Docs will be located in the generated "netsuite_rest_client folder" at the rot of the project

#### Usage ####
```python
# import Netsuite Package
from netsuite import Netsuite
# import the generated Client
from netsuite_rest_client import apis, rest_api_client
# import models
from netsuite_rest_client.model.customer import Customer
# instantiate the SDK
netsuite = Netsuite()
# Instantiate the generated Client
rest_client = rest_api_client.RestApiClient(netsuite)
# Instantiate the generated API endpoints using the generated client
customer_api = apis.CustomerApi(rest_client)


```

#### Notes ####
  * Requirements
    * Sandbox requires the same setup as Prod, it DOES NOT copy over
    * An administrator for the Netsuite app to follow the steps [here](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_157771281570.html)
      * A user with the correct role
      * A role with the correct permissions
      * An Integration Record with the correct permissions (ensure default form is set correctly)
        * Client ID and Secret comes from this step, ensure they provide these
      * Certificate ID
        * A Certificate can be generated once you register the package with CLI with 'netsuite generate-certificate' 
        * Cert ID is available under Setup -> Integration -> OAuth 2.0 Client Credentials once the certificate is uploaded.

## Use Restlets ##
saved search example ref: https://timdietrich.me/blog/netsuite-saved-search-api/
```python
# import restlet client
restlet_client = netsuite.RESTLET_CLIENT.restlet_api
# create body params 
body_params = {"searchID": 'customsearch184275'}
# call restlet
print(restlet_client.execute_restlet(script=1999, deploy=1, body_params=body))
```

## Regenerating the API Client with more records types
re-run ```netsuite generate-rest-client```
* when asked about using more record types, choose option that lets you set them
* pick record types from the list
* complete prompts

## Uploading x509 certificate to Netsuite ##
* On Client's Netsuite top ribbon go to `Setup -> Integration -> OAuth 2.0 Client Credentials`
* Click `Create-New` button
    * Entity: The User created for TAG
    * ROLE: Role created for this integration
    * Application: Application Created for this integration
    * Certificate: Click "Choose A File" and upload the PUBLIC Cert (called netsuite-certificate.pem by default)
* Copy the Certificate ID


# Other Commands #

## Generating x509 certificate for Netsuite ###
 * Run `netsuite generate-certificate`
   * Domain: theapiguys.com
   * Organization: TAG 
   * Department: DEV
   * City: BOSTON
   * State: MA
   * Country: US
   * Email: will@theapiguys.com
 
 * It will store the cert in a file in the root of the project under config/netsuite


## Setting up Netsuite SDK in a project ##
* Run `netsuite generate-client-config`
    * It will ask you for information obtained above: You can use all the defaults
        * Client ID
        * Netsuite Certificate ID
        * Netsuite Key File
        * Netsuite Application Name 
        * Storage Class
      
    * If you want to save to file
        * Provide a valid path for netsuite-credentials.json
        * else the credentials will be echoed out
    * To confirm, check the netsuite credentials path you entered, or the default, and there should be a json file with all
      the info you entered. Verify the details.

## Getting The Access Token ##
* Run `$netsuite get-access-token`
    * Use the defaults or repeat the info used above for
        * Path to Netsuite Credentials
    * Confirm the app name to be refreshed, if single app, just use default
* That's it! You should now have a valid token to use with the Netsuite API.



