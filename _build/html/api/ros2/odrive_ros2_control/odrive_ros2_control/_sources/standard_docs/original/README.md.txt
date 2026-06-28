# ODrive ros2_control Plugin

This package serves as a hardware interface to control ODrives from [ros2_control](https://control.ros.org/master/index.html).

It assumes that the ODrive is already configured and calibrated (see [docs](https://docs.odriverobotics.com/v/latest/guides/getting-started.html) for details).

**This is a work in progress** (see **Features**).

>This package is only compatible with ODrive v3.6. It is a modified version of the official odrive ros2 control package which is only compatible with ODrive S1/Pro.

## Features

- Communicates over Linux SocketCAN
- Position Control (with optional velocity and torque feedforward)
- Velocity Control (with optional torque feedforward)
- Torque Control
- Automatic control mode selection (based on which Command Interfaces are claimed by the ros2_control Controller)
- Position, velocity and torque Feedback
- Multiple ODrives

**TODO:**

- Error feedback & error handling: If an ODrive disarms for some reason (e.g. undervoltage), the application that connects to ros2_control will currently not be notified.
- Reduction ratio's, in ros2 control xacro or urdf?


## Parameters

Top level:

- `can`: Name of the CAN interface to run on

Per joint:

- `node_id`: `node_id` of the ODrive

## Command Interfaces

(from ros2_control Controller to ODrive)

- `position`
- `velocity`
- `effort` (aka Torque)

## State Interfaces

(from ODrive to ros2_control Controller)

- `position`
- `velocity`
- `effort` (aka Torque)
