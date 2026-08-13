# Cybertron Hardware Discovery V12

V12 adds live hardware awareness to Cybertron.

## Features

- Live macOS USB plug/unplug detection.
- Serial endpoint discovery for development boards and USB serial adapters.
- Hardware classification for common microcontrollers, debuggers, adapters, instruments, storage, cameras, audio devices, hubs, mobile devices, and network adapters.
- Unknown USB devices remain visible with their VID/PID instead of being ignored.
- Full hardware scan for external storage, cameras, audio devices, and Thunderbolt devices.
- Connect/disconnect events feed Cybertron's event bus, spatial activity display, telemetry, and optional voice announcements.
- Windows Plug-and-Play discovery foundation for a later Windows build.
- No new runtime dependencies.

## Commands

- `Show hardware`
- `What is connected?`
- `What did I just plug in?`
- `Scan my hardware`
- `Scan all hardware`
- `Hardware status`

The default live scan is intentionally lightweight. Slower full-system inventory is run only when requested.
