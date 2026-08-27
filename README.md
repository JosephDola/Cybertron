# C.Y.B.E.R.

**An AI assistant for people who build, test, and repair hardware.**

C.Y.B.E.R. is designed to understand both **your computer** and the **hardware connected to it**. The goal is simple: instead of digging through menus, device lists, logs, manuals, and error messages, you can ask C.Y.B.E.R. what is happening and work through the problem with it.

> Plug something in. Ask what it is. Ask what your computer sees. Start troubleshooting.

## What C.Y.B.E.R. can do right now

- **Talk with you** using voice.
- **Detect connected hardware** such as USB and serial devices.
- **Recognize common engineering hardware** such as ESP32 boards, Arduino boards, USB-to-serial adapters, debuggers, storage, input devices, and more.
- **Keep unknown devices visible** instead of pretending it knows what they are.
- **Combine related connections into one device.** For example, an ESP32 that appears once as USB and once as a serial port can be treated as one physical asset.
- **Read live Mac information** such as CPU, memory, disk, battery, network, uptime, and thermal state.
- **Remember hardware it has seen before.**
- **Create diagnostic sessions** so troubleshooting steps and observations are not forgotten.
- **Use screen awareness** when requested.

C.Y.B.E.R. is still an **alpha project**, so we are currently focused on making hardware detection, system awareness, and startup reliability extremely solid.

## Example

You connect an ESP32.

**C.Y.B.E.R.:** “ESP32-S3 detected.”

**You:** “What connection is it using?”

**C.Y.B.E.R.:** “USB is connected and a serial interface is available.”

**You:** “Start a diagnostic session. It won’t upload.”

C.Y.B.E.R. can now keep the device identity, current system information, and your troubleshooting notes together while you work on the problem.

That is the direction of the product: **an AI that understands the real hardware you are working on, not just the question you typed.**

## Current version

### V13.0.2 — Runtime Integrity Repair

This update fixes the V13 installation problems that could cause startup errors such as missing `telemetry` files or mismatched hardware scanner files.

V13.0.2 now installs the complete matching runtime together and checks it before launching C.Y.B.E.R.

See [`releases/v13.0.2/README.md`](releases/v13.0.2/README.md) for the release notes.

## Useful commands

- `Show assets`
- `Show current asset`
- `What did I just plug in?`
- `What can I do with this device?`
- `Show raw hardware`
- `System information`
- `CPU usage`
- `RAM usage`
- `Start diagnostic session`
- `Diagnostic status`
- `Note that ...`
- `End diagnostic session`

## Where this is going

The bigger goal is to turn C.Y.B.E.R. into an **AI field and engineering assistant**.

A technician or engineer should eventually be able to point C.Y.B.E.R. at a machine or board and have it combine:

- the hardware it can detect,
- what the camera sees,
- what is happening on the computer,
- live device data,
- manuals and datasheets,
- previous repair history,
- and the current troubleshooting session.

Then the user can simply ask things like:

> “What am I working on?”
>
> “Why is this failing?”
>
> “Show me the correct manual.”
>
> “What happened the last time this device failed?”

For professional and industrial use, technical guidance should come from verified documentation and approved procedures rather than guessed instructions.

## Roadmap

1. **Perfect hardware detection** — reliably recognize what is connected.
2. **Documentation intelligence** — connect devices to the right manuals, pinouts, and datasheets.
3. **Serial and telemetry intelligence** — understand logs and live engineering data.
4. **Hardware vision** — recognize boards, components, connectors, tools, and indicators with a camera.
5. **Project and repair memory** — remember what was built, tested, changed, and fixed.
6. **Field support** — guide technicians using the correct documentation and live context.
7. **Fleet intelligence** — help companies understand repeated failures across many machines.

## Platform

Development is currently focused on **macOS**, with Windows support planned.

The release target is a normal desktop application so users do not need to launch C.Y.B.E.R. from Terminal or manage Python themselves.

- macOS: `Cybertron.app` / `.dmg`
- Windows: `.exe` / installer

## For developers

C.Y.B.E.R. currently uses Python, PySide2, OpenCV, and NumPy, with heavier AI work designed to run in the cloud so the desktop app can stay lightweight.

Development history is documented in [`CHANGELOG.md`](CHANGELOG.md) and [`docs/updates/`](docs/updates/).
