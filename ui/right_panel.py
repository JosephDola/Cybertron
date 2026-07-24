from datetime import datetime

from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QWidget,
    QSizePolicy,
    QGraphicsOpacityEffect,
)
from PySide2.QtCore import Qt, QPropertyAnimation, QEasingCurve

from ui.theme import Theme
from brain.events import events


MAX_ENTRIES = 50


class ActivityEntry(QLabel):
    def __init__(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        super().__init__(f"{timestamp}   {message}")
        self.setFont(Theme.SMALL)
        self.setWordWrap(True)
        self.setStyleSheet(
            f"""
            color:{Theme.TEXT_COLOR};
            padding:10px 12px;
            background:{Theme.GLASS_BG};
            border:1px solid {Theme.PANEL_BORDER};
            border-radius:10px;
            """
        )

        self._effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self._effect)
        self._effect.setOpacity(0.0)

        self._anim = QPropertyAnimation(self._effect, b"opacity", self)
        self._anim.setDuration(Theme.DUR_BASE)
        self._anim.setStartValue(0.0)
        self._anim.setEndValue(1.0)
        self._anim.setEasingCurve(QEasingCurve.OutCubic)
        self._anim.start(QPropertyAnimation.DeleteWhenStopped)


class RightPanel(QFrame):
    """
    Live activity feed. Reuses the existing events.log signal - the same
    one ai_log.py's console listens to - so anything that already logs
    shows up here too, no backend changes needed.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("glassCard")
        self.setFixedWidth(Theme.RIGHT_PANEL_WIDTH)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        outer = QVBoxLayout()
        outer.setContentsMargins(18, 18, 18, 18)
        outer.setSpacing(14)

        title_row = QVBoxLayout()
        title = QLabel("LIVE ACTIVITY")
        title.setFont(Theme.HEADER)
        title.setStyleSheet(f"color:{Theme.ACCENT}; letter-spacing: 1px;")
        title_row.addWidget(title)
        outer.addLayout(title_row)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.NoFrame)

        self.feed_container = QWidget()
        self.feed_layout = QVBoxLayout()
        self.feed_layout.setSpacing(8)
        self.feed_layout.addStretch()
        self.feed_container.setLayout(self.feed_layout)

        self.scroll.setWidget(self.feed_container)
        outer.addWidget(self.scroll)

        self.setLayout(outer)

        self.entries = []

        events.log.connect(self.add_entry)

    def add_entry(self, message):
        entry = ActivityEntry(message)
        # index 0 so newest sits at the top, above the stretch
        self.feed_layout.insertWidget(0, entry)

        self.entries.append(entry)
        if len(self.entries) > MAX_ENTRIES:
            oldest = self.entries.pop(0)
            self.feed_layout.removeWidget(oldest)
            oldest.deleteLater()
