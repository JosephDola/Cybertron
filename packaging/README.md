# Cybertron desktop builds

The preferred release format is a frozen desktop application, not a Terminal-launched Python project.

## macOS Big Sur / Intel

Run from the repository root on the Big Sur Mac:

```bash
./packaging/build_macos.sh
```

Expected output:

```text
dist/Cybertron.app
dist/Cybertron-macOS-x86_64.dmg
```

The official Big Sur-compatible build should be produced on Big Sur because third-party native binaries bundled by PyInstaller may target the macOS version they were built on.

## Windows

Run on a Windows machine:

```powershell
.\packaging\build_windows.ps1
```

Expected output:

```text
dist\Cybertron\Cybertron.exe
```

Windows packaging should be tested after the platform-specific system-control code has been separated from the shared application core.
