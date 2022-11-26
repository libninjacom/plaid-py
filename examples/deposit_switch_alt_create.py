import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.deposit_switch_alt_create(target_account, target_user)
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.deposit_switch_alt_create(target_account, target_user)
    print(f"{response!r}")


target_account = DepositSwitchTargetAccount(
    account_number="your account number",
    account_subtype="your account subtype",
    routing_number="your routing number",
    account_name="your account name",
)
target_user = DepositSwitchTargetUser(
    family_name="your family name",
    address=DepositSwitchAddressData(
        city="your city",
        region="your region",
        street="your street",
        postal_code="your postal code",
        country="your country",
    ),
    given_name="your given name",
    phone="your phone",
    email="your email",
    tax_payer_id="your tax payer id",
)
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
