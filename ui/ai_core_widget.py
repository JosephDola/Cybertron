import math
import random
from datetime import datetime

from PySide2.QtWidgets import QWidget, QSizePolicy
from PySide2.QtCore import Qt, QTimer, QRectF, QPointF
from PySide2.QtGui import QPainter, QPen, QColor, QFont, QRadialGradient

from ui.theme import Theme


def greeting_for_now():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning."
    if hour < 18:
        return "Good afternoon."
    return "Good evening."


# Public states the orb understands. Anything calling set_state() with an
# unrecognized string falls back to "idle" rather than raising, so this
# stays safe to wire up incrementally from the backend.
STATE_IDLE = "idle"
STATE_LISTENING = "listening"
STATE_THINKING = "thinking"
STATE_SPEAKING = "speaking"

_VALID_STATES = {STATE_IDLE, STATE_LISTENING, STATE_THINKING, STATE_SPEAKING}


class AICoreWidget(QWidget):
    """
    Animated hero orb - the signature element of the CYBER dashboard.

    Backward compatible: constructor takes no args (same as before), and
    the widget is still safe to drop in anywhere with zero backend
    dependency. NEW: call set_state("listening" | "thinking" | "speaking"
    | "idle") to react to voice/AI activity if/when the backend wires it
    up - if nothing calls it, the orb just runs its calm idle animation
    forever, identical in spirit to the original.
    """

    def __init__(self):
        super().__init__()

        self.setMinimumHeight(280)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tick = 0
        self._state = STATE_IDLE
        self._energy = 0.0       # smoothed 0..1 activity level, drives glow/speed
        self._target_energy = 0.0

        self._particles = []
        for _ in range(28):
            angle = random.uniform(0, 2 * math.pi)
            self._particles.append({
                "angle": angle,
                "radius_mult": random.uniform(0.55, 1.15),
                "speed": random.uniform(0.002, 0.007) * random.choice([-1, 1]),
                "size": random.uniform(1.2, 2.6),
                "phase": random.uniform(0, 2 * math.pi),
            })

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._animate)
        self.timer.start(20)  # ~50fps for a smooth orb without hogging CPU

    # ---------------------------------------------------------------
    # Public API (new, additive)
    # ---------------------------------------------------------------
    def set_state(self, state):
        """Switch the orb's animated mood. Safe no-op for unknown states."""
        if state not in _VALID_STATES:
            state = STATE_IDLE
        self._state = state
        if state == STATE_IDLE:
            self._target_energy = 0.0
        elif state == STATE_LISTENING:
            self._target_energy = 0.55
        elif state == STATE_THINKING:
            self._target_energy = 0.8
        elif state == STATE_SPEAKING:
            self._target_energy = 1.0

    def current_state(self):
        return self._state

    # ---------------------------------------------------------------
    # Animation loop
    # ---------------------------------------------------------------
    def _animate(self):
        self.tick += 1
        self._energy += (self._target_energy - self._energy) * 0.08
        for p in self._particles:
            p["angle"] += p["speed"] * (1.0 + self._energy * 2.0)
        self.update()

    # ---------------------------------------------------------------
    # Painting
    # ---------------------------------------------------------------
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        try:
            cx = self.width() / 2
            cy = self.height() / 2 - 22
            base_radius = min(self.width(), self.height()) * 0.17
            base_radius = max(base_radius, 60)

            accent = QColor(Theme.ACCENT)
            accent2 = QColor(Theme.ACCENT2)

            speed_mult = 1.0 + self._energy * 1.6

            # ---- Outer ambient glow (radial gradient, breathes with energy) ----
            glow_radius = base_radius * (2.6 + 0.5 * self._energy)
            pulse = 0.5 + 0.5 * math.sin(self.tick * 0.02 * speed_mult)
            glow = QRadialGradient(QPointF(cx, cy), glow_radius)
            c1 = QColor(accent)
            c1.setAlpha(int(28 + 22 * pulse + 30 * self._energy))
            c2 = QColor(accent)
            c2.setAlpha(0)
            glow.setColorAt(0.0, c1)
            glow.setColorAt(1.0, c2)
            painter.setPen(Qt.NoPen)
            painter.setBrush(glow)
            painter.drawEllipse(QPointF(cx, cy), glow_radius, glow_radius)

            # ---- Rotating rings (3 rings, alternating cyan/violet tint) ----
            ring_specs = [
                (0, 0, accent, 2.0),
                (22, 1, accent, 1.0),
                (44, -1, accent2, 1.0),
            ]
            for i, (spread, direction, color, width) in enumerate(ring_specs):
                radius = base_radius + spread + (6 * self._energy if i == 0 else 0)
                local_pulse = 0.5 + 0.5 * math.sin((self.tick + i * 30) * 0.02 * speed_mult)

                pen_color = QColor(color)
                base_alpha = 70 - i * 14
                pen_color.setAlpha(int(max(20, min(255, base_alpha + 70 * local_pulse + 60 * self._energy))))

                pen = QPen(pen_color)
                pen.setWidthF(width + self._energy * 1.2)
                painter.setPen(pen)
                painter.setBrush(Qt.NoBrush)

                rect = QRectF(cx - radius, cy - radius, radius * 2, radius * 2)

                # Draw as an arc sweep to sell "rotation" rather than a
                # static ring - each ring rotates at its own rate/direction.
                rotation_deg = (self.tick * 0.6 * speed_mult * direction) % 360
                span = 300 if i == 0 else 220
                painter.drawArc(rect, int(rotation_deg * 16), int(span * 16))

                # faint full ring underneath so it doesn't look broken
                faint = QColor(color)
                faint.setAlpha(int(max(8, base_alpha * 0.25)))
                faint_pen = QPen(faint)
                faint_pen.setWidthF(1.0)
                painter.setPen(faint_pen)
                painter.drawEllipse(rect)

            # ---- Orbiting particles ----
            for p in self._particles:
                r = base_radius * p["radius_mult"] * (1.0 + 0.08 * self._energy)
                px = cx + r * math.cos(p["angle"])
                py = cy + r * math.sin(p["angle"])
                twinkle = 0.5 + 0.5 * math.sin(self.tick * 0.05 + p["phase"])
                color = QColor(accent if p["radius_mult"] < 0.9 else accent2)
                color.setAlpha(int(60 + 140 * twinkle))
                painter.setPen(Qt.NoPen)
                painter.setBrush(color)
                painter.drawEllipse(QPointF(px, py), p["size"], p["size"])

            # ---- Core wordmark ----
            painter.setPen(QColor(Theme.TEXT_COLOR))
            painter.setFont(QFont("Helvetica", 32, QFont.Bold))
            painter.drawText(
                QRectF(0, cy - 20, self.width(), 44),
                int(Qt.AlignCenter),
                "CYBER"
            )

            state_labels = {
                STATE_IDLE: "AI CORE",
                STATE_LISTENING: "LISTENING…",
                STATE_THINKING: "THINKING…",
                STATE_SPEAKING: "SPEAKING…",
            }
            painter.setPen(QColor(Theme.ACCENT))
            painter.setFont(Theme.SMALL)
            painter.drawText(
                QRectF(0, cy + 22, self.width(), 24),
                int(Qt.AlignCenter),
                state_labels.get(self._state, "AI CORE")
            )

            painter.setPen(QColor(Theme.SUBTEXT))
            painter.setFont(Theme.TEXT)
            painter.drawText(
                QRectF(0, cy + base_radius + 58, self.width(), 30),
                int(Qt.AlignCenter),
                greeting_for_now()
            )

        finally:
            painter.end()
