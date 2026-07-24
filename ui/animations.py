"""
Shared animation helpers for the CYBER UI.

This module is additive - it doesn't replace or rename anything in the
existing project. Every widget file can import from here to avoid
re-implementing the same fade/slide/pulse logic.

All builders return QPropertyAnimation / QAbstractAnimation instances that
the CALLER owns (keep a reference on `self`, otherwise Qt/PySide may garbage
collect the animation mid-flight and it will silently stop).
"""

from PySide2.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
    QSequentialAnimationGroup,
    QParallelAnimationGroup,
    QPoint,
    QRect,
)
from PySide2.QtWidgets import QGraphicsOpacityEffect

from ui.theme import Theme


def fade_in(widget, duration=Theme.DUR_BASE, on_finished=None):
    """Fade a widget from transparent to opaque. Returns (effect, animation).
    Caller must keep both alive (e.g. self._fade_effect, self._fade_anim)."""
    effect = QGraphicsOpacityEffect(widget)
    widget.setGraphicsEffect(effect)
    effect.setOpacity(0.0)

    anim = QPropertyAnimation(effect, b"opacity")
    anim.setDuration(duration)
    anim.setStartValue(0.0)
    anim.setEndValue(1.0)
    anim.setEasingCurve(QEasingCurve.OutCubic)
    if on_finished:
        anim.finished.connect(on_finished)
    anim.start(QPropertyAnimation.DeleteWhenStopped)
    return effect, anim


def fade_out(widget, duration=Theme.DUR_BASE, on_finished=None):
    effect = widget.graphicsEffect()
    if effect is None or not isinstance(effect, QGraphicsOpacityEffect):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        effect.setOpacity(1.0)

    anim = QPropertyAnimation(effect, b"opacity")
    anim.setDuration(duration)
    anim.setStartValue(effect.opacity())
    anim.setEndValue(0.0)
    anim.setEasingCurve(QEasingCurve.InCubic)
    if on_finished:
        anim.finished.connect(on_finished)
    anim.start(QPropertyAnimation.DeleteWhenStopped)
    return effect, anim


def slide_in(widget, start_offset=QPoint(24, 0), duration=Theme.DUR_SLOW, easing=QEasingCurve.OutCubic):
    """Slide a widget into its current `pos()` from an offset position.
    Widget must already be positioned/laid out (use with fixed-geometry
    widgets, e.g. inside a manually-positioned overlay, or call after show())."""
    end_pos = widget.pos()
    start_pos = end_pos + start_offset

    anim = QPropertyAnimation(widget, b"pos")
    anim.setDuration(duration)
    anim.setStartValue(start_pos)
    anim.setEndValue(end_pos)
    anim.setEasingCurve(easing)
    anim.start(QPropertyAnimation.DeleteWhenStopped)
    return anim


def animate_geometry(widget, end_rect, duration=Theme.DUR_BASE, easing=QEasingCurve.OutCubic, on_finished=None):
    """Animate a widget's geometry (position + size) to end_rect."""
    anim = QPropertyAnimation(widget, b"geometry")
    anim.setDuration(duration)
    anim.setStartValue(widget.geometry())
    anim.setEndValue(end_rect)
    anim.setEasingCurve(easing)
    if on_finished:
        anim.finished.connect(on_finished)
    anim.start(QPropertyAnimation.DeleteWhenStopped)
    return anim


def animate_max_width(widget, start, end, duration=Theme.DUR_SLOW, easing=QEasingCurve.InOutCubic, on_finished=None):
    """Used for the sidebar collapse/expand slide."""
    anim = QPropertyAnimation(widget, b"maximumWidth")
    anim.setDuration(duration)
    anim.setStartValue(start)
    anim.setEndValue(end)
    anim.setEasingCurve(easing)
    if on_finished:
        anim.finished.connect(on_finished)
    anim.start(QPropertyAnimation.DeleteWhenStopped)
    return anim


class HoverLift:
    """
    Attach hover-lift + glow behavior to any QFrame/QWidget by installing
    an event filter. Usage:

        self._hover = HoverLift(self.card, lift=6)

    Keep a reference (self._hover) so it isn't garbage collected.
    """

    def __init__(self, widget, lift=4, duration=Theme.DUR_FAST):
        self.widget = widget
        self.lift = lift
        self.duration = duration
        self._base_pos = None
        widget.installEventFilter(self)

    def eventFilter(self, obj, event):
        from PySide2.QtCore import QEvent
        if obj is self.widget:
            if event.type() == QEvent.Enter:
                self._animate(-self.lift)
            elif event.type() == QEvent.Leave:
                self._animate(0)
        return False

    def _animate(self, dy):
        if self._base_pos is None:
            self._base_pos = self.widget.pos()

        target = QPoint(self._base_pos.x(), self._base_pos.y() + dy)
        anim = QPropertyAnimation(self.widget, b"pos", self.widget)
        anim.setDuration(self.duration)
        anim.setStartValue(self.widget.pos())
        anim.setEndValue(target)
        anim.setEasingCurve(QEasingCurve.OutCubic)
        anim.start(QPropertyAnimation.DeleteWhenStopped)
        self._anim = anim
