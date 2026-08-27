# Cybertron

**C.Y.B.E.R. — The Engineering Copilot for the Physical World.**

C.Y.B.E.R. is being built as a lightweight desktop AI for engineers, technicians, robotics builders, electronics work, and eventually industrial field support. The product combines voice, live computer telemetry, hardware discovery, asset identity, screen awareness, technical knowledge, diagnostic memory, and later hardware vision.

## Product direction

The long-term company direction is an **industrial field-intelligence platform**: C.Y.B.E.R. should understand both the computer and the physical equipment a technician is working on, connect that context to approved documentation and service history, and maintain a structured diagnostic investigation.

Core pillars:

- **Voice** — fast, interruptible hands-free conversation.
- **Hardware discovery** — USB, serial, HID, storage, camera, audio, Bluetooth, displays, Thunderbolt, and unknown devices.
- **Asset intelligence** — collapse raw OS endpoints into persistent physical engineering assets.
- **Live telemetry** — current CPU, memory, disk, battery, network, uptime, and thermal state.
- **Engineering knowledge** — device profiles, capabilities, datasheet/manual targets, and future organization documentation.
- **Diagnostics** — persistent sessions that remember the asset, symptom, observations, evidence, telemetry, and resolution.
- **Vision** — screen understanding now; physical hardware/component recognition next.

## Current release: V13 Asset Intelligence Core

V13 adds an asset layer above V12.2 hardware discovery. A board that appears as both USB and serial can now resolve into one physical asset with multiple interfaces. Each asset can carry an identity-confidence score, evidence trail, manufacturer/family information, capabilities, documentation targets, and persistent local history.

Unknown hardware is still retained instead of being ignored or forced into a guessed model.

Useful commands:

- `Show assets`
- `Show current asset`
- `What did I just plug in?`
- `What can I do with this device?`
- `Start diagnostic session`
- `Diagnostic status`
- `Note that ...`
- `End diagnostic session`
- `Show raw hardware`

See [`docs/updates/cybertron_asset_intelligence_v13/README.md`](docs/updates/cybertron_asset_intelligence_v13/README.md).

## Current platform target

Primary development target:

- Intel MacBook Pro (Late 2013)
- macOS Big Sur 11.7.11
- Python + PySide2
- OpenCV + NumPy
- Cloud AI for expensive inference
- performance-first background hardware/system monitoring

Windows support is planned through a separate OS-integration layer while keeping the shared AI, asset, diagnostic, UI, research, and hardware logic portable.

## Distribution plan

Users should not need Terminal or their own Python installation.

- **macOS:** `Cybertron.app` distributed in `Cybertron-macOS-x86_64.dmg`
- **Windows:** packaged `Cybertron.exe` application and installer

See [`docs/PACKAGING.md`](docs/PACKAGING.md).

## Near-term roadmap

1. Perfect asset identity and hardware discovery reliability.
2. Add verified documentation retrieval and device-specific technical profiles.
3. Add serial/log/telemetry intelligence for engineering hardware.
4. Add hardware vision for boards, tools, components, connectors, and indicators.
5. Add richer diagnostic-session evidence and project/service history.
6. Add industrial connectors and organization-approved maintenance knowledge.
7. Add fleet-level failure and repair analytics.

## Status

C.Y.B.E.R. is an **alpha project**. Identity confidence is evidence-based, and safety-critical/industrial guidance should rely on approved documentation rather than invented repair procedures.
