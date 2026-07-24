import time


class CybertronState:

    def __init__(self):

        # Camera

        self.camera_online = False
        self.camera_resolution = "Unknown"
        self.camera_fps = 0


        # Vision

        self.face_visible = False
        self.confidence = 0


        # Target

        self.target_id = None
        self.target_locked = False


        # Scanner state

        self.mode = "SEARCHING"


        # Position

        self.target_x = 0
        self.target_y = 0

        self.smooth_x = 0
        self.smooth_y = 0


        # Memory

        self.last_seen = 0
        self.tracking = False


        # System

        self.cpu = 0
        self.ram = 0



    def set_mode(
        self,
        mode
    ):

        self.mode = mode



    def update_target_position(
        self,
        x,
        y
    ):

        self.target_x = x
        self.target_y = y


        self.last_seen = time.time()

        self.tracking = True


        if self.smooth_x == 0:

            self.smooth_x = x


        if self.smooth_y == 0:

            self.smooth_y = y



        self.smooth_x += (
            x -
            self.smooth_x
        ) * 0.15


        self.smooth_y += (
            y -
            self.smooth_y
        ) * 0.15



    def target_active(self):

        return (
            time.time()
            -
            self.last_seen
        ) < 1.0



state = CybertronState()
