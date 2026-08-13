# Cybertron V12.1 — Voice Restore

V12.1 fixes the speech regression introduced during the V11 → V12 merge.

## Fixes

- Restores the macOS `/usr/bin/say` fallback when the browser voice bridge is offline or not fully connected.
- Restores speaking-state audio pulses for the central core.
- Resets Cybertron from `SPEAKING` to `IDLE` after local speech ends.
- Prevents later hardware connection announcements from being suppressed by a stale `SPEAKING` state.
- Keeps V12 Hardware Discovery unchanged.
- Adds no runtime dependencies.

## Test

After installing V12.1, trigger `test voice`. Cybertron should speak `Voice online.` even if the browser microphone bridge is not currently online. Then connect a USB device to verify hardware announcements continue to speak normally.
