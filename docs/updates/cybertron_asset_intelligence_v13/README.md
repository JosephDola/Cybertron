# C.Y.B.E.R. V13 — Asset Intelligence Core

V13 is the first release organized around **engineering assets** rather than raw operating-system device endpoints.

## Why this exists

A real physical device can appear to macOS as several interfaces at once. An ESP32, for example, may expose a USB identity and a serial device. Earlier Cybertron builds treated those as separate hardware entries. V13 resolves related interfaces into one asset whenever identity evidence is strong enough and preserves them separately when the match would be speculative.

## New systems

- `hardware/assets/model.py` — asset and interface data models.
- `hardware/assets/resolver.py` — endpoint-to-asset identity resolution.
- `hardware/assets/registry.py` — persistent local asset history.
- `hardware/assets/engine.py` — active-asset state and connect/disconnect events.
- `hardware/knowledge/device_profiles.py` — device-family profiles, capabilities, and documentation targets.
- `hardware/diagnostics/session.py` — persistent diagnostic investigation memory.

## Asset profile

Each active asset can carry a stable asset ID, display name, category, manufacturer, model/family when supported by evidence, serial number when exposed by the OS, identity confidence, identity evidence, OS interfaces, device capabilities, documentation targets, and first/last-seen history.

Unknown hardware remains visible as a generic asset with whatever identifiers macOS exposes.

## Performance design

Asset resolution runs over the already-cached V12.2 hardware snapshot. It does not launch extra `system_profiler` or IOKit processes. Registry writes are batched and occur only when identities/interfaces change, devices connect/disconnect, or the baseline is first established.

## Diagnostic sessions

A diagnostic session stores the selected asset, reported symptom, asset identity snapshot, local telemetry snapshot, observations, and final resolution. This creates deterministic investigation memory outside the LLM conversation history.

## Voice/UI commands

- `Show assets`
- `Show current asset`
- `What did I just plug in?`
- `What can I do with this device?`
- `Start diagnostic session`
- `Diagnostic status`
- `Note that ...`
- `End diagnostic session`
- `Show raw hardware`

## Initial profile coverage

V13 includes profiles/capabilities for ESP32 families, ESP8266, Arduino Uno/Nano/Mega, RP2040/Pico, Teensy, CP210x, CH34x, FTDI, ST-LINK, J-Link, Saleae, common Rigol/Keysight/Tektronix/Fluke name patterns, PEAK PCAN, Kvaser, CANable, and name-based profiles for several industrial controller/drive families.

These profiles are evidence-driven. C.Y.B.E.R. keeps an identity confidence score and does not treat a weak match as a verified exact model.
