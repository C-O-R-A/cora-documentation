Client
======

The ``codi.client`` module provides the two main classes for communicating
with a CORA arm: :class:`CoraClient` for the controlling side and
:class:`CoraServer` for the robot side. Both inherit from the low-level
:class:`CoraInterface` base class.

CoraClient
----------

.. autoclass:: codi.client.CoraClient
   :members: connect, configure, setup, init_threads, start_thread,
             stop_thread, reconcile_threads, kill_options, cleanup,
             update_options, receive_states, get_states,
             receive_vision_poses, get_vision_poses, receive_frame,
             get_frame, send_command, configure_robot
   :show-inheritance:
   :undoc-members:

CoraServer
----------

.. autoclass:: codi.client.CoraServer
   :members: start, connect, start_threads, stop_threads, bind,
             accept_connections, cleanup, receive_command, get_command,
             receive_config, get_config, send_state, send_vision_poses,
             send_frame
   :show-inheritance:
   :undoc-members:


CoraInterface
-------------
Base class shared by both client and server. Not instantiated directly.

.. autoclass:: codi.client.CoraInterface
   :members: get_info
   :show-inheritance:
   :undoc-members:
