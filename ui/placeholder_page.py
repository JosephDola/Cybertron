from PySide2.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide2.QtCore import Qt

from ui.theme import Theme


class PlaceholderPage(QFrame):
    """
    Generic 'coming soon' page for any sidebar section that doesn't have
    a real backend wired up yet. Swap this out for the real widget later -
    the sidebar/stacked-page wiring in main_window.py doesn't need to
    change when you do.
    """

    def __init__(self, title, glyph, description):
        super().__init__()

        self.setObjectName("glassCard")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(12)

        icon = QLabel(glyph)
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet(f"color:{Theme.ACCENT}; font-size:44px;")

        heading = QLabel(title)
        heading.setAlignment(Qt.AlignCenter)
        heading.setFont(Theme.TITLE)

        sub = QLabel(description)
        sub.setAlignment(Qt.AlignCenter)
        sub.setFont(Theme.TEXT)
        sub.setStyleSheet(f"color:{Theme.SUBTEXT};")
        sub.setWordWrap(True)
        sub.setMaximumWidth(420)

        tag = QLabel("NOT CONNECTED YET")
        tag.setAlignment(Qt.AlignCenter)
        tag.setFont(Theme.SMALL)
        tag.setStyleSheet(
            f"""
            color:{Theme.WARNING};
            letter-spacing: 2px;
            background: rgba(255, 179, 71, 20);
            border: 1px solid {Theme.WARNING};
            border-radius: 10px;
            padding: 6px 14px;
            """
        )

        layout.addWidget(icon)
        layout.addWidget(heading)
        layout.addWidget(sub)
        layout.addSpacing(8)
        layout.addWidget(tag, 0, Qt.AlignCenter)

        self.setLayout(layout)
