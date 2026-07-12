Messages
========

Pydantic models and dataclasses used as structured payloads across all CoDI
sockets. These are the wire types that :func:`~codi.protocol.encode` and
:func:`~codi.protocol.decode` serialise and deserialise.

ROS primitive types
-------------------

.. autopydantic_model:: codi.messages.Time
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.Header
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.Vector3
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.Quaternion
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.Transform
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.TransformStamped
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.TFMessage
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.JointStates
   :members:
   :show-inheritance:

Wire message types
------------------

.. autopydantic_model:: codi.messages.ImageMessage
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.CommandMessage
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.FeedbackMessage
   :members:
   :show-inheritance:

.. autopydantic_model:: codi.messages.ConfigMessage
   :members:
   :show-inheritance:

Helper dataclasses
------------------

.. autoclass:: codi.messages.JointStateObject
   :members:
   :show-inheritance:

.. autoclass:: codi.messages.TransformObject
   :members:
   :show-inheritance:

.. autoclass:: codi.messages.FeedbackObject
   :members:
   :show-inheritance: