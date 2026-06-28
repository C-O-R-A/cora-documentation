Validation
==========

Command schema and semantic validation. Called automatically inside
:meth:`~codi.client.CoraClient.send_command` — you do not normally
need to call these directly.

.. autofunction:: codi.validation.validate_command_schema
.. autofunction:: codi.validation.validate_command_semantic
.. autofunction:: codi.validation.status
