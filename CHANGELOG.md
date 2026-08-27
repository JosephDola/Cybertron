# Cybertron Changelog

This is the preserved development sequence from the Cybertron update packages. Older experiments remain documented even when later builds replaced them.

1. Motion foundation
2. Reactive AI core
3. Launcher fix
4. Responsive UI + screen capture foundation
5. Resize crash fix
6. Voice foundation
7. Unified Live / Iapetus experiment
8. ElevenAgents cloud experiment
9. ElevenAgents cloud fix
10. ElevenAgents cloud v3
11. AVA/JARVIS full rebuild
12. OpenRouter cloud brain
13. Responsive performance pass
14. Stability + brain validation
15. Startup recovery
16. Qt / Big Sur compatibility
17. Camera + hand + voice upgrade
18. Voice conversation fix
19. New Element spatial engine V1
20. New Element spatial engine V2
21. New Element spatial engine V3
22. Spatial alignment V4
23. Spatial Lite V5
24. Spatial Research V6
25. Core Depth V7
26. Spatial Voice + Mac Control V8
27. Gaze Voice V9
28. Gaze Single-Window V10
29. Gaze Model Fix V11
30. V12 Hardware Discovery
31. V12.1 Voice Restore
32. V12.2 Real-Time Hardware + System Engine
33. V13 Asset Intelligence Core
34. V13.0.1 Scanner/Monitor Compatibility Hotfix
35. V13.0.2 Runtime Integrity Repair

Detailed notes: [`docs/updates/`](docs/updates/).

## V13.0.2 — Runtime Integrity Repair

- Fixed startup failure caused by the V13 UI importing `telemetry.system_monitor` while a partial V13 installation did not contain the `telemetry/` package.
- Changed the repair strategy from isolated-file patches to deployment of the complete matched V13 runtime.
- Added full-runtime syntax compilation and internal-import closure validation before the live tree is launched.
- Added real import preflight through `telemetry`, hardware, asset intelligence, diagnostics, screen awareness, voice, and `ui.main_window`.
- Added telemetry and hardware preflights so packaging/version failures are reported by the installer instead of appearing later during normal startup.

## V13.0.1 — Scanner/Monitor Compatibility Hotfix

- Fixed the V13 startup crash caused by a new hardware monitor being installed over an older scanner API.
- V13.0.1 explicitly ships the matching tiered `hardware/scanner.py`.
- Hardened `hardware/monitor.py` so optional scanner APIs are feature-detected instead of assumed during import.
- Added graceful compatibility fallbacks for older scanners rather than allowing a module-import crash.

## V13.0 — Asset Intelligence Core

- Added a persistent engineering asset model above raw hardware endpoints.
- Added endpoint-to-asset resolution so USB + serial interfaces can represent one physical board.
- Added identity confidence, identity evidence, manufacturer/family metadata, capabilities, and documentation targets.
- Added local asset registry under `~/.config/cybertron/asset_registry.json`.
- Added persistent diagnostic sessions under `~/.config/cybertron/diagnostic_sessions.json`.
- Added device profiles for major microcontroller families, USB-UART bridges, debuggers, CAN interfaces, test instruments, and common industrial controller/drive names.
- Added asset connect/disconnect events and asset-aware voice announcements.
- Changed `What did I just plug in?` to prefer the resolved asset instead of a raw endpoint.
- Added `Show raw hardware` for low-level endpoint diagnostics.
- Added asset and diagnostic context to cloud reasoning.
- Batched asset-registry writes so the new identity layer does not add expensive disk I/O to the fast hardware scan loop.

## V12.2 — Real-Time Hardware + System Engine

- Rebuilt hardware monitoring into fast/medium/slow cached discovery tiers.
- Added modern IOKit USB scanning plus fallback paths.
- Added HID, serial, external storage, Bluetooth, audio, camera, Thunderbolt, display, and FireWire discovery.
- Added real-time CPU, memory, disk, battery, uptime, network, and thermal-state telemetry.
- Added live system context to cloud reasoning.

## V12.1 — Voice Restore

- Restored the macOS speech fallback and fixed speech-state recovery.

## V12 — Hardware Discovery

- Added live USB/serial hardware discovery, common engineering-device identification, and hardware connect/disconnect events.
