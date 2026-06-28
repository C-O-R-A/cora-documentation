# Installation

CORA requires Node.js 20+, Python 3.11+, and ROS 2 Jazzy.
The configurator and Python SDK can run without ROS 2 installed.

## Prerequisites

| Dependency | Version | Required for |
|-----------|---------|-------------|
| Node.js | `≥ 20.x` | Configurator frontend |
| Python | `≥ 3.11` | codi SDK, backend |
| ROS 2 | `Jazzy` | ROS 2 packages, simulation |
| Gazebo | `Harmonic` | Simulation only |
| MoveIt 2 | `Jazzy branch` | Motion planning |

## ROS 2 workspace setup

```bash
# Source system ROS 2 first — always before the local overlay
source /opt/ros/jazzy/setup.bash
cd ~/ros2_ws
colcon build --symlink-install
source install/setup.bash
```

:::{warning} ABI mismatch
If you see a segfault in `gz_ros2_control`, remove `build/`, `install/`,
and `log/` and do a clean rebuild. Always source the system install before
the local overlay — never reverse the order.
:::
