from PySide2.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PySide2.QtCore import Qt

from vision.camera import CameraThread

from ui.hud_overlay import HUDOverlay


class CameraWidget(QWidget):

    def __init__(self):

        super().__init__()


        self.setMinimumSize(
            400,
            300
        )


        self.camera = CameraThread()


        # Camera image

        self.image_label = QLabel()

        self.image_label.setAlignment(
            Qt.AlignCenter
        )

        self.image_label.setStyleSheet(
            """
            background:black;
            """
        )


        # Container

        self.container = QWidget()


        self.layout = QVBoxLayout(
            self.container
        )

        self.layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        self.layout.addWidget(
            self.image_label
        )


        self.setLayout(
            self.layout
        )


        # HUD overlay

        self.hud = HUDOverlay(
            self
        )

        self.hud.raise_()



        # Camera signals

        self.camera.frame_ready.connect(
            self.update_frame
        )


        self.camera.start()



    def resizeEvent(self, event):

        super().resizeEvent(
            event
        )

        self.hud.resize(
            self.size()
        )


    def update_frame(self, pixmap):

        scaled = pixmap.scaled(
            self.image_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.image_label.setPixmap(
            scaled
        )
