import yaml
from simple_salesforce import Salesforce

def get_salesforce_connection(config_path='config/dev.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    sfdc_config = config['sfdc']
    sf = Salesforce(username=sfdc_config['username'], password=sfdc_config['password'], security_token=sfdc_config['token'])
    return sf

def query_accounts(sf):
    query = """
    SELECT Id, Name, Website, Phone, BillingStreet, BillingCity, BillingState, BillingPostalCode, BillingCountry,
    ShippingStreet, ShippingCity, ShippingState, ShippingPostalCode, ShippingCountry, LastModifiedDate
    FROM Account
    """
    return sf.query(query)['records']