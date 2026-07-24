"""
GlassCard - a reusable glassmorphism panel used throughout the redesign.

This is a NEW file (additive). Existing widgets that used a plain QFrame
with objectName("glassCard") continue to work unmodified since the
stylesheet selector (#glassCard) is preserved in theme.py - but new/rebuilt
widgets can subclass GlassCard directly for hover-lift + glow behavior
without repeating boilerplate.
"""

from PySide2.QtWidgets import QFrame, QGraphicsDropShadowEffect
from PySide2.QtCore import Qt, QEvent, QPropertyAnimation, QEasingCurve
from PySide2.QtGui import QColor

from ui.theme import Theme


class GlassCard(QFrame):
    """
    A glass-panel QFrame with:
      - soft drop shadow (glow) that intensifies on hover
      - optional subtle lift-on-hover
      - objectName("glassCard") so it still matches the existing QSS rule
    """

    def __init__(self, parent=None, glow_color=None, hoverable=True):
        super().__init__(parent)
        self.setObjectName("glassCard")
        self._hoverable = hoverable
        self._glow_color = glow_color or Theme.ACCENT

        self._shadow = QGraphicsDropShadowEffect(self)
        self._shadow.setBlurRadius(24)
        self._shadow.setOffset(0, 6)
        self._shadow.setColor(QColor(0, 0, 0, 160))
        self.setGraphicsEffect(self._shadow)

        if hoverable:
            self.setAttribute(Qt.WA_Hover, True)
            self.setMouseTracking(True)

        self._glow_anim = None

    def eventFilter(self, obj, event):
        return super().eventFilter(obj, event)

    def enterEvent(self, event):
        if self._hoverable:
            self.setObjectName("glassCardHover")
            self.style().unpolish(self)
            self.style().polish(self)
            self._animate_glow(36, QColor(self._glow_color).lighter(110))
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self._hoverable:
            self.setObjectName("glassCard")
            self.style().unpolish(self)
            self.style().polish(self)
            self._animate_glow(24, QColor(0, 0, 0, 160))
        super().leaveEvent(event)

    def _animate_glow(self, blur, color):
        anim = QPropertyAnimation(self._shadow, b"blurRadius", self)
        anim.setDuration(Theme.DUR_FAST)
        anim.setStartValue(self._shadow.blurRadius())
        anim.setEndValue(blur)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start(QPropertyAnimation.DeleteWhenStopped)
        self._shadow.setColor(color)
        self._glow_anim = anim
