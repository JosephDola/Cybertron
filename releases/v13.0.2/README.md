# C.Y.B.E.R. V13.0.2

**Runtime Integrity Repair**

This update fixes the startup problems some V13 installs had.

## What was wrong?

Some V13 updates installed only part of the new code. That meant C.Y.B.E.R. could start with a new UI or hardware monitor but still have older or missing files underneath it.

That caused errors such as:

```text
ModuleNotFoundError: No module named 'telemetry'
```

and scanner/monitor version mismatch crashes.

## What does V13.0.2 fix?

V13.0.2 installs the **complete matching runtime** together instead of patching only one or two files.

It includes the matching:

- core systems
- hardware scanner and monitor
- asset intelligence
- system telemetry
- screen tools
- voice system
- UI
- vision modules
- AI provider layer

Before C.Y.B.E.R. launches, the installer now checks that the important files exist, compile correctly, and can import each other.

## Why this matters

The goal is to stop this cycle:

```text
fix one missing file
↓
launch again
↓
find another missing file
```

The installer should catch those problems **before** C.Y.B.E.R. starts.

## If you are on V13 or V13.0.1

Use **V13.0.2**. It is the current repair build for the V13 Asset Intelligence release.

## Release files

- `cybertron_v13_0_2_runtime_integrity_repair.zip` — installer/update package
- `Cybertron-v13.0.2-source-snapshot.zip` — full source snapshot

### SHA-256

- `cybertron_v13_0_2_runtime_integrity_repair.zip`: `c41b35bee53b622ff2a642ebae9587e2955496b67fbb5dff8200ac7ae1457e98`
- `Cybertron-v13.0.2-source-snapshot.zip`: `b5fe87ee12d2a0fd0f6b117155475b24c79f9645fe877b475f39d4ac475490e9`

More technical details are in [`../../docs/updates/cybertron_v13_0_2_runtime_integrity_repair/README.md`](../../docs/updates/cybertron_v13_0_2_runtime_integrity_repair/README.md).
