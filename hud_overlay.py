from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPainter, QColor, QPen, QFont


class HUDOverlay(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.setAttribute(Qt.WA_TranslucentBackground)

        self.fps = 0
        self.status = "VISION ONLINE"



    def set_fps(self, fps):

        self.fps = fps

        self.update()



    def set_status(self, status):

        self.status = status

        self.update()



    def paintEvent(self, event):

        painter = QPainter(self)

        painter.setRenderHint(QPainter.Antialiasing)



        pen = QPen(QColor(0, 255, 255))

        pen.setWidth(2)

        painter.setPen(pen)



        margin = 10



        painter.drawRect(

            margin,

            margin,

            self.width() - margin * 2,

            self.height() - margin * 2

        )



        font = QFont()

        font.setPointSize(10)

        font.setBold(True)

        painter.setFont(font)



        painter.drawText(

            20,

            30,

            "CYBER VISION"

        )



        painter.drawText(

            20,

            50,

            self.status

        )



        painter.drawText(

            self.width() - 120,

            30,

            f"FPS: {self.fps}"

        )
