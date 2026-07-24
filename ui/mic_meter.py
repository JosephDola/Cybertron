from PySide2.QtWidgets import QWidget
from PySide2.QtCore import QTimer, Qt, QRectF
from PySide2.QtGui import QPainter, QColor, QLinearGradient

from ui.theme import Theme


class MicMeter(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.level = 0
        self.target_level = 0

        self.setMinimumHeight(40)

        self.timer = QTimer()
        self.timer.timeout.connect(self.animate)
        self.timer.start(30)

    def set_level(self, value):
        self.target_level = max(0, min(100, value))

    def animate(self):
        self.level += (self.target_level - self.level) * 0.2
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        width = self.width()
        height = self.height()

        bars = 14
        gap = 3
        bar_width = (width - gap * (bars - 1)) / bars

        accent = QColor(Theme.ACCENT)
        idle_color = QColor(Theme.PANEL_BORDER)

        for i in range(bars):
            threshold = (i + 1) * (100 / bars)
            bar_height = 8 + (i * 2.2)

            x = i * (bar_width + gap)

            if self.level >= threshold:
                grad = QLinearGradient(0, height, 0, height - bar_height)
                c1 = QColor(accent)
                c1.setAlpha(230)
                c2 = QColor(Theme.ACCENT2)
                c2.setAlpha(180)
                grad.setColorAt(0.0, c1)
                grad.setColorAt(1.0, c2)
                painter.setBrush(grad)
                painter.setPen(Qt.NoPen)
            else:
                painter.setBrush(idle_color)
                painter.setPen(Qt.NoPen)

            rect = QRectF(x, height - bar_height, bar_width, bar_height)
            painter.drawRoundedRect(rect, 2, 2)

        painter.end()
