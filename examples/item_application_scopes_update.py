import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.item_application_scopes_update(
        access_token="your access token",
        application_id="your application id",
        scopes=Scopes(
            accounts=[
                AccountAccess(
                    unique_id="your unique id",
                    authorized=True,
                    account_product_access=AccountProductAccessNullable(
                        account_product_access=AccountProductAccess(
                            statements=True,
                            tax_documents=True,
                            account_data=True,
                        ),
                    ),
                )
            ],
            new_accounts=True,
            product_access=ProductAccess(
                transactions=True,
                auth=True,
                accounts_tax_statements=True,
                accounts_details_transactions=True,
                statements=True,
                identity=True,
                accounts_statements=True,
                customers_profiles=True,
                accounts_routing_number=True,
            ),
        ),
        context="your context",
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.item_application_scopes_update(
        access_token="your access token",
        application_id="your application id",
        scopes=Scopes(
            accounts=[
                AccountAccess(
                    unique_id="your unique id",
                    authorized=True,
                    account_product_access=AccountProductAccessNullable(
                        account_product_access=AccountProductAccess(
                            statements=True,
                            tax_documents=True,
                            account_data=True,
                        ),
                    ),
                )
            ],
            new_accounts=True,
            product_access=ProductAccess(
                transactions=True,
                auth=True,
                accounts_tax_statements=True,
                accounts_details_transactions=True,
                statements=True,
                identity=True,
                accounts_statements=True,
                customers_profiles=True,
                accounts_routing_number=True,
            ),
        ),
        context="your context",
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
