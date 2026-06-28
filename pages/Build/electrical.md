# Electrical & Connectors

Each joint has four connectors on its back shell: two for the 60 A power
chain (XT60, in + out) and two for CAN bus (M12 A-coded 5-pin, in + out).

## Connector selection rationale

No single M12 connector family handles both 60 A power and CAN bus
simultaneously. The two-connector-per-side approach is the practical outcome:

| Function | Connector | Rating | Sourcing |
|----------|-----------|--------|----------|
| Power (60 A) | `XT60 panel-mount` | 60 A continuous | Amass XT60PW-M/F, RAMPOW |
| CAN bus | `M12 A-coded 5-pin bulkhead` | 4-pin CAN + shield | Binder 763, Phoenix SACC-M12 |

:::{warning} PCB clearance constraint
Axial PCB depth is approximately 12–18 mm on the revolute_80mm joint.
All connectors must be sourced and verified against this clearance
before ordering the PCB run.
:::
