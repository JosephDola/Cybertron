from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit
)

from PySide2.QtCore import Qt

from brain.events import events
from brain.commands import commands
from ui.theme import Theme


class AILog(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(12)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.output.setStyleSheet(
            f"""
            QTextEdit {{
                background:#050B12;
                color:{Theme.ACCENT};
                font-family:Menlo, monospace;
                font-size:12px;
                border:1px solid {Theme.PANEL_BORDER};
                border-radius:12px;
                padding:14px;
            }}
            """
        )

        self.input = QLineEdit()
        self.input.setPlaceholderText("Enter command...")
        self.input.setStyleSheet(
            f"""
            QLineEdit {{
                background:{Theme.BG_DEEPER};
                color:{Theme.TEXT_COLOR};
                padding:10px 14px;
                font-family:Menlo, monospace;
                border:1px solid {Theme.PANEL_BORDER};
                border-radius:10px;
            }}
            QLineEdit:focus {{
                border:1px solid {Theme.ACCENT};
            }}
            """
        )
        self.input.returnPressed.connect(self.process_command)

        self.layout.addWidget(self.output)
        self.layout.addWidget(self.input)

        self.setLayout(self.layout)

        events.log.connect(self.add_log)

    def add_log(self, message):
        self.output.append(message)

    def process_command(self):
        command = self.input.text()

        if not command:
            return

        self.output.append(f"<span style='color:#8FA7B5;'>&gt; {command}</span>")

        response = commands.execute(command)

        self.output.append(f"<b style='color:{Theme.ACCENT2};'>CYBERTRON:</b> {response}")

        self.input.clear()
