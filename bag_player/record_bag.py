"""Open Orbbec camera, display Color + Depth, and record to a .bag file on demand.

Controls:
    R - Start recording to a .bag file
    S - Stop recording
    Q / ESC - Quit
"""

import sys
from datetime import datetime

import cv2
import numpy as np
from pyorbbecsdk import Pipeline, Config, OBSensorType

from utils import frame_to_bgr_image

ESC_KEY = 27
WINDOW_NAME = "Orbbec Viewer"


def render_depth(depth_frame) -> np.ndarray | None:
    width = depth_frame.get_width()
    height = depth_frame.get_height()
    scale = depth_frame.get_depth_scale()

    depth_data = np.frombuffer(depth_frame.get_data(), dtype=np.uint16)
    depth_data = depth_data.reshape((height, width))
    depth_data = depth_data.astype(np.float32) * scale
    depth_image = cv2.normalize(depth_data, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    depth_image = cv2.applyColorMap(depth_image, cv2.COLORMAP_JET)
    return depth_image


def main():
    pipeline = Pipeline()
    config = Config()

    # Enable color stream
    profile_list = pipeline.get_stream_profile_list(OBSensorType.COLOR_SENSOR)
    color_profile = profile_list.get_default_video_stream_profile()
    config.enable_stream(color_profile)
    print(f"Color: {color_profile.get_width()}x{color_profile.get_height()}"
          f"@{color_profile.get_fps()} {color_profile.get_format()}")

    # Enable depth stream
    profile_list = pipeline.get_stream_profile_list(OBSensorType.DEPTH_SENSOR)
    depth_profile = profile_list.get_default_video_stream_profile()
    config.enable_stream(depth_profile)
    print(f"Depth: {depth_profile.get_width()}x{depth_profile.get_height()}"
          f"@{depth_profile.get_fps()} {depth_profile.get_format()}")

    pipeline.enable_frame_sync()
    pipeline.start(config)

    recording = False
    print("\nReady. Press R to record, S to stop recording, Q/ESC to quit.")

    try:
        while True:
            frames = pipeline.wait_for_frames(1000)
            if frames is None:
                continue

            images = []

            color_frame = frames.get_color_frame()
            if color_frame is not None:
                color_image = frame_to_bgr_image(color_frame)
                if color_image is not None:
                    images.append(color_image)

            depth_frame = frames.get_depth_frame()
            if depth_frame is not None:
                depth_image = render_depth(depth_frame)
                if depth_image is not None:
                    images.append(depth_image)

            if images:
                display_h = 480
                resized = []
                for img in images:
                    h, w = img.shape[:2]
                    display_w = int(w * display_h / h)
                    resized.append(cv2.resize(img, (display_w, display_h)))
                canvas = np.hstack(resized)

                # Recording indicator
                if recording:
                    cv2.circle(canvas, (30, 30), 12, (0, 0, 255), -1)
                    cv2.putText(canvas, "REC", (50, 38),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                cv2.imshow(WINDOW_NAME, canvas)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("r") and not recording:
                filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".bag"
                pipeline.start_recording(filename)
                recording = True
                print(f"Recording started: {filename}")

            elif key == ord("s") and recording:
                pipeline.stop_recording()
                recording = False
                print("Recording stopped.")

            elif key == ord("q") or key == ESC_KEY:
                break

    except KeyboardInterrupt:
        pass
    finally:
        if recording:
            pipeline.stop_recording()
            print("Recording stopped.")
        pipeline.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
