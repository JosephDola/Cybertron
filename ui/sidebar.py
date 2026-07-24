from PySide2.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QButtonGroup,
    QSizePolicy,
    QGraphicsOpacityEffect,
)
from PySide2.QtCore import Qt, Signal, QPropertyAnimation, QEasingCurve

from ui.theme import Theme


# (label, icon glyph) - plain text glyphs so this has zero image/font
# dependencies. Swap the glyphs for real icons whenever you want.
NAV_ITEMS = [
    ("Dashboard", "◧"),
    ("Research", "◎"),
    ("Browser", "◍"),
    ("Files", "▤"),
    ("Memory", "◈"),
    ("Vision", "◉"),
    ("Coding", "◫"),
    ("Skills", "✦"),
    ("Settings", "⚙"),
]


class Sidebar(QFrame):

    page_selected = Signal(str)

    def __init__(self):
        super().__init__()

        self.setObjectName("glassCard")
        self.setFixedWidth(Theme.SIDEBAR_WIDTH)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setStyleSheet(
            f"""
            QFrame#glassCard {{
                background:{Theme.BG_DEEPER};
                border:1px solid {Theme.PANEL_BORDER};
                border-radius:16px;
            }}
            """
        )

        self.buttons = {}
        self.button_group = QButtonGroup(self)
        self.button_group.setExclusive(True)

        self._fade_effects = []

        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(18, 22, 18, 20)
        layout.setSpacing(3)

        # ---- Logo ----
        logo_row = QHBoxLayout()
        logo_row.setSpacing(8)

        logo_mark = QLabel("◆")
        logo_mark.setStyleSheet(f"color:{Theme.ACCENT}; font-size:20px;")

        logo_text = QLabel("CYBER")
        logo_text.setFont(Theme.LOGO_FONT)
        logo_text.setStyleSheet(f"color:{Theme.TEXT_COLOR}; letter-spacing: 2px;")

        logo_row.addWidget(logo_mark)
        logo_row.addWidget(logo_text)
        logo_row.addStretch()

        layout.addLayout(logo_row)

        subtitle = QLabel("COMMAND CENTER")
        subtitle.setFont(Theme.SMALL)
        subtitle.setStyleSheet(f"color:{Theme.SUBTEXT}; letter-spacing: 1px;")
        layout.addWidget(subtitle)

        layout.addSpacing(26)

        # ---- Nav buttons (staggered fade-in) ----
        for i, (label, glyph) in enumerate(NAV_ITEMS):
            btn = QPushButton(f"  {glyph}   {label}")
            btn.setObjectName("navButton")
            btn.setCheckable(True)
            btn.setFont(Theme.NAV_FONT)
            btn.setCursor(Qt.PointingHandCursor)
            btn.clicked.connect(lambda checked, l=label: self.page_selected.emit(l))

            self.button_group.addButton(btn)
            self.buttons[label] = btn

            layout.addWidget(btn)
            self._stagger_fade_in(btn, delay=i * 35)

        layout.addStretch()

        self.setLayout(layout)

        # Default selection
        self.select("Dashboard")

    def _stagger_fade_in(self, widget, delay=0):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        effect.setOpacity(0.0)

        anim = QPropertyAnimation(effect, b"opacity", widget)
        anim.setDuration(Theme.DUR_BASE)
        anim.setStartValue(0.0)
        anim.setEndValue(1.0)
        anim.setEasingCurve(QEasingCurve.OutCubic)

        from PySide2.QtCore import QTimer
        QTimer.singleShot(delay, lambda: anim.start(QPropertyAnimation.DeleteWhenStopped))

        self._fade_effects.append((effect, anim))

    def select(self, label):
        if label in self.buttons:
            self.buttons[label].setChecked(True)
