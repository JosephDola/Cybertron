from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
    QLabel,
)
from PySide2.QtCore import Qt

from ui.theme import Theme
from ui.ai_core_widget import AICoreWidget
from ui.system_panel import SystemPanel
from brain.events import events


class VisionStatusCard(QFrame):
    """Small real-data card: reflects actual camera/face events, no fake numbers."""

    def __init__(self):
        super().__init__()
        self.setObjectName("glassCard")

        layout = QVBoxLayout()
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(8)

        title = QLabel("VISION")
        title.setFont(Theme.HEADER)
        title.setStyleSheet(f"color:{Theme.ACCENT}; letter-spacing: 1px;")

        self.status = QLabel("Camera offline")
        self.status.setFont(Theme.TEXT)
        self.status.setStyleSheet(f"color:{Theme.SUBTEXT};")

        layout.addWidget(title)
        layout.addWidget(self.status)
        layout.addStretch()

        self.setLayout(layout)

        events.camera_connected.connect(lambda: self._set("Camera online", Theme.SUCCESS))
        events.camera_disconnected.connect(lambda: self._set("Camera offline", Theme.DANGER))
        events.face_detected.connect(lambda c: self._set(f"Target detected  {c:.0f}%", Theme.ACCENT))
        events.face_lost.connect(lambda: self._set("Searching...", Theme.SUBTEXT))
        events.target_locked.connect(lambda tid: self._set(f"Target #{tid} locked", Theme.SUCCESS))

    def _set(self, text, color):
        self.status.setText(text)
        self.status.setStyleSheet(f"color:{color};")


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(28, 28, 28, 28)
        layout.setSpacing(22)

        self.ai_core = AICoreWidget()
        layout.addWidget(self.ai_core)

        cards_row = QHBoxLayout()
        cards_row.setSpacing(18)

        cards_row.addWidget(VisionStatusCard())
        cards_row.addWidget(SystemPanel())

        layout.addLayout(cards_row)
        layout.addStretch()

        self.setLayout(layout)

        # Wire the orb's mood to real signals, if/when they fire - falls
        # back to its default idle animation if nothing ever emits.
        events.mic_level.connect(self._on_mic_level)
        events.face_detected.connect(lambda c: self.ai_core.set_state("thinking"))
        events.face_lost.connect(lambda: self.ai_core.set_state("idle"))
        events.target_locked.connect(lambda tid: self.ai_core.set_state("speaking"))

    def _on_mic_level(self, level):
        if level > 5:
            self.ai_core.set_state("listening")
        elif self.ai_core.current_state() == "listening":
            self.ai_core.set_state("idle")
