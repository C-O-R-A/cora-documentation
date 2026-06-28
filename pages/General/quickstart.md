# Quickstart

From zero to a simulated running arm in under 30 minutes.

## 1. Clone the repository

```bash
git clone https://github.com/your-org/cora.git
cd cora

# Configurator frontend
cd configurator && npm install && cd ..

# Python SDK (codi)
cd codi && pip install -e ".[dev]" && cd ..
```

## 2. Start the dev servers

```bash
# Terminal 1 — backend API
cd configurator && docker-compose up

# Terminal 2 — frontend
cd configurator && npm run dev
```

## 3. Configure your first arm

Open `http://localhost:5173`. Add joints using the sidebar panel.
The 3D viewport updates live.

## 4. Export your package

Click **Export**. You'll receive a ZIP containing STEP files, a URDF,
MoveIt SRDF, and a ROS 2 package ready to build.

## 5. Launch in simulation

```bash
cd ~/ros2_ws
colcon build --packages-select cora_robot
source install/setup.bash
ros2 launch cora_robot sim.launch.py
```

:::{tip} Expected result
Gazebo opens with your configured arm. RViz2 shows the robot model with
MoveIt 2 loaded. You can send joint goals from the Motion Planning panel.
:::
