from pyorbbecsdk import Pipeline, Context, OBStreamType


def main():
    ctx = Context()
    devs = ctx.query_devices()
    if devs.get_count() == 0 :
        print(f"No Orbbec Devices found !")
        return
        
    pipeline = Pipeline()

    # Depth profiles
    depth_profiles = pipeline.get_stream_profile_list(OBStreamType.DEPTH)
    print("DEPTH PROFILES:")
    for i in range(depth_profiles.get_count()):
        p = depth_profiles.get_profile(i).as_video_stream_profile()
        print(i, p.get_width(), p.get_height(), p.get_format(), p.get_fps())

    # Color profiles
    color_profiles = pipeline.get_stream_profile_list(OBStreamType.COLOR)
    print("\nCOLOR PROFILES:")
    for i in range(color_profiles.get_count()):
        p = color_profiles.get_profile(i).as_video_stream_profile()
        print(i, p.get_width(), p.get_height(), p.get_format(), p.get_fps())
    
    
if __name__ == "__main__":
    main()

