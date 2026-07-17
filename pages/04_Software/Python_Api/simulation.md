# Gazebo Simulation

The simulation environment mirrors your physical arm exactly. Run motion
plans in Gazebo before touching hardware to catch configuration errors early.

## Launching

The following command launches the robot in an empty world

```bash
source /opt/ros/jazzy/setup.bash
cd ~/cora_desktop
source install/setup.bash
ros2 launch cora_gazebo gazebo.launch.py
```

To choose a world the robot should spawn in, pass it as launch arg

```bash
ros2 launch cora_gazebo gazebo.launch.py gazebo_world:=../chess/gazebo/worlds/chess/chess.sdf
```

## Custom Worlds

Plenty of use cases exist to make gazebo worlds. As a bonus to this package,
a blender script is used to export from blender to gazebo classic or ignition.