import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient


def main():
    client = PlaidClient.from_env()
    response = client.payment_initiation_consent_payment_execute(
        consent_id, amount, idempotency_key
    )
    print(f"{response!r}")


async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.payment_initiation_consent_payment_execute(
        consent_id, amount, idempotency_key
    )
    print(f"{response!r}")


consent_id = "your consent id"
amount = PaymentAmount(
    value=1.0,
    currency="your currency",
)
idempotency_key = "your idempotency key"
if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio

        asyncio.run(async_main())
    else:
        main()
