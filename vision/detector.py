import cv2
import os


class VisionDetector:

    def __init__(self):

        folder = os.path.dirname(__file__)

        proto = os.path.join(
            folder,
            "deploy.prototxt"
        )

        model = os.path.join(
            folder,
            "res10_300x300_ssd_iter_140000.caffemodel"
        )

        self.net = cv2.dnn.readNetFromCaffe(
            proto,
            model
        )

        self.confidence_threshold = 0.60

        self.target_id = 1

        self.scan_offset = 0


    def process(self, frame):

        h, w = frame.shape[:2]

        info = {
            "face": False,
            "confidence": 0,
            "count": 0,
            "center": None,
            "bbox": None,
            "id": None
        }


        blob = cv2.dnn.blobFromImage(
            cv2.resize(frame, (300,300)),
            1.0,
            (300,300),
            (104,177,123)
        )


        self.net.setInput(blob)

        detections = self.net.forward()


        best = 0
        box = None


        for i in range(detections.shape[2]):

            confidence = float(
                detections[0,0,i,2]
            )


            if confidence < self.confidence_threshold:
                continue


            if confidence > best:

                best = confidence

                box = detections[0,0,i,3:7] * [
                    w,
                    h,
                    w,
                    h
                ]


        if box is None:

            return frame, info


        startX,startY,endX,endY = box.astype(int)


        startX=max(0,startX)
        startY=max(0,startY)
        endX=min(w,endX)
        endY=min(h,endY)



        centerX = (startX+endX)//2
        centerY = (startY+endY)//2


        info["face"] = True
        info["confidence"] = best*100
        info["count"] = 1
        info["center"] = (
            centerX,
            centerY
        )
        info["bbox"] = (
            startX,
            startY,
            endX,
            endY
        )
        info["id"] = self.target_id



        # -------------------------
        # CYBERTRON HUD
        # -------------------------


        color = (
            0,
            229,
            255
        )


        length = 35


        thickness = 2



        # corners

        cv2.line(
            frame,
            (startX,startY),
            (startX+length,startY),
            color,
            thickness
        )

        cv2.line(
            frame,
            (startX,startY),
            (startX,startY+length),
            color,
            thickness
        )


        cv2.line(
            frame,
            (endX,startY),
            (endX-length,startY),
            color,
            thickness
        )

        cv2.line(
            frame,
            (endX,startY),
            (endX,startY+length),
            color,
            thickness
        )


        cv2.line(
            frame,
            (startX,endY),
            (startX+length,endY),
            color,
            thickness
        )

        cv2.line(
            frame,
            (startX,endY),
            (startX,endY-length),
            color,
            thickness
        )


        cv2.line(
            frame,
            (endX,endY),
            (endX-length,endY),
            color,
            thickness
        )

        cv2.line(
            frame,
            (endX,endY),
            (endX,endY-length),
            color,
            thickness
        )



        # center target

        cv2.circle(
            frame,
            (centerX,centerY),
            5,
            (0,255,120),
            -1
        )


        # info panel

        cv2.putText(
            frame,
            f"TARGET #{self.target_id}",
            (startX,startY-35),
            cv2.FONT_HERSHEY_SIMPLEX,
            .65,
            color,
            2
        )


        cv2.putText(
            frame,
            f"CONF {best*100:.0f}%",
            (startX,startY-12),
            cv2.FONT_HERSHEY_SIMPLEX,
            .55,
            color,
            2
        )


        return frame, info
