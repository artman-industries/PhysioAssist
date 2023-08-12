from sample_frames_from_video_interval import *
import numpy as np

# Example usage
url = "https://www.youtube.com/watch?v=tsYm7GBIU7Y"
start_time = 30  # Start time in seconds
end_time = 120  # End time in seconds
num_samples = 10  # Number of samples

frames = get_frames_from_video(url, start_time, end_time, num_samples)
for idx, frame in enumerate(frames):
    np_frame = np.array(frame)
    print(f"Frame {idx + 1} shape: {np_frame.shape}")
