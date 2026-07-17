# CORA

CORA (Collaborative Open Robotic Arms) is a modular cobot platform. Design your arm in the
configurator, generate matching CAD and ROS 2 software automatically, build it, and run it.

:::{note} Alpha release
The project is currently under active development, APIs may change between minor versions.
:::

## What is CORA?

Cora is an open source and modular robotic system. This project focuses on the design and  development of interchangable cobot joints. Each joint can be swapped for another one with minimal effort. The on-board robot software is also reconfigurable to match any robot configuration.

## Workflow

Designing, Building and programming your own arm involves several steps as follows:

<div>
    <img src="_static/assets/diagrams/workflow.png" alt="workflow" style="width:100%;border-radius:6px;margin-bottom:12px;">
</div>


## Pipeline

A lot of documentation is available for this platform, however it is advised to read the following.

<div class="card-grid">
  <a class="card" href="pages/03_Configurator/configurator.html">
    <div class="card-icon">
    <img src="_static/assets/icons/configurator.png" 
    style="width:32px !important;height:32px !important;object-fit:contain;object-position:center;">
    </div>
    <div class="card-title">Configurator</div>
    <div class="card-desc">Browser-based app to compose joints, set parameters, and preview the arm in 3D.</div>
  </a>
  <a class="card" href="pages/Api/ros2-setup.html">
    <div class="card-icon" style="display:flex;gap:6px;align-items:center;">
      <!-- <img src="https://www.onshape.com/favicon.ico" style="width:28px;height:28px;object-fit:contain;"> -->
      <img src="https://upload.wikimedia.org/wikipedia/commons/b/bb/Ros_logo.svg" 
      style="width:80px !important;height:40px;object-fit:contain;filter:invert(1);">
    </div>
    <div class="card-title">Robot Software</div>
    <div class="card-desc">ROS2 Packages documentation</div>
  </a>
  <a class="card" href="api/python/index.html">
    <div class="card-icon">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"
    style="width:32px !important;height:32px !important;object-fit:contain;object-position:center;">
     </div>
    <div class="card-title">API reference</div>
    <div class="card-desc">API reference of CoDI.</div>
  </a>
  <a class="card" href="pages/General/joints.html">
    <div class="card-icon">
    <img src="_static/assets/icons/joints.png"
    style="width:32px !important;height:32px !important;object-fit:contain;object-position:center;">
    </div>
    <div class="card-title">Joints</div>
    <div class="card-desc">Specs and build guide for each joint</div>
  </a>
</div>

## Projects

Some examples of robots built with our system.

## Joints

All the joints in our library.
[]()
