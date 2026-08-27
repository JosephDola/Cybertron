# C.Y.B.E.R. V13.0.1 — Scanner/Monitor Compatibility Hotfix

Artifacts:

- `cybertron_v13_0_1_compatibility_hotfix.zip`
- `Cybertron-v13.0.1-source-snapshot.zip`

SHA-256:

- `cybertron_v13_0_1_compatibility_hotfix.zip`: `a5c54b737c6aed9558d71faf0a2379303622c45572ab6fc1591795f9f55846a3`
- `Cybertron-v13.0.1-source-snapshot.zip`: `13b5328b11e44d69d7c03cf4fbc39aecb7e794ed77d9283c1def4a495dbc4877`

## Fix

V13.0 could install `hardware/monitor.py` without installing the matching `hardware/scanner.py`. An older scanner therefore caused Cybertron to crash during import because the monitor expected `HardwareScanner.SLOW_SPECS`.

V13.0.1 explicitly installs the matching scanner and makes the monitor backward-compatible so missing optional scanner APIs degrade gracefully instead of crashing startup.

Detailed notes: [`../../docs/updates/cybertron_v13_0_1_compatibility_hotfix/README.md`](../../docs/updates/cybertron_v13_0_1_compatibility_hotfix/README.md)
