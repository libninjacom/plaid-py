import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.transactions_enhance(account_type, transactions)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.transactions_enhance(account_type, transactions)
    print(f"{response!r}")


account_type = "your account type"
transactions = [
    ClientProvidedRawTransaction(
        description="your description",
        iso_currency_code="your iso currency code",
        id="your id",
        amount=1.0,
    )
]
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
