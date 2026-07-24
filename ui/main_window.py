from PySide2.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
)

from ui.theme import Theme
from ui.sidebar import Sidebar
from ui.top_bar import TopBar
from ui.bottom_bar import BottomBar
from ui.right_panel import RightPanel
from ui.dashboard_page import DashboardPage
from ui.camera_widget import CameraWidget
from ui.ai_log import AILog
from ui.placeholder_page import PlaceholderPage
from ui.particles_bg import AmbientBackground

from brain.events import events


# Sections that have a real widget behind them today. Everything else in
# the sidebar gets an honest "not connected yet" placeholder.
PLACEHOLDER_PAGES = {
    "Research": ("◎", "Pull in and summarize sources on demand."),
    "Browser": ("◍", "An embedded browser view will live here."),
    "Files": ("▤", "Browse and manage files from inside CYBER."),
    "Memory": ("◈", "Visualize what CYBER remembers over time."),
    "Skills": ("✦", "A library of tools CYBER can call on."),
    "Settings": ("⚙", "Preferences, connections, and account settings."),
}


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cybertron")
        self.resize(1600, 950)
        self.setStyleSheet(Theme.stylesheet())

        self.build_ui()

    def build_ui(self):
        root = QWidget()
        root.setObjectName("rootBackground")

        # Ambient animated background sits as the bottom-most layer,
        # stacked underneath everything else via a manual overlay so it
        # doesn't disturb the existing layout tree at all.
        self.ambient_bg = AmbientBackground(root)
        self.ambient_bg.lower()

        root_layout = QVBoxLayout()
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # ---- Top bar (full width) ----
        self.top_bar = TopBar()

        # ---- Middle row: sidebar | workspace | right panel ----
        middle = QHBoxLayout()
        middle.setContentsMargins(14, 14, 14, 14)
        middle.setSpacing(14)

        self.sidebar = Sidebar()
        middle.addWidget(self.sidebar)

        self.workspace = QStackedWidget()
        self.pages = {}
        self.build_pages()
        middle.addWidget(self.workspace, stretch=1)

        self.right_panel = RightPanel()
        middle.addWidget(self.right_panel)

        middle_widget = QWidget()
        middle_widget.setLayout(middle)

        # ---- Bottom bar (full width) ----
        self.bottom_bar = BottomBar()

        root_layout.addWidget(self.top_bar)
        root_layout.addWidget(middle_widget, stretch=1)
        root_layout.addWidget(self.bottom_bar)

        # Wrap root_layout content in a container so the ambient background
        # can sit behind it within the same root widget.
        content = QWidget()
        content.setLayout(root_layout)

        overlay_layout = QVBoxLayout()
        overlay_layout.setContentsMargins(0, 0, 0, 0)
        overlay_layout.addWidget(content)
        root.setLayout(overlay_layout)

        self.setCentralWidget(root)

        # ---- Wiring ----
        self.sidebar.page_selected.connect(self.show_page)

        # Same mic wiring as before, just pointed at the mic meter that
        # now lives inside the bottom bar instead of its own row.
        events.mic_level.connect(self.bottom_bar.mic_meter.set_level)

        # NOTE: there is exactly one HUDOverlay instance in the app - it
        # lives inside CameraWidget (see ui/camera_widget.py), which is
        # used directly as the "Vision" page below. Nothing else creates
        # a HUDOverlay.

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self, "ambient_bg"):
            self.ambient_bg.resize(self.centralWidget().size())

    def build_pages(self):
        self.pages["Dashboard"] = DashboardPage()
        self.workspace.addWidget(self.pages["Dashboard"])

        self.camera_widget = CameraWidget()
        self.pages["Vision"] = self.camera_widget
        self.workspace.addWidget(self.camera_widget)

        self.logs = AILog()
        self.pages["Coding"] = self.logs
        self.workspace.addWidget(self.logs)

        for title, (glyph, description) in PLACEHOLDER_PAGES.items():
            page = PlaceholderPage(title, glyph, description)
            self.pages[title] = page
            self.workspace.addWidget(page)

        self.workspace.setCurrentWidget(self.pages["Dashboard"])

    def show_page(self, title):
        page = self.pages.get(title)
        if page is not None:
            self.workspace.setCurrentWidget(page)
