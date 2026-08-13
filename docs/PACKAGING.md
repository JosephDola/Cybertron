# Packaging Cybertron

## Recommended path

Keep the current Python/PySide2 codebase and **freeze it into a standalone desktop application** instead of rewriting the app just to remove Terminal.

For the current Intel Big Sur target, PyInstaller is the lowest-risk route: it bundles the interpreter and dependencies so the user launches a normal app without installing Python.

## macOS

Build an **onedir + windowed** PyInstaller application. The result is `Cybertron.app`; distribute that inside a DMG.

Recommended output:

```text
Cybertron.app
Cybertron-macOS-x86_64.dmg
```

For Big Sur compatibility, build the official Intel release on the Big Sur machine itself (or another Big Sur build environment). This follows PyInstaller's guidance to freeze on the oldest macOS version you intend to support.

Do not use a one-file/windowed build for the main Mac release; the onedir app starts faster and avoids unpacking the whole runtime on every launch.

## Windows

Use the same source tree and run PyInstaller on Windows. PyInstaller is not a cross-compiler, so Windows artifacts must be built on Windows.

Start with an onedir/windowed build:

```text
Cybertron/
  Cybertron.exe
  _internal/...
```

Once that is stable, wrap it in a normal Windows installer.

## Why not Electron now?

Electron would add another Chromium runtime to an application that already has a Qt UI and browser-assisted voice components. That is unnecessary RAM/CPU overhead on an older Intel Mac.

## Why not rewrite everything in Tauri now?

Tauri is a good lightweight future shell, but switching now would require a UI rewrite and a sidecar strategy for the existing Python AI/vision/hardware code. It makes more sense after the engineering workflow and hardware APIs are stable.

## Cross-platform architecture

```text
Cybertron
├── core/              shared state, commands, events
├── providers/         cloud AI providers
├── voice/             shared conversation protocol
├── screen/            screen-awareness API
├── hardware/          future Arduino/ESP32/RPi/serial modules
├── ui/                shared Qt UI
└── platform/
    ├── macos.py       macOS-specific integration
    └── windows.py     Windows-specific integration
```

Do not fork the whole application into separate Mac and Windows projects. Keep only OS-specific behavior behind the platform layer.
