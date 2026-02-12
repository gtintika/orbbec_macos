"""Inspect an Orbbec .bag file and print diagnostic info."""

import argparse
import sys

from pyorbbecsdk import Pipeline, OBMediaState


def playback_state_callback(state):
    if state == OBMediaState.OB_MEDIA_BEGIN:
        print("[state] Playback started")
    elif state == OBMediaState.OB_MEDIA_END:
        print("[state] Playback ended")


def main():
    parser = argparse.ArgumentParser(description="Inspect an Orbbec .bag file")
    parser.add_argument("bag_file", help="Path to the .bag file")
    parser.add_argument("-n", "--max-frames", type=int, default=30,
                        help="Max framesets to read (default: 30)")
    args = parser.parse_args()

    print(f"Opening: {args.bag_file}")
    pipeline = Pipeline(args.bag_file)

    playback = pipeline.get_playback()
    playback.set_playback_state_callback(playback_state_callback)

    try:
        device_info = playback.get_device_info()
        print(f"Device name:    {device_info.get_name()}")
        print(f"Serial number:  {device_info.get_serial_number()}")
        print(f"Firmware:       {device_info.get_firmware_version()}")
        print(f"PID:            {device_info.get_pid()}")
        print(f"Connection:     {device_info.get_connection_type()}")
    except Exception as e:
        print(f"Could not read device info: {e}")

    try:
        camera_param = pipeline.get_camera_param()
        print(f"Camera param:   {camera_param}")
    except Exception as e:
        print(f"Could not read camera param: {e}")

    pipeline.start()

    count = 0
    empty = 0
    print(f"\nReading up to {args.max_frames} framesets (timeout 2000ms each)...\n")

    for i in range(args.max_frames + empty):
        if count >= args.max_frames:
            break
        if empty > 20:
            print("Too many consecutive empty reads, stopping.")
            break

        frames = pipeline.wait_for_frames(2000)
        if frames is None:
            empty += 1
            continue

        empty = 0
        count += 1
        parts = []

        depth = frames.get_depth_frame()
        if depth:
            parts.append(
                f"depth {depth.get_width()}x{depth.get_height()} "
                f"fmt={depth.get_format()} scale={depth.get_depth_scale()} "
                f"ts={depth.get_timestamp()}"
            )

        color = frames.get_color_frame()
        if color:
            parts.append(
                f"color {color.get_width()}x{color.get_height()} "
                f"fmt={color.get_format()} ts={color.get_timestamp()}"
            )

        ir = frames.get_ir_frame()
        if ir:
            parts.append(
                f"ir {ir.get_width()}x{ir.get_height()} "
                f"fmt={ir.get_format()} ts={ir.get_timestamp()}"
            )

        n = frames.get_frame_count()
        print(f"[{count:3d}] {n} frame(s): {' | '.join(parts) if parts else '(no recognized frames)'}")

    print(f"\nTotal framesets read: {count}")
    pipeline.stop()


if __name__ == "__main__":
    main()
