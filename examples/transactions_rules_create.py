import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.transactions_rules_create(
        client_id="your client id",
        access_token="your access token",
        secret="your secret",
        personal_finance_category="your personal finance category",
        rule_details=TransactionsRuleDetails(
            query="your query",
            type="your type",
            field="your field",
        ),
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.transactions_rules_create(
        client_id="your client id",
        access_token="your access token",
        secret="your secret",
        personal_finance_category="your personal finance category",
        rule_details=TransactionsRuleDetails(
            query="your query",
            type="your type",
            field="your field",
        ),
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
