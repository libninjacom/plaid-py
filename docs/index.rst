.. container::
   :name: top

.. raw:: html

   <p align="center">

.. raw:: html

   </p>

Plaid client, generated from the OpenAPI spec.

Usage
=====

.. code:: python

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

This example loads configuration from environment variables,
specifically:

-  ``PLAID_ENV``

-  ``PLAID_CLIENT_ID``

-  ``PLAID_SECRET``

-  ``PLAID_VERSION``

Documentation
=============

You can see working examples of every API call in the ``examples/``
directory.

Contributing
============

Contributions are welcome!

*Library created with* `Libninja <https://www.libninja.com>`__\ *.*
