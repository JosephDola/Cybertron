import psutil

from PySide2.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
)
from PySide2.QtCore import QTimer

from ui.theme import Theme
from ui.mic_meter import MicMeter
from brain.events import events


class StatItem(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setFont(Theme.SMALL)
        self.setStyleSheet(f"color:{Theme.SUBTEXT};")


class BottomBar(QFrame):
    """
    Slim status strip. Camera/mic status comes from the real event bus.
    CPU/battery come from psutil (real). Location/weather are placeholders
    on purpose - no backend for those exists yet.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("glassCard")
        self.setFixedHeight(Theme.BOTTOM_BAR_HEIGHT)
        self.setStyleSheet(
            f"""
            QFrame#glassCard {{
                background:{Theme.BG_DEEPER};
                border:1px solid {Theme.PANEL_BORDER};
                border-radius:16px;
            }}
            """
        )
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout = QHBoxLayout()
        layout.setContentsMargins(22, 8, 22, 8)
        layout.setSpacing(24)

        self.location = StatItem("📍 Location: --")
        self.network = StatItem("Network: checking...")
        self.battery = StatItem("Battery: --")
        self.camera_status = StatItem("Camera: offline")

        layout.addWidget(self.location)
        layout.addWidget(self.network)
        layout.addWidget(self.battery)
        layout.addWidget(self.camera_status)

        layout.addStretch()

        # Reuse the existing mic meter widget as-is - no duplication
        self.mic_meter = MicMeter()
        self.mic_meter.setFixedWidth(180)
        layout.addWidget(self.mic_meter)

        layout.addStretch()

        self.mic_label = StatItem("Mic: idle")
        layout.addWidget(self.mic_label)

        self.setLayout(layout)

        events.camera_connected.connect(lambda: self.camera_status.setText("Camera: online"))
        events.camera_disconnected.connect(lambda: self.camera_status.setText("Camera: offline"))
        events.mic_level.connect(self._on_mic_level)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(2000)
        self.update_stats()

    def _on_mic_level(self, level):
        self.mic_label.setText("Mic: listening" if level > 5 else "Mic: idle")

    def update_stats(self):
        try:
            battery = psutil.sensors_battery()
            if battery is not None:
                plug = " (plugged in)" if battery.power_plugged else ""
                self.battery.setText(f"Battery: {int(battery.percent)}%{plug}")
            else:
                self.battery.setText("Battery: N/A")
        except Exception:
            self.battery.setText("Battery: N/A")

        try:
            stats = psutil.net_if_stats()
            up = any(s.isup for s in stats.values())
            self.network.setText("Network: online" if up else "Network: offline")
        except Exception:
            self.network.setText("Network: unknown")
