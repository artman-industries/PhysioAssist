
def predict_skeletons(frame_list: list, activate_model_function) -> list:
    """
    Process a list of 3D NumPy arrays using the given model and create a list of Skeleton objects.

    Args:
        frame_list (list): A list of 3D NumPy arrays representing frames.
        activate_model_function: The function used for processing the frames to skeletons.

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
        skeleton = activate_model_function(frame)

        skeletons.append(skeleton)

    return skeletons
