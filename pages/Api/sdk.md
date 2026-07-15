# Python SDK — codi

`codi` provides a high-level TCP interface for controlling and monitoring
a CORA robot without writing ROS 2 directly.

## Installation

```bash
# From source (recommended during development)
cd codi && pip install -e .

# Once published
pip install codi
```

## Basic usage — client

```python
from codi import CoraClient

arm = CoraClient(filepath="config.yaml")
arm._activate()

# Send a Cartesian pose command
arm.send_command(pose_command=(0.1, 0.0, 0.3, 0.0, 0.0, 0.0))

# Send a joint-space command
arm.send_command(joint_command=(0.0, 1.57, -0.5, 0.0, 0.0, 0.0))

# Read latest state
state = arm.get_states()
print(state.joint_states)
print(state.transforms)

# Read latest video frame (requires use_camera=True)
frame = arm.get_frame()
```

## Basic usage — server

```python
from codi import CoraServer

server = CoraServer(filepath="config.yaml")
server.start()

# In your control loop:
server.send_state(transforms, jointstates, status)
server.send_frame(image)

command = server.get_command()
config  = server.get_config()
```

## Config file

```yaml
host: 192.168.1.100
ports:
  command_port: 5000
  states_port:  5001
  video_port:   5002
  config_port:  5003
```

:::{note} Connection lifecycle
`CoraClient._activate()` launches a background supervisor thread that
automatically reconnects if the server drops. `CoraServer.start()` does
the same on the server side — it re-accepts a new client after any
disconnect.
:::

## Full API reference

See [Python SDK API Reference](../api/python/index.rst) for all classes,
methods, parameters, and exceptions generated directly from
`codi/src/` docstrings.