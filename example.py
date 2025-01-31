from backup.netsuite import Netsuite
from netsuite_client.api.customer_api import CustomerApi

netsuite = Netsuite(config_file=settings.NS_CREDENTIALS_PATH)

customer_api = CustomerApi(netsuite.REST_CLIENT)

print(customer_api.customer_id_get(id=1617260))