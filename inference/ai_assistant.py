import numpy as np
from __global.processed_skeleton import ProcessedSkeleton
from __global.utils import is_number_around
from inference.generate_sequence.generate1 import generate_skeletons
from inference.ready_to_squat.is_ready1 import is_ready_to_squat


def compare_skeletons(skeleton1, skeleton2, similarity_threshold=0.1):
    """
    Compare two skeleton objects to check if they are similar.

    Args:
        skeleton1 (ProcessedSkeleton): The first skeleton object.
        skeleton2 (ProcessedSkeleton): The second skeleton object.
        similarity_threshold (float, optional): The threshold for considering skeletons as similar.
            It represents the maximum acceptable difference between corresponding skeleton attributes.
            Defaults to 0.1.

    Returns:
        bool: True if the skeletons are similar, False otherwise.

    Notes:
        This function compares two skeleton objects and checks if they are similar.
        It considers the skeletons similar if the absolute differences between their attributes (e.g., angles, distances)
        are within the specified similarity_threshold.
    """
    # Compare attributes of the two skeletons
    return all(is_number_around(getattr(skeleton1, attr), getattr(skeleton2, attr), similarity_threshold)
               for attr in dir(skeleton1)
               if not callable(getattr(skeleton1, attr)) and not attr.startswith("__"))


def compare_skeleton_lists(list1, list2, similarity_threshold=0.1):
    """
    Compare two lists of skeleton objects to check where they are similar or not.

    Args:
        list1 (list): The first list of skeleton objects.
        list2 (list): The second list of skeleton objects. It must have the same length as list1.
        similarity_threshold (float, optional): The threshold for considering skeletons as similar.
            It represents the maximum acceptable difference between corresponding skeleton attributes.
            Defaults to 0.1.

    Returns:
        list of bool: A list of Boolean values indicating where the skeletons are similar (True) or not (False).

    Notes:
        This function compares corresponding pairs of skeletons from list1 and list2 and checks if they are similar.
        It considers the skeletons similar if the absolute differences between their attributes (e.g., angles, distances)
        are within the specified similarity_threshold.

        The attributes of the skeleton objects are assumed to be comparable using a function like 'compare_skeletons'.

        This function assumes that both lists have the same length.
    """
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

    return [compare_skeletons(s1, s2, similarity_threshold) for s1, s2 in zip(list1, list2)]


def validate_skeleton_list(pl_model, initial_skeleton, skeleton_list, similarity_threshold=0.1):
    """
    Validate a list of skeletons to check if they "make sense" based on squat readiness and model predictions.

    Args:
        pl_model (PLModel): The PyTorch Lightning model used for generating skeletons.
        initial_skeleton (Skeleton): The initial skeleton to check for squat readiness.
        skeleton_list (list of Skeleton): The list of skeletons to validate.
        similarity_threshold (float, optional): The threshold for considering skeletons as similar.
            It represents the maximum acceptable difference between corresponding skeleton attributes.
            Defaults to 0.1.

    Returns:
        int: The index of the first skeleton in the list that does not meet the criteria,
                    or -1 if all skeletons pass the validation.

    Notes:
        This function validates a list of skeletons based on two criteria:
        1. Squat Readiness: It checks if the first skeleton in the list is ready to start a squat.
        2. Model Predictions: It compares the rest of the skeletons in the list with what the model predicted
           based on the initial skeleton. All skeletons should be similar to what the model predicted.

        The function assumes that the PLModel has already been trained and is ready for inference.
    """
    # Check if the first skeleton is ready to squat
    if not is_ready_to_squat(initial_skeleton):
        return 0  # The first skeleton is not ready to squat

    # Generate a list of expected skeletons based on the model
    expected_skeletons = generate_skeletons(pl_model, initial_skeleton, num_skeletons=len(skeleton_list))

    # Check if the rest of the skeletons are similar to what the model predicted
    for i in range(1, len(skeleton_list)):  # Start from the second skeleton
        if not compare_skeletons(expected_skeletons[i], skeleton_list[i], similarity_threshold):
            return i  # Return the index of the first mismatch

    return -1  # All skeletons passed the validation


if __name__ == "__main__":
    # array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    # result = check_array_condition(array)
    # print(result)
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    ps = ProcessedSkeleton.from_numpy_array(arr)
    print(ps.to_numpy_array())
