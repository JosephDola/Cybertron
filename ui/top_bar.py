from PySide2.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QGraphicsDropShadowEffect,
)
from PySide2.QtCore import Qt, QTimer, QTime, QPropertyAnimation, QEasingCurve
from PySide2.QtGui import QColor

from ui.theme import Theme
from brain.events import events


class TopBar(QFrame):

    def __init__(self):

        super().__init__()

        self.setObjectName("glassCard")
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Fixed
        )
        self.setFixedHeight(68)

        self.status_state = "SEARCHING"

        self.build_ui()

        self.connect_events()

        self.start_clock()

        self._pulse_timer = QTimer(self)
        self._pulse_timer.timeout.connect(self._pulse_dot)
        self._pulse_timer.start(45)
        self._pulse_phase = 0.0

    def build_ui(self):

        layout = QHBoxLayout()

        layout.setContentsMargins(22, 12, 22, 12)
        layout.setSpacing(20)

        # ---------------- STATUS PILL ----------------

        self.status = QLabel("● SEARCHING...")
        self.status.setFont(Theme.SMALL)
        self.status.setObjectName("statusPill")
        self.set_searching()

        layout.addWidget(self.status)

        layout.addStretch()

        # ---------------- CLOCK ----------------

        self.clock = QLabel("--:--:--")
        self.clock.setFont(Theme.HEADER)
        self.clock.setStyleSheet(f"color:{Theme.ACCENT};")
        layout.addWidget(self.clock)

        layout.addSpacing(20)

        # ---------------- VERSION ----------------

        self.version = QLabel("CORE v0.4")
        self.version.setFont(Theme.SMALL)
        self.version.setStyleSheet(f"color:{Theme.SUBTEXT};")
        layout.addWidget(self.version)

        self.setLayout(layout)

    def start_clock(self):
        self.clock_timer = QTimer()
        self.clock_timer.timeout.connect(self.update_clock)
        self.clock_timer.start(1000)
        self.update_clock()

    def update_clock(self):
        self.clock.setText(QTime.currentTime().toString("hh:mm:ss"))

    def connect_events(self):

        events.camera_connected.connect(
            self.camera_online
        )

        events.camera_disconnected.connect(
            self.camera_offline
        )

        events.face_detected.connect(
            self.face_found
        )

        events.target_locked.connect(
            self.locked
        )

        events.face_lost.connect(
            self.searching
        )

    # ---------------- STATES (unchanged behavior, restyled) ----------------

    def _apply_pill_style(self, color_hex):
        self.status.setStyleSheet(
            f"""
            QLabel#statusPill {{
                color:{color_hex};
                background: rgba(0,0,0,40);
                border: 1px solid {color_hex};
                border-radius: 10px;
                padding: 6px 12px;
            }}
            """
        )

    def set_searching(self):
        self.status.setText("● SEARCHING...")
        self._apply_pill_style(Theme.SUBTEXT)

    def camera_online(self):
        self.status.setText("● CAMERA ONLINE")
        self._apply_pill_style(Theme.SUCCESS)

    def camera_offline(self):
        self.status.setText("● CAMERA OFFLINE")
        self._apply_pill_style(Theme.DANGER)

    def face_found(self, confidence):
        self.status.setText(f"● TARGET DETECTED  {confidence:.0f}%")
        self._apply_pill_style(Theme.ACCENT)

    def locked(self, target_id):
        self.status.setText(f"● TARGET #{target_id} LOCKED")
        self._apply_pill_style(Theme.SUCCESS)

    def searching(self):
        self.set_searching()

    def _pulse_dot(self):
        # Subtle opacity pulse on the whole pill to suggest "live" status,
        # without touching layout/geometry (cheap to repaint).
        import math
        self._pulse_phase += 0.05
        pulse = 0.75 + 0.25 * math.sin(self._pulse_phase)
        effect = self.status.graphicsEffect()
        if effect is None:
            from PySide2.QtWidgets import QGraphicsOpacityEffect
            effect = QGraphicsOpacityEffect(self.status)
            self.status.setGraphicsEffect(effect)
        effect.setOpacity(pulse)
