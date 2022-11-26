<div id="top"></div>

<p align="center">
    <a href="https://github.com/libninjacom/plaid-py/stargazers">
        <img src="https://img.shields.io/github/stars/libninjacom/plaid-py.svg?style=flat-square" alt="Stars" />
    </a>
    <a href="https://github.com/libninjacom/plaid-py/actions">
        <img src="https://img.shields.io/github/workflow/status/libninjacom/plaid-py/ci?style=flat-square" alt="Build Status" />
    </a>
    
<a href="https://pypi.org/project/plaid2">
    <img src="https://img.shields.io/pypi/dm/plaid2?style=flat-square" alt="Downloads" />
</a>

<a href="https://pypi.org/project/plaid2">
    <img src="https://img.shields.io/pypi/v/plaid2?style=flat-square" alt="Pypi" />
</a>

</p>

Plaid client, generated from the OpenAPI spec.

# Usage

```python
import os
from plaid2 import AsyncPlaidClient
from plaid2 import PlaidClient

def main():
    client = PlaidClient.from_env()
    response = client.item_application_list()
    print(f"{response!r}")

async def async_main():
    client = AsyncPlaidClient.from_env()
    response = await client.item_application_list()
    print(f"{response!r}")


if __name__ == "__main__":
    if os.environ.get("ASYNC"):
        import asyncio
        asyncio.run(async_main())
    else:
        main()


```

This example loads configuration from environment variables, specifically:

* `PLAID_ENV`

* `PLAID_CLIENT_ID`

* `PLAID_SECRET`

* `PLAID_VERSION`

# Documentation

You can see working examples of every API call in the `examples/` directory.

# Contributing

Contributions are welcome!

*Library created with [Libninja](https://www.libninja.com).*