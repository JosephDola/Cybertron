# C.Y.B.E.R. V13.0.2 — Runtime Integrity Repair

V13.0.2 fixes a partial-upgrade packaging failure discovered after V13.0.1.

## Root cause

`ui/main_window.py` imports `telemetry.system_monitor`, but the V13 installer copied only `core/`, `hardware/`, `ui/`, and `providers/`. On systems that had not already received the complete V12.2 runtime, Cybertron failed at startup with `ModuleNotFoundError: No module named 'telemetry'`.

V13.0.1 repaired the scanner/monitor mismatch but still updated only the hardware pair, so it did not close the full runtime dependency graph.

## Fix

The V13.0.2 repair installer deploys the complete matched V13 runtime as one versioned unit: `core/`, `hardware/`, `providers/`, `screen/`, `telemetry/`, `ui/`, `vision/`, `voice/`, and `main.py`.

It does not reinstall or upgrade third-party dependencies. Local settings, the asset registry, and diagnostic history are preserved.

Before relaunch, the installer compiles every runtime Python module, verifies that internal imports resolve to files in the installed tree, then performs a real import preflight through `ui.main_window` plus telemetry and hardware preflights.