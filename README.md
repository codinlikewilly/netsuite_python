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

* #### Notes ####
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

## Generating x509 certificate for Netsuite ###
 * Run `netsuite generate-certificate`
   * Domain: theapiguys.com
   * Organization: TAG 
   * Department: DEV
   * City: BOSTON
   * State: MA
   * Country: US
   * Email: will@theapiguys.com
 
 * It will ask for the file name that you wish to save the key to. This will be used when entering the creds.

## Uploading x509 certificate to Netsuite ##
* On Client's Netsuite top ribbon go to `Setup -> Integration -> OAuth 2.0 Client Credentials`
* Click `Create-New` button
    * Entity: The User created for TAG
    * ROLE: Role created for this integration
    * Application: Application Created for this integration
    * Certificate: Click "Choose A File" and upload the PUBLIC Cert (NOT PRIVATE KEY)
* Copy the Certificate ID
## Setting up Netsuite SDK in a project ##
* Run `netsuite generate-client-config`
    * It will ask you for information obtained above: You can use all the defaults
        * Client ID
        * Netsuite Certificate ID
        * Netsuite Key File
        * Netsuite Application Name
        * Allow None
        * Use Datetime
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


## Usage ##


It is pretty simple to get started using the SDK once you have a valid token.

### Setup Netsuite ###
```
import pathlib
from netsuite import Netsuite

#Include config file, config dict, or leave empty to use default setup

# w/ config file 
# netsuite = Netsuite(config_file=pathlib.Path('./netsuite-credentials.json'))

# using default 
netsuite = Netsuite()

#initialize apis
ns_contact_api = netsuite.REST_CLIENT.contact_api
ns_customer_api = netsuite.REST_CLIENT.customer_api
```