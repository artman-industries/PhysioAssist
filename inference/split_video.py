import cv2


def extract_timestamps(video_path, predicate_func):
    """
    Extract timestamps from a video based on a given predicate function.

    Args:
        video_path (str): The path to the input video file.
        predicate_func (callable): A predicate function that takes a frame (numpy.ndarray) as input and returns a boolean
                                   value indicating whether the frame meets the criteria.

    Returns:
        list: A list of timestamps (in seconds) where the predicate function is True.

    Raises:
        FileNotFoundError: If the specified video file does not exist.
        TypeError: If the predicate_func is not callable.

    Example:
        def custom_predicate(frame):
            # Example predicate function: Check if the frame has a certain color.
            # You can replace this with your own criteria.
            return some_condition

        video_path = 'video.mp4'
        timestamps = extract_timestamps(video_path, custom_predicate)
        print(timestamps)
    """
    try:
        # Open the video file for reading
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise FileNotFoundError(f"Video file not found: {video_path}")

        timestamps = []
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))

        while True:
            ret, frame = cap.read()

            if not ret:
                break

            if predicate_func(frame):
                current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0
                timestamps.append(current_time)

        return timestamps

    except FileNotFoundError:
        raise
    except TypeError:
        raise TypeError("predicate_func must be a callable function.")

    finally:
        if cap.isOpened():
            cap.release()


if __name__ == "__main__":
    def custom_predicate(frame):
        # Replace this function with your own predicate logic.
        # For example, you can check for specific content in the frame.
        return True  # Modify this condition as needed


    video_path = 'video.mp4'
    timestamps = extract_timestamps(video_path, custom_predicate)
    print(timestamps)
