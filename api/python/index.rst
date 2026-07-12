Python SDK — codi
=================

Auto-generated from docstrings in ``codi/src/codi/``.

.. toctree::
   :maxdepth: 2

   interfaces
   runtime
   protocol
   messages
   codi_enums
   exceptions

----

Quick reference
---------------

.. code-block:: python

   # Typical client usage
   from codi.runtime import start_client, get_client, stop_client
   from codi.enums import InterfaceTypes, GoalSpace
   from codi.interfaces import CoraClient

   client = CoraClient("path/to/config.yaml")
   client.connect()
   client.configure_robot(interface_type=InterfaceTypes.POSITION, space=GoalSpace.TS)
   client.send_command()
