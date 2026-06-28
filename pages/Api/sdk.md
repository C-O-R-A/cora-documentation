# Python SDK (codi)

`codi` provides a high-level interface for joint control and motion
sequencing without writing ROS 2 directly. It wraps the generated
`ros2_control` hardware interfaces.

## Installation

```bash
# From source (recommended during development)
cd codi && pip install -e ".[dev]"

# Once published
pip install codi
```

## Basic usage

```python
from codi import CoraArm

arm = CoraArm("desktop_3dof_v1")
arm.connect()

# Move a single joint
arm.move_joint("shoulder_pan", position=1.57)  # radians

# Named pose from SRDF
arm.go_to_pose("home")

# Cartesian waypoints (requires MoveIt 2)
arm.move_cartesian([
    (0.1, 0.0, 0.3),
    (0.2, 0.1, 0.3),
])

arm.disconnect()
```

## Context manager

```python
with CoraArm("desktop_3dof_v1") as arm:
    arm.go_to_pose("home")
    arm.move_joint("elbow", position=-0.5)
```

:::{note} ROS 2 node lifecycle
`CoraArm` manages its own `rclpy` node. `connect()` calls `rclpy.init()`
if not already initialised. Pass `init_ros=False` when embedding inside
an existing ROS 2 node.
:::

## Full API reference

See [Python SDK API Reference](../api/python/index.rst) for all classes,
methods, parameters, and exceptions — generated directly from
`codi/src/` docstrings.
