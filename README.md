# Cybertron

**C.Y.B.E.R. — an AI engineering companion for software, electronics, robotics, and physical hardware.**

Cybertron is being built as a lightweight desktop AI that can talk naturally, understand the screen when permitted, organize research in a spatial workspace, and eventually help design, debug, and learn from real hardware projects such as Arduino, ESP32, Raspberry Pi, robotics, mechatronics, circuits, sensors, and embedded systems.

## Long-term goal

**The Engineering Copilot for the Physical World.**

Core pillars:

- **Voice** — fast, interruptible, low-latency conversation.
- **Vision** — screen awareness now; hardware/circuit recognition later.
- **Spatial workspace** — research, code, schematics, CAD references, and debugging information around the C.Y.B.E.R. core.
- **Engineering memory** — project-specific parts, wiring, code, tests, and decisions.
- **Debugging** — help diagnose software and hardware problems.

## Current target

Primary development machine:

- Intel MacBook Pro (Late 2013)
- macOS Big Sur 11.7.11
- Python desktop application
- PySide2
- OpenCV
- NumPy
- Cloud AI for expensive inference

Windows support is planned. Platform-specific actions should live behind a small OS integration layer so the AI, UI, voice, research, and future hardware modules stay shared.

## Distribution plan

Cybertron can stay Python internally without making the user run Python or Terminal. The release build should be frozen into a standalone desktop application.

- **macOS:** `Cybertron.app` inside `Cybertron-macOS-x86_64.dmg`
- **Windows:** packaged `Cybertron.exe` application, then a normal Windows installer

See [Packaging](docs/PACKAGING.md).

## Development history

The repo now contains a documented history of the Cybertron update sequence through **V11**. Every preserved update has its own README under [`docs/updates/`](docs/updates/README.md).

See also [CHANGELOG.md](CHANGELOG.md).

## Current priorities

1. Stable ChatGPT-Voice-style conversation with interruption.
2. Lightweight screen awareness.
3. Reliable desktop integration.
4. Hardware engineering mode: parts, pinouts, wiring, serial logs, datasheets, and debugging.
5. Windows platform layer.
6. Research graph and engineering memory.

## Status

Cybertron is an **alpha project**. Historical builds are preserved for reference while the architecture is being consolidated for desktop packaging and the hardware-engineering roadmap.
