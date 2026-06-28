Python SDK — codi
=================

Auto-generated from docstrings in ``codi/src/codi/``.

.. toctree::
   :maxdepth: 2

   client
   protocol
   runtime
   validation
   exceptions

----

Quick reference
---------------

.. code-block:: python

   # Typical client usage
   from codi.runtime import start_client, get_client, stop_client

   start_client("path/to/config.yaml")
   client = get_client()
   client.send_command({...})
   stop_client()

   # Or manage the client directly
   from codi.client import CoraClient

   client = CoraClient("path/to/config.yaml")
   client.connect()
   client.send_command({...})
   client.cleanup()
