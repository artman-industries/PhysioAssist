from _collect_data.display_frame import display_frame_at_timestamp
from _process_data.predict_skeletons.model1.model1_predict_skeleton import model1_predict_skeleton
from _process_data.predict_skeletons.predict_skeletons import predict_skeletons
import cv2

from __global.rep_object import RepObject

def video_to_skeleton_list(video_path, num_of_frames):
    """
    Process a video using the given model and create a list of Skeleton objects.

    Args:
        video_path (str): The path of the video.
        num_of_frames (int): The number of frames to process.

    Returns:
        list: A list of Skeleton objects.
    """
    video = cv2.VideoCapture(video_path)
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    fps = video.get(cv2.CAP_PROP_FPS)
    duration = frames / fps

    list_of_frames = []

    for i in range(num_of_frames):
        timestamp = duration / num_of_frames * i
        frame = display_frame_at_timestamp(video_path, timestamp)
        # save the frame in the repository
        frame_path = f"frame_{i}.jpg"
        cv2.imwrite(frame_path, frame)
        rep = RepObject(video_path)
        rep.add_frame(i, frame_path)
    list_of_frames.append(rep)
    print(list_of_frames)

    return predict_skeletons(list_of_frames, model1_predict_skeleton)

# Main function
if __name__ == "__main__":
    print("Alon doing experiment")
    video_path = r"C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\Squats_real_video\0_1.mov"
    num_of_frames = 25  # Example number of frames to process

    skeletons = video_to_skeleton_list(video_path, num_of_frames)
    print(skeletons)
    print(len(skeletons))