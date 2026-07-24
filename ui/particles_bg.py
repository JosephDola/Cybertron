"""
AmbientBackground - subtle animated grid + floating particles.

New additive file. Intended to be placed as the bottom-most widget behind
the main window's content (see main_window.py), purely decorative and
cheap to render (no image assets, no heavy blur - just thin lines and
soft dots at low opacity so it never competes with real content).
"""

import random

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt, QTimer, QPointF
from PySide2.QtGui import QPainter, QColor, QPen, QRadialGradient

from ui.theme import Theme


class AmbientBackground(QWidget):

    def __init__(self, parent=None, particle_count=36):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.tick = 0

        self._particles = []
        for _ in range(particle_count):
            self._particles.append({
                "x": random.uniform(0, 1),
                "y": random.uniform(0, 1),
                "r": random.uniform(1.0, 2.6),
                "speed": random.uniform(0.00006, 0.00022),
                "phase": random.uniform(0, 6.283),
                "drift": random.uniform(-0.00012, 0.00012),
            })

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._animate)
        self.timer.start(33)  # ~30fps is plenty for ambient motion

    def _animate(self):
        self.tick += 1
        for p in self._particles:
            p["y"] -= p["speed"]
            p["x"] += p["drift"]
            if p["y"] < -0.02:
                p["y"] = 1.02
                p["x"] = random.uniform(0, 1)
            if p["x"] < -0.02:
                p["x"] = 1.02
            elif p["x"] > 1.02:
                p["x"] = -0.02
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w, h = self.width(), self.height()

        # ---- Base gradient wash (very dark, deep navy -> near black) ----
        grad_color_top = QColor(Theme.BG_DEEPER)
        painter.fillRect(self.rect(), grad_color_top)

        # ---- Faint grid ----
        grid_color = QColor(Theme.ACCENT)
        grid_color.setAlpha(10)
        pen = QPen(grid_color)
        pen.setWidth(1)
        painter.setPen(pen)

        spacing = 64
        offset = (self.tick * 0.15) % spacing

        x = -spacing + offset
        while x < w:
            painter.drawLine(int(x), 0, int(x), h)
            x += spacing

        y = -spacing + offset
        while y < h:
            painter.drawLine(0, int(y), w, int(y))
            y += spacing

        # ---- Soft radial glow anchored top-center (echoes AI Core) ----
        glow = QRadialGradient(QPointF(w * 0.5, h * 0.05), w * 0.6)
        c1 = QColor(Theme.ACCENT)
        c1.setAlpha(18)
        c2 = QColor(Theme.ACCENT)
        c2.setAlpha(0)
        glow.setColorAt(0.0, c1)
        glow.setColorAt(1.0, c2)
        painter.fillRect(self.rect(), glow)

        # ---- Floating particles ----
        for p in self._particles:
            px = p["x"] * w
            py = p["y"] * h
            twinkle = 0.5 + 0.5 * __import__("math").sin(self.tick * 0.02 + p["phase"])
            alpha = int(40 + 80 * twinkle)

            color = QColor(Theme.ACCENT)
            color.setAlpha(alpha)
            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            painter.drawEllipse(QPointF(px, py), p["r"], p["r"])

        painter.end()
