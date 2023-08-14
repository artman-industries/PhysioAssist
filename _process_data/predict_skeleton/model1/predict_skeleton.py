import tensorflow_hub as hub
from __global.skeleton import Skeleton

model = hub.load('https://bit.ly/metrabs_l')  # or _s


def predict_skeletons(frame_list: list) -> list:
    """
    Process a list of 3D NumPy arrays using the given model and create a list of Skeleton objects.

    Args:
        frame_list (list): A list of 3D NumPy arrays representing frames.
        model: The model used for processing the frames.

    Returns:
        list: A list of Skeleton objects.
    """
    skeletons = []
    ##############################
    # Note: it will be different #
    ##############################
    # todo:make it as batch calculation
    for frame in frame_list:
        # Process the frame using the model to get predicted skeleton
        preds = model.detect_poses(frame, skeleton='smpl+head_30')
        # todo: need to convert "predicted_skeleton" to match the Skeleton class parameters
        points = preds['poses3d'][0, :, :]  # num_of_points, 3
        # Create a Skeleton object using attributes_array
        skeleton = None#Skeleton(*attributes_array)

        skeletons.append(skeleton)

    return skeletons
