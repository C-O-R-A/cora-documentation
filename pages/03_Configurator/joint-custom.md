# Adding a Custom Joint

CORA is designed to be extended without modifying platform code.
A new joint type is a self-contained folder.

## Folder structure

```
<ros_package>/joints/
└── your_joint_id/
    ├── manifest.json       # required — see Joint Manifest Schema
    ├── cad.py              # CadQuery parametric script
    ├── mesh.dae            # visual mesh
    └── mesh_collision.stl  # simplified collision mesh
```

## Steps

**1. Create the folder**

Use your joint ID (snake_case) as the folder name.

**2. Write `manifest.json`**

Follow the [Joint Manifest Schema](schema.md). Validation runs on
server startup — the backend will refuse to start if any manifest is invalid.

**3. Write `cad.py`**

A CadQuery script that accepts the `params` dict from the manifest
and returns the path to a STEP file. The export pipeline calls
`build(params) → Path`.

```python
import cadquery as cq
from pathlib import Path

def build(params: dict) -> Path:
    d = params["housing_diameter_mm"]
    result = cq.Workplane("XY").cylinder(
        height=params.get("height_mm", 60),
        radius=d / 2,
    )
    out = Path("/tmp/output.step")
    cq.exporters.export(result, str(out))
    return out
```

**4. Add mesh files**

Provide a visual mesh (`.dae` or `.stl`) and a simplified collision
mesh (`.stl`). Reference both in the manifest `mesh` field.

**5. Restart the backend**

The joint appears in the configurator automatically. No code changes required.
