def transform_accounts(accounts):
    transformed_accounts = []
    for account in accounts:
        transformed_account = {
            "id": account.get("Id", ""),
            "name": account.get("Name", ""),
            "email": account.get("Website", ""),
            "phone": account.get("Phone", ""),
            "billingAddress": {
                "street": account.get("BillingStreet", ""),
                "city": account.get("BillingCity", ""),
                "state": account.get("BillingState", ""),
                "postalCode": account.get("BillingPostalCode", ""),
                "country": account.get("BillingCountry", "")
            },
            "shippingAddress": {
                "street": account.get("ShippingStreet", ""),
                "street2": "Nowhere",
                "city": account.get("ShippingCity", ""),
                "state": account.get("ShippingState", ""),
                "postalCode": account.get("ShippingPostalCode", ""),
                "country": account.get("ShippingCountry", "")
            },
            "lastModifiedDate": account.get("LastModifiedDate", "")
        }
        transformed_accounts.append(transformed_account)
    return transformed_accounts