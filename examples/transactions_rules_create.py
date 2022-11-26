import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.transactions_rules_create(
        access_token, personal_finance_category, rule_details
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.transactions_rules_create(
        access_token, personal_finance_category, rule_details
    )
    print(f"{response!r}")


access_token = "your access token"
personal_finance_category = "your personal finance category"
rule_details = TransactionsRuleDetails(
    query="your query",
    field="your field",
    type="your type",
)
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
