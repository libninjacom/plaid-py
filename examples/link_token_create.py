import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.link_token_create(
        client_name="your client name",
        language="your language",
        country_codes=["your country codes"],
        user=LinkTokenCreateRequestUser(
            id_number=UserIdNumber(
                value="your value",
                type="your type",
            ),
            address=UserAddress(
                street_2="your street 2",
                region="your region",
                street="your street",
                city="your city",
                postal_code="your postal code",
                country="your country",
            ),
            legal_name="your legal name",
            phone_number="your phone number",
            email_address="your email address",
            client_user_id="your client user id",
            email_address_verified_time="your email address verified time",
            date_of_birth="your date of birth",
            phone_number_verified_time="your phone number verified time",
            name=UserName(
                family_name="your family name",
                given_name="your given name",
            ),
            ssn="your ssn",
        ),
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.link_token_create(
        client_name="your client name",
        language="your language",
        country_codes=["your country codes"],
        user=LinkTokenCreateRequestUser(
            id_number=UserIdNumber(
                value="your value",
                type="your type",
            ),
            address=UserAddress(
                street_2="your street 2",
                region="your region",
                street="your street",
                city="your city",
                postal_code="your postal code",
                country="your country",
            ),
            legal_name="your legal name",
            phone_number="your phone number",
            email_address="your email address",
            client_user_id="your client user id",
            email_address_verified_time="your email address verified time",
            date_of_birth="your date of birth",
            phone_number_verified_time="your phone number verified time",
            name=UserName(
                family_name="your family name",
                given_name="your given name",
            ),
            ssn="your ssn",
        ),
    )
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
