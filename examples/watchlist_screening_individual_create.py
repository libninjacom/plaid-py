import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.watchlist_screening_individual_create(search_terms)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.watchlist_screening_individual_create(search_terms)
    print(f"{response!r}")


search_terms = WatchlistScreeningRequestSearchTerms(
    country="your country",
    watchlist_program_id="your watchlist program id",
    document_number="your document number",
    legal_name="your legal name",
    date_of_birth="your date of birth",
)

if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
