# Primary documentation and instructions

CORA (Collaborative Open Robotic Arms) is a modular cobot platform. Design your arm in the
configurator, generate matching CAD and ROS 2 software automatically, build it, and run it.

:::{note} Alpha release
CORA is under active development. The joint manifest schema is stable; the configurator
UI and Python SDK are in progress. APIs may change between minor versions.
:::

## What is CORA?

Cora is an open source and modular robotic platform. This project focuses on the design and  development of interchangable cobot joints. Each joint can be swapped for another one with minimal effort. The on-board robot software is also reconfigurable to match the real robot configuration.

## Workflow

Building and programming your own CORA involves several steps as follows:

```mermaid
flowchart LR
    A[Configure CORA] --> B[Export Configuration]

    B --> B1[URDF]
    B --> B2[MoveIt Configuration]
    B --> B3[ROS 2 Control Configuration]
    B --> B4[Onshape Document]

    B --> D[Manufacture Components]
    D --> E[Assemble Robot]

    B1 --> F[Install Software]
    B2 --> F
    B3 --> F
    B4 --> F

    E --> F

    F --> G[Set Up Robot Using Generated Files]
    G --> H[Ready to Program and Operate CORA]
```

## Main Documentation Sources

A lot of documentation is available for this platform, however the ones most relevant to a user are the following.

<div class="card-grid">
  <a class="card" href="pages/Configurator/configurator.html">
    <div class="card-icon">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" 
    style="width:32px !important;height:32px !important;object-fit:contain;object-position:center;">
    </div>
    <div class="card-title">Configurator</div>
    <div class="card-desc">Browser-based app to compose joints, set parameters, and preview the arm in 3D.</div>
  </a>
  <a class="card" href="pages/Configurator/export.html">
    <div class="card-icon" style="display:flex;gap:6px;align-items:center;">
      <!-- <img src="https://www.onshape.com/favicon.ico" style="width:28px;height:28px;object-fit:contain;"> -->
      <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Ros_logo.svg" 
      style="width:80px !important;height:80px;object-fit:contain;filter:invert(1);">
    </div>
    <div class="card-title">Export Pipeline</div>
    <div class="card-desc">Auto-generates STEP, URDF/XACRO, MoveIt SRDF, ros2_control YAML, and Python SDK config.</div>
  </a>
  <a class="card" href="pages/Api/simulation.html">
    <div class="card-icon">
    <img src="https://gazebosim.org/assets/images/logos/gazebo_vert_pos.svg" 
     style="width:100px !important;height:100px !important;object-fit:contain;object-position:center;">
     </div>
    <div class="card-title">Simulation</div>
    <div class="card-desc">Gazebo simulation mirrors your exact arm. Validate motion plans before touching hardware.</div>
  </a>
  <a class="card" href="pages/Api/sdk.html">
    <div class="card-icon">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
    style="width:32px !important;height:32px !important;object-fit:contain;object-position:center;">
    </div>
    <div class="card-title">Python SDK</div>
    <div class="card-desc">High-level SDK for joint control and motion planning without writing ROS 2 directly.</div>
  </a>
</div>

## Design principles

| Principle | What it means in practice |
|-----------|--------------------------|
| **Schema-first** | The joint manifest JSON schema is the contract between the configurator, the export pipeline, and the physical build. Lock it before implementing anything else. |
| **Drop-in extensibility** | Adding a new joint type requires only a folder: manifest, mesh files, and a CadQuery script. No platform code changes. |
| **Zero manual integration** | Every exported software package is generated directly from the hardware configuration. The URDF, SRDF, and control YAML always match the physical arm. |
| **REP-103 everywhere** | Z-up, metres, radians throughout — no unit conversions anywhere in the stack. |
