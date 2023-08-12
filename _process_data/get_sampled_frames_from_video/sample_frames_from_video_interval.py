import cv2
from pytube import YouTube


def get_frames_from_video(url: str, start_time: float, end_time: float, num_samples: int) -> list:
    """
    Retrieve frames from a YouTube video within a specified time range.

    Args:
        url (str): The URL of the YouTube video.
        start_time (float): The start time in seconds.
        end_time (float): The end time in seconds.
        num_samples (int): The number of frames to extract.

    Returns:
        list: A list of NumPy 3D arrays representing frames from the video.
    """
    # Download the video
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    video_path = stream.download()

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    frames = []

    for i in range(num_samples):
        # Calculate the frame time
        frame_time = start_time + (i / (num_samples - 1)) * (end_time - start_time)

        # Set the video capture to the desired frame
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(frame_time * cap.get(cv2.CAP_PROP_FPS)))

        # Read the frame
        ret, frame = cap.read()

        if ret:
            frames.append(frame)
        else:
            break

    # Release the video capture
    cap.release()

    return frames


