# Start Here — What is C.Y.B.E.R.?

C.Y.B.E.R. is an AI assistant for people who work with computers, electronics, and hardware.

The easiest way to understand it is this:

> **C.Y.B.E.R. tries to understand what is connected to your computer, what your computer is doing, and what problem you are trying to solve — then lets you talk through the problem with it.**

## A simple example

You plug an ESP32 board into your computer.

Normally, you might need to open system information, find the USB device, find the serial port, check the IDE, search for the board model, and then start looking through error messages.

C.Y.B.E.R. is being built to bring that information together.

You should be able to say:

**You:** “Cyber, what did I just plug in?”

**C.Y.B.E.R.:** “I detected an ESP32-S3. USB is connected and a serial port is available.”

**You:** “It won’t upload. Start troubleshooting.”

C.Y.B.E.R. can keep the device information, your computer’s current state, and your troubleshooting notes together while you work.

## What works today

C.Y.B.E.R. currently focuses on:

- voice conversation,
- connected hardware detection,
- common engineering-device recognition,
- live computer information such as CPU and memory,
- remembering devices,
- combining related USB and serial connections into one physical device,
- and saving diagnostic sessions.

It is still an alpha project, so reliability is the main priority right now.

## What we are building toward

The long-term idea is much bigger.

Imagine a technician working on a machine. C.Y.B.E.R. could eventually combine:

1. **What is physically connected** to the computer.
2. **What the camera sees** on the machine or circuit board.
3. **What is happening on the computer** or engineering software.
4. **Live device data** such as serial logs or sensor readings.
5. **The correct manual, datasheet, or company procedure.**
6. **What happened during previous repairs.**

Then the technician could simply ask:

> “What is wrong?”
>
> “What does this error mean?”
>
> “Show me the right manual.”
>
> “What fixed this problem last time?”

That is the direction of C.Y.B.E.R.: **an AI that understands the real technical situation around you, not just a text prompt.**

## Why hardware detection matters

The first step is making C.Y.B.E.R. reliably understand what the computer can see.

A single board can appear as several separate things to an operating system. For example, an ESP32 might appear as a USB device and also as a serial port.

C.Y.B.E.R. tries to combine those signals into one real device so the user does not have to understand the operating system’s raw device list.

## Current version

The current repair build is **V13.0.2**.

V13 introduced the Asset Intelligence system. V13.0.2 fixes installation problems so all of the matching runtime files are installed together and checked before C.Y.B.E.R. launches.

See [`../releases/v13.0.2/README.md`](../releases/v13.0.2/README.md) for the latest release notes.
