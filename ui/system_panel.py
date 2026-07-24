from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QProgressBar,
    QSizePolicy
)

from PySide2.QtCore import QTimer

import psutil

from ui.theme import Theme


class SystemPanel(QFrame):

    def __init__(self):
        super().__init__()

        self.setObjectName("glassCard")
        self.setMinimumWidth(150)
        self.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding
        )

        self.build_ui()

        self.start_monitor()

    def build_ui(self):

        layout = QVBoxLayout()
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        title = QLabel("SYSTEM")
        title.setFont(Theme.HEADER)
        title.setStyleSheet(f"color:{Theme.ACCENT}; letter-spacing: 1px;")
        layout.addWidget(title)

        # ---------- CPU ----------

        self.cpu_title = QLabel("CPU")
        self.cpu_title.setFont(Theme.TEXT)
        self.cpu_title.setStyleSheet(f"color:{Theme.SUBTEXT};")

        self.cpu = QProgressBar()
        self.cpu.setRange(0, 100)
        self.cpu.setTextVisible(True)

        layout.addWidget(self.cpu_title)
        layout.addWidget(self.cpu)

        # ---------- RAM ----------

        self.ram_title = QLabel("RAM")
        self.ram_title.setFont(Theme.TEXT)
        self.ram_title.setStyleSheet(f"color:{Theme.SUBTEXT};")

        self.ram = QProgressBar()
        self.ram.setRange(0, 100)
        self.ram.setTextVisible(True)

        layout.addWidget(self.ram_title)
        layout.addWidget(self.ram)

        # ---------- DISK ----------

        self.disk_title = QLabel("DISK")
        self.disk_title.setFont(Theme.TEXT)
        self.disk_title.setStyleSheet(f"color:{Theme.SUBTEXT};")

        self.disk = QProgressBar()
        self.disk.setRange(0, 100)
        self.disk.setTextVisible(True)

        layout.addWidget(self.disk_title)
        layout.addWidget(self.disk)

        # ---------- NETWORK ----------

        self.net = QLabel("NETWORK: ONLINE")
        self.net.setFont(Theme.SMALL)
        self.net.setStyleSheet(f"color:{Theme.SUCCESS};")

        layout.addSpacing(16)
        layout.addWidget(self.net)

        layout.addStretch()

        self.setLayout(layout)

    def start_monitor(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(500)

    def update_stats(self):
        cpu = int(psutil.cpu_percent())
        ram = int(psutil.virtual_memory().percent)
        disk = int(psutil.disk_usage("/").percent)

        self.cpu.setValue(cpu)
        self.cpu.setFormat(f"{cpu}%")

        self.ram.setValue(ram)
        self.ram.setFormat(f"{ram}%")

        self.disk.setValue(disk)
        self.disk.setFormat(f"{disk}%")
