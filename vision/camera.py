import time
import cv2

from PySide2.QtCore import (
    QThread,
    Signal
)

from PySide2.QtGui import (
    QImage,
    QPixmap
)

from vision.detector import VisionDetector

from brain.events import events
from brain.state import state


class CameraThread(QThread):

    frame_ready = Signal(QPixmap)

    fps_ready = Signal(int)

    resolution_ready = Signal(str)


    def __init__(self):

        super().__init__()

        self.running = True

        self.detector = VisionDetector()


        self.last_face = False

        self.last_lock = False

        self.lock_time = None

        self.target_id = 1


        self.missed_frames = 0

        self.max_missed_frames = 15



    def run(self):

        camera = cv2.VideoCapture(0)


        camera.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            1280
        )

        camera.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            720
        )


        if not camera.isOpened():

            state.set_mode(
                "CAMERA ERROR"
            )

            events.log.emit(
                "Camera failed."
            )

            events.camera_disconnected.emit()

            return



        state.camera_online = True

        state.set_mode(
            "SEARCHING"
        )


        events.camera_connected.emit()

        events.log.emit(
            "Camera connected."
        )

        events.log.emit(
            "Searching for targets..."
        )



        width = int(
            camera.get(
                cv2.CAP_PROP_FRAME_WIDTH
            )
        )

        height = int(
            camera.get(
                cv2.CAP_PROP_FRAME_HEIGHT
            )
        )


        resolution = (
            f"{width} x {height}"
        )


        state.camera_resolution = resolution


        self.resolution_ready.emit(
            resolution
        )



        frames = 0

        last_time = time.time()



        while self.running:


            success, frame = camera.read()


            if not success:
                continue



            frame, info = self.detector.process(
                frame
            )


            face_found = info["face"]

            confidence = info["confidence"]



            # ------------------------
            # TARGET POSITION
            # ------------------------

            if face_found:


                self.missed_frames = 0


                if info["center"]:


                    state.update_target_position(
                        info["center"][0],
                        info["center"][1]
                    )



                state.face_visible = True

                state.confidence = confidence



                if state.mode == "SEARCHING":

                    state.set_mode(
                        "TARGET FOUND"
                    )

                    events.log.emit(
                        "Target found."
                    )



                elif state.mode == "TARGET FOUND":

                    state.set_mode(
                        "TRACKING"
                    )

                    events.log.emit(
                        "Tracking target."
                    )



            else:


                self.missed_frames += 1



                if self.missed_frames > self.max_missed_frames:


                    state.face_visible = False

                    state.target_locked = False

                    state.set_mode(
                        "SEARCHING"
                    )



            # ------------------------
            # EVENTS
            # ------------------------


            if face_found and not self.last_face:


                self.last_face = True


                events.face_detected.emit(
                    confidence
                )


                events.log.emit(
                    f"Confidence {confidence:.0f}%"
                )


                self.lock_time = time.time()



            elif (
                not face_found
                and self.last_face
                and self.missed_frames > self.max_missed_frames
            ):


                self.last_face = False

                self.last_lock = False


                events.face_lost.emit()


                events.log.emit(
                    "Target lost."
                )



            # ------------------------
            # LOCK
            # ------------------------


            if (
                face_found
                and self.lock_time
                and not self.last_lock
            ):


                if time.time() - self.lock_time > 0.5:


                    self.last_lock = True


                    state.target_locked = True

                    state.target_id = self.target_id


                    state.set_mode(
                        "LOCKED"
                    )


                    events.target_locked.emit(
                        self.target_id
                    )


                    events.log.emit(
                        f"Target #{self.target_id} locked."
                    )



            # ------------------------
            # FRAME OUTPUT
            # ------------------------


            rgb = cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )


            h,w,ch = rgb.shape


            image = QImage(
                rgb.data,
                w,
                h,
                ch*w,
                QImage.Format_RGB888
            )


            self.frame_ready.emit(
                QPixmap.fromImage(image)
            )



            # ------------------------
            # FPS
            # ------------------------


            frames += 1


            if time.time() - last_time >= 1:


                fps = frames

                frames = 0

                last_time = time.time()


                state.camera_fps = fps


                self.fps_ready.emit(
                    fps
                )


                events.fps_changed.emit(
                    fps
                )



        camera.release()


        state.camera_online = False

        state.set_mode(
            "OFFLINE"
        )


        events.camera_disconnected.emit()



    def stop(self):

        self.running = False

        self.wait()
