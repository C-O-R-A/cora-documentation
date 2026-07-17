# Installation

[CoDI (python sdk)](#codi)

## Prerequisites

| Dependency | Version | Required for |
|-----------|---------|-------------|
| Node.js | `≥ 20.x` | Configurator frontend |
| Python | `≥ 3.11` | codi SDK, backend |
| ROS 2 | `Jazzy` | ROS 2 packages, simulation |
| MoveIt 2 | `Jazzy branch` | ROS 2 packages |
| Gazebo | `Harmonic` | Simulation only |

## ROS packages

1. Clone the repository

    Robot

    ```bash
    git clone https://github.com/C-O-R-A/cora_robot.git
    ```

    Simulation

    ```bash
    git clone https://github.com/C-O-R-A/cora_desktop.git
    ```

2. Run install script
    > *This installs all dependencies, and builds the workspace*

    ```bash
    bash ./install.sh
    ```

## Codi

### Linux

Create a venv and source it:

```bash
python3 -m venv .venv\
source .venv/bin/activate
```

Install from github

```bash
pip install git+https://github.com/C-O-R-A/CoDI.git@main
```

Or install a specific release:

```bash
pip install git+https://github.com/C-O-R-A/CoDI.git@v0.1.0
```


Local installation (development)

```bash
git clone https://github.com/C-O-R-A/CoDI.git
cd codi
pip install -e .
```

### Windows

install globally from github

```bash
pip install git+https://github.com/C-O-R-A/CoDI.git@v0.1.0
```

### Setup

#### Assign static IPs

>Before the client pc can connect to the robot, static ethernet ip's must be configured. 

##### Linux setup:

###### 1. Create a new Netplan file if none exists already

```bash
sudo nano /etc/netplan/02-ethernet-static.yaml
```

Paste this exactly:

```yaml
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    enx503eaa8b7587:
      dhcp4: no
      addresses:
        - 192.168.10.2/24
```

###### 2. Apply the new configuration

```bash
sudo netplan apply
```

Verify it worked

```bash
ip a show
```

You should now see:

```bash
inet 192.168.10.2/24 scope global <ethernet interface name>
```

##### Windows setup:

Navigate to your network settings, then ethernet, then to the ethernet adapter connected to the robot.
> Windows 10 often **requires a gateway and DNS** in the Settings app, even for a direct Ethernet link.

###### IPv4 Settings

- **IP address:** `192.168.10.2`
- **Subnet prefix length:** `24`
- **Default gateway:** `192.168.10.1`
- **Preferred DNS:** `1.1.1.1` (or `8.8.8.8`)

> The gateway/DNS are only to satisfy Windows, the PCs will still talk directly.

###### Steps (recommended / reliable way)

1. Press `Win`
2. Go to **Settings**
3. Click **Network & Internet**
4. Then **Ethernet**
5. Select the adapter corresponding to the robot
6. Scroll down to **IP settings** and click **Edit**
7. Set **IPv4** to **On** 
8. Enter:
   - IP address: `192.168.10.2`
   - Subnet prefix length: `24`
   - Gateway: `192.168.10.1`
   - Preferred DNS: `1.1.1.1`
9. Click **Save**

##### Test

Open Command Prompt and type:

```shell
ping 192.168.10.1
```

or

```shell
ping cora.local
```
