Protocol
========

Wire-format encoding and decoding functions. These are used internally
by :class:`~codi.client.CoraClient` and :class:`~codi.client.CoraServer`
but can also be called directly if you are building a custom integration.

.. autofunction:: codi.protocol.encode_commands
.. autofunction:: codi.protocol.decode_commands
.. autofunction:: codi.protocol.encode_pose_feedback
.. autofunction:: codi.protocol.decode_pose_feedback
.. autofunction:: codi.protocol.encode_configs
.. autofunction:: codi.protocol.decode_configs
.. autofunction:: codi.protocol.encode_aruco_poses
.. autofunction:: codi.protocol.decode_aruco_poses
.. autofunction:: codi.protocol.image_to_bytes
.. autofunction:: codi.protocol.bytes_to_image
