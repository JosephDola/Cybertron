from PySide2.QtGui import QFont, QColor


class Theme:

    # ---- Existing tokens - unchanged, other files depend on these ----
    BG = "#05080D"
    PANEL = "#0A1220"

    ACCENT = "#00E5FF"
    SUCCESS = "#00FF88"
    WARNING = "#FFB347"
    DANGER = "#FF5C5C"

    TEXT_COLOR = "#EAF8FF"
    SUBTEXT = "#8FA7B5"

    TITLE_FONT = QFont("Helvetica", 20, QFont.Bold)
    HEADER_FONT = QFont("Helvetica", 12, QFont.Bold)
    TEXT_FONT = QFont("Helvetica", 10)
    SMALL_FONT = QFont("Helvetica", 9)

    # Compatibility with the rest of the project
    TITLE = TITLE_FONT
    HEADER = HEADER_FONT
    TEXT = TEXT_FONT
    SMALL = SMALL_FONT

    # ---- New tokens for the CYBER dashboard redesign ----
    BG_DEEPER = "#03050A"
    PANEL_BORDER = "#173049"
    ACCENT_DIM = "#0B6B80"
    SIDEBAR_WIDTH = 240
    RIGHT_PANEL_WIDTH = 320
    BOTTOM_BAR_HEIGHT = 64

    NAV_FONT = QFont("Helvetica", 10)
    LOGO_FONT = QFont("Helvetica", 17, QFont.Bold)
    MONO_FONT = QFont("Menlo", 10)

    # ---- Secondary accent (violet) - used sparingly for agent/memory
    # signals so the whole UI doesn't read as one flat cyan wash ----
    ACCENT2 = "#7C6CFF"
    ACCENT2_DIM = "#3A2E8A"

    # ---- Glass / elevation tokens ----
    GLASS_BG = "rgba(12, 20, 32, 210)"
    GLASS_BG_HOVER = "rgba(16, 28, 44, 230)"
    GLASS_BORDER = "rgba(0, 229, 255, 45)"
    GLASS_BORDER_HOVER = "rgba(0, 229, 255, 110)"
    DIVIDER = "rgba(143, 167, 181, 35)"

    CARD_RADIUS = 16
    PILL_RADIUS = 18

    # ---- Motion tokens - shared by ui/animations.py ----
    DUR_FAST = 140
    DUR_BASE = 260
    DUR_SLOW = 420
    DUR_AMBIENT = 2200

    @staticmethod
    def qcolor(hex_or_rgba, alpha=None):
        """Helper: turn a hex string into QColor, optionally overriding alpha (0-255)."""
        c = QColor(hex_or_rgba)
        if alpha is not None:
            c.setAlpha(alpha)
        return c

    @staticmethod
    def stylesheet():
        return f"""
        QMainWindow {{
            background:{Theme.BG};
        }}

        QWidget {{
            background:transparent;
            color:{Theme.TEXT_COLOR};
            font-family:Helvetica;
            font-size:10pt;
        }}

        QMainWindow, #rootBackground {{
            background:{Theme.BG};
        }}

        QFrame {{
            background:{Theme.PANEL};
            border-radius:{Theme.CARD_RADIUS}px;
        }}

        QLabel {{
            background:transparent;
            color:{Theme.TEXT_COLOR};
        }}

        QTextEdit {{
            background:#08111B;
            color:{Theme.TEXT_COLOR};
            border:1px solid {Theme.PANEL_BORDER};
            border-radius:12px;
            padding:10px;
            selection-background-color:{Theme.ACCENT_DIM};
        }}

        QLineEdit {{
            background:#0C1622;
            color:{Theme.TEXT_COLOR};
            border:1px solid {Theme.PANEL_BORDER};
            border-radius:10px;
            padding:8px 12px;
        }}

        QLineEdit:focus {{
            border:1px solid {Theme.ACCENT};
        }}

        QProgressBar {{
            border:none;
            background:#0E1A26;
            border-radius:5px;
            text-align:center;
            height:10px;
            color:{Theme.TEXT_COLOR};
        }}

        QProgressBar::chunk {{
            background:{Theme.ACCENT};
            border-radius:5px;
        }}

        QScrollArea {{
            border:none;
            background:transparent;
        }}

        QScrollBar:vertical {{
            border:none;
            background:transparent;
            width:8px;
            margin:2px;
        }}

        QScrollBar::handle:vertical {{
            background:{Theme.ACCENT_DIM};
            border-radius:4px;
            min-height:24px;
        }}

        QScrollBar::handle:vertical:hover {{
            background:{Theme.ACCENT};
        }}

        QScrollBar::add-line:vertical,
        QScrollBar::sub-line:vertical {{
            height:0px;
        }}

        QScrollBar:horizontal {{
            border:none;
            background:transparent;
            height:8px;
        }}

        QScrollBar::handle:horizontal {{
            background:{Theme.ACCENT_DIM};
            border-radius:4px;
        }}

        QPushButton#navButton {{
            background:transparent;
            color:{Theme.SUBTEXT};
            text-align:left;
            padding:11px 14px;
            border-radius:10px;
            border:none;
            font-size:10pt;
        }}

        QPushButton#navButton:hover {{
            background:rgba(0, 229, 255, 18);
            color:{Theme.TEXT_COLOR};
        }}

        QPushButton#navButton:checked {{
            background:rgba(0, 229, 255, 28);
            color:{Theme.ACCENT};
            border-left: 3px solid {Theme.ACCENT};
        }}

        QPushButton#pillButton {{
            background:rgba(0, 229, 255, 16);
            color:{Theme.ACCENT};
            border:1px solid {Theme.GLASS_BORDER};
            border-radius:{Theme.PILL_RADIUS}px;
            padding:8px 16px;
            font-weight:600;
        }}

        QPushButton#pillButton:hover {{
            background:rgba(0, 229, 255, 30);
            border:1px solid {Theme.ACCENT};
        }}

        QPushButton#pillButton:pressed {{
            background:rgba(0, 229, 255, 45);
        }}

        QPushButton#ghostButton {{
            background:transparent;
            color:{Theme.SUBTEXT};
            border:1px solid {Theme.PANEL_BORDER};
            border-radius:10px;
            padding:7px 12px;
        }}

        QPushButton#ghostButton:hover {{
            color:{Theme.TEXT_COLOR};
            border:1px solid {Theme.ACCENT_DIM};
            background:rgba(0, 229, 255, 10);
        }}

        QFrame#glassCard {{
            background:{Theme.GLASS_BG};
            border:1px solid {Theme.GLASS_BORDER};
            border-radius:{Theme.CARD_RADIUS}px;
        }}

        QFrame#glassCardHover {{
            background:{Theme.GLASS_BG_HOVER};
            border:1px solid {Theme.GLASS_BORDER_HOVER};
            border-radius:{Theme.CARD_RADIUS}px;
        }}

        QFrame#divider {{
            background:{Theme.DIVIDER};
            border-radius:1px;
        }}
        """
