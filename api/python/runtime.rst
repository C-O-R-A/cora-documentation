Runtime
=======

Module-level helpers for managing a single global :class:`~codi.client.CoraClient`
instance. Useful for scripts and notebooks where you want a simple
start/stop API without managing the client object yourself.

.. autofunction:: codi.runtime.start_client
.. autofunction:: codi.runtime.get_client
.. autofunction:: codi.runtime.stop_client
