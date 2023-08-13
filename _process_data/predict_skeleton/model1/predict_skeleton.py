import sys

sys.path.append('../../../global/skeleton.py')
from skeleton import Skeleton

# sys.path.append('../../../global')

model = None  # todo: define the model


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
        predicted_skeleton = model(frame)
        # todo: need to convert "predicted_skeleton" to match the Skeleton class parameters

        # Create a Skeleton object using attributes_array
        skeleton = Skeleton(*attributes_array)

        skeletons.append(skeleton)

    return skeletons
