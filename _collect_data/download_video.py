import os
import yt_dlp as youtube_dl


# https://www.youtube.com/watch?v=5dlubcRwYnI
from __global.utils import get_video_id_from_url


def download_video(url, name=None):
    """
    Download a video from a given URL and save it to the current working directory.

    Args:
        url (str): The URL of the video to be downloaded.
        name (str, optional): The desired name for the downloaded video file. If not provided,
                             the default name will be derived from the URL.

    Returns:
        str: The path to the downloaded video file, or None if an error occurred.
    """
    try:
        # If a custom name is not provided, use the URL as the name
        if name is None:
            name = get_video_id_from_url(url)

        # Add '.mp4' extension to the name if not already present
        if not name.endswith('.mp4'):
            name += '.mp4'

        # Construct the full path to save the video
        video_path = os.path.join(os.getcwd(), name)
        print(f'{video_path=}')
        # YouTube-DL options
        ydl_opts = {
            'outtmpl': video_path,  # Set the output file path and name
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        }

        # Download the video using YouTube-DL
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])  # Download the video from the provided URL

        print(f"Video downloaded and saved as: {video_path}")
        return video_path

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
