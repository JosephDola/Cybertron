from PySide2.QtCore import QObject, Signal


class EventBus(QObject):

    log = Signal(str)

    face_detected = Signal(float)

    face_lost = Signal()

    target_locked = Signal(int)

    camera_connected = Signal()

    camera_disconnected = Signal()

    fps_changed = Signal(int)

    mic_level = Signal(float)



events = EventBus()
