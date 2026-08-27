# Cybertron V13.0.1 — Scanner/Monitor Compatibility Hotfix

## Problem

V13 installed a new `hardware/monitor.py` but did not include the matching `hardware/scanner.py`. Systems still carrying the older V12 scanner crashed at startup with:

```text
AttributeError: 'HardwareScanner' object has no attribute 'SLOW_SPECS'
```

## Fix

- Ships the matching tiered hardware scanner explicitly.
- Ships a hardened monitor that does not require `SLOW_SPECS` during module import.
- Adds compatibility wrappers for `scan_medium`, `scan_usb_fallback`, `scan_slow_category`, and `last_errors`.
- If an older scanner somehow appears again, Cybertron falls back to its legacy `scan_full()` path rather than failing to launch.
- Preserves V13 Asset Intelligence, voice, telemetry, and performance settings.

## Dependencies

No new dependencies.
