# Gazebo Simulation

The simulation environment mirrors your physical arm exactly. Run motion
plans in Gazebo before touching hardware to catch configuration errors early.

## Launching

```bash
source /opt/ros/jazzy/setup.bash
source ~/ros2_ws/install/setup.bash
ros2 launch cora_robot sim.launch.py
```

## Sim clock

To suppress the RViz2 sim-clock warning, set `use_sim_time: true`
for the RViz2 node in your launch file:

```python
rviz_node = Node(
    package='rviz2',
    executable='rviz2',
    parameters=[{'use_sim_time': True}],
)
```

## Motion planning with CHOMP

CHOMP is enabled by default. To switch to OMPL, edit
`config/moveit/planning_pipeline.yaml`:

```yaml
planning_plugin: ompl_interface/OMPLPlanner
```
