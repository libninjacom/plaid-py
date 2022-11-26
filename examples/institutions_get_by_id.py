import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.institutions_get_by_id(institution_id, country_codes)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.institutions_get_by_id(institution_id, country_codes)
    print(f"{response!r}")


institution_id = "your institution id"
country_codes = ["your country codes"]
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
