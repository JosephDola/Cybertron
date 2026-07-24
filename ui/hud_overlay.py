from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt, QTimer, QRectF
from PySide2.QtGui import QPainter, QColor, QPen, QFont

from ui.theme import Theme


class HUDOverlay(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.fps = 0
        self.status = "VISION ONLINE"

        self._scan_pos = 0.0
        self._tick = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._animate)
        self.timer.start(20)

    def set_fps(self, fps):
        self.fps = fps
        self.update()

    def set_status(self, status):
        self.status = status
        self.update()

    def _animate(self):
        self._tick += 1
        self._scan_pos = (self._scan_pos + 0.006) % 1.0
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        accent = QColor(Theme.ACCENT)
        margin = 14
        w, h = self.width(), self.height()

        # ---- corner brackets instead of a plain rectangle ----
        bracket_len = 26
        pen = QPen(accent)
        pen.setWidth(2)
        painter.setPen(pen)

        corners = [
            (margin, margin, 1, 1),
            (w - margin, margin, -1, 1),
            (margin, h - margin, 1, -1),
            (w - margin, h - margin, -1, -1),
        ]
        for x, y, dx, dy in corners:
            painter.drawLine(x, y, x + dx * bracket_len, y)
            painter.drawLine(x, y, x, y + dy * bracket_len)

        # ---- faint full frame ----
        faint = QColor(accent)
        faint.setAlpha(40)
        faint_pen = QPen(faint)
        faint_pen.setWidth(1)
        painter.setPen(faint_pen)
        painter.drawRect(margin, margin, w - margin * 2, h - margin * 2)

        # ---- scanning sweep line ----
        scan_y = margin + self._scan_pos * (h - margin * 2)
        scan_color = QColor(accent)
        scan_color.setAlpha(160)
        scan_pen = QPen(scan_color)
        scan_pen.setWidth(2)
        painter.setPen(scan_pen)
        painter.drawLine(margin, int(scan_y), w - margin, int(scan_y))

        # ---- text ----
        font = QFont("Helvetica", 10, QFont.Bold)
        painter.setFont(font)
        painter.setPen(accent)
        painter.drawText(margin + 12, margin + 24, "CYBER VISION")

        status_color = QColor(Theme.SUCCESS) if "ONLINE" in self.status.upper() else QColor(Theme.SUBTEXT)
        painter.setPen(status_color)
        painter.drawText(margin + 12, margin + 44, self.status)

        painter.setPen(accent)
        painter.drawText(QRectF(w - margin - 110, margin + 10, 100, 20), int(Qt.AlignRight), f"FPS: {self.fps}")

        painter.end()
