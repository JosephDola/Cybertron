# C.Y.B.E.R. V13.0.2 — Startup & Runtime Repair

This update fixes the V13 startup problems caused by missing or mismatched runtime files.

## What changed

Earlier V13 updates could install only part of the new system. For example, C.Y.B.E.R. could receive the new UI while the telemetry package was still missing, or receive a new hardware monitor while an older scanner was still installed.

That caused startup errors such as:

```text
ModuleNotFoundError: No module named 'telemetry'
```

V13.0.2 changes the update strategy: the matching runtime is treated as one unit and checked before C.Y.B.E.R. launches.

## What this fixes

- missing internal packages,
- scanner/monitor version mismatches,
- partial V13 upgrades,
- startup import failures,
- one-fix-at-a-time dependency problems.

## Who should use it

If you are testing V13 or V13.0.1, move to **V13.0.2**.

## GitHub downloads

This GitHub Release automatically includes:

- `Cybertron-13.0.2-source.zip` — the repository source at the exact release commit,
- `SHA256SUMS.txt` — checksum for the uploaded release files.

The separate Mac repair installer package was produced during development, but it is not yet built by the GitHub Actions release runner. The release workflow is now in place so future versions can automatically attach built Mac and Windows packages once those build jobs are connected.

## What is next

Now that releases are automated, the main focus returns to making hardware detection, live system awareness, and Asset Intelligence reliable before adding more major features.

More technical details are in [`../../docs/updates/cybertron_v13_0_2_runtime_integrity_repair/README.md`](../../docs/updates/cybertron_v13_0_2_runtime_integrity_repair/README.md).
