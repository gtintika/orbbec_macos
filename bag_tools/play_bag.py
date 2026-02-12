"""Play back an Orbbec .bag file and display depth + color streams."""

import argparse
import sys

import cv2
import numpy as np
from pyorbbecsdk import Pipeline, OBMediaState

from utils import frame_to_bgr_image

ESC_KEY = 27
WINDOW_NAME = "Bag Playback"


def playback_state_callback(state):
    if state == OBMediaState.OB_MEDIA_BEGIN:
        print("Playback started")
    elif state == OBMediaState.OB_MEDIA_END:
        print("Playback ended")


def render_depth_frame(depth_frame) -> np.ndarray | None:
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
    parser = argparse.ArgumentParser(description="Play back an Orbbec .bag file")
    parser.add_argument("bag_file", help="Path to the .bag file")
    args = parser.parse_args()

    pipeline = Pipeline(args.bag_file)

    playback = pipeline.get_playback()
    playback.set_playback_state_callback(playback_state_callback)

    device_info = playback.get_device_info()
    print(f"Device: {device_info.get_name()} (S/N: {device_info.get_serial_number()})")

    pipeline.start()

    try:
        while True:
            frames = pipeline.wait_for_frames(1000)
            if frames is None:
                continue

            images = []

            depth_frame = frames.get_depth_frame()
            if depth_frame is not None:
                depth_image = render_depth_frame(depth_frame)
                if depth_image is not None:
                    images.append(("Depth", depth_image))

            color_frame = frames.get_color_frame()
            if color_frame is not None:
                color_image = frame_to_bgr_image(color_frame)
                if color_image is not None:
                    images.append(("Color", color_image))

            if images:
                # Resize all to the same height for side-by-side display
                display_h = 480
                resized = []
                for label, img in images:
                    h, w = img.shape[:2]
                    display_w = int(w * display_h / h)
                    resized.append(cv2.resize(img, (display_w, display_h)))
                cv2.imshow(WINDOW_NAME, np.hstack(resized))

            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == ESC_KEY:
                break
    except KeyboardInterrupt:
        pass
    finally:
        pipeline.stop()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
