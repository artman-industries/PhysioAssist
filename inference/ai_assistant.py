import numpy as np
from __global.processed_skeleton import ProcessedSkeleton
from __global.utils import is_number_around
from inference.generate_sequence.rnn_generate_seq import generate_skeletons
from inference.ready_to_squat.is_ready1 import is_ready_to_squat
from inference.generate_sequence.rnn_generate_seq import rnn_generate_skeletons


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


def validate_skeletons(skeletons: list, generation_function, amount_of_skeletons_to_use: int = 10,
                       similarity_threshold=0.1):
    """
        Validate a list of skeletons to check if they "make sense" based on squat readiness and model predictions.

        Args:
            skeletons (list of skeletons): The list of skeletons to validate.
            amount_of_skeletons_to_use (int, optional): The Amount of skeletons to use for the prediction
            generation_function (function): A function used for generation the rest of the sequence depending on (amount_of_skeletons_to_use).
            similarity_threshold (float, optional): The threshold for considering skeletons as similar.
                It represents the maximum acceptable difference between corresponding skeleton attributes.
                Defaults to 0.1.

        Returns:
            int: The index of the first skeleton in the list that does not meet the criteria,
                        or -1 if all skeletons pass the validation.
    """
    initial_skeleton = skeletons[0]
    # Check if the first skeleton is ready to squat
    if not is_ready_to_squat(initial_skeleton):
        return 0  # The first skeleton is not ready to squat

    # Generate a list of expected skeletons based on the model
    trusted_skeletons = skeletons[:amount_of_skeletons_to_use]
    expected_skeletons = generation_function(trusted_skeletons)
    untrusted_skeletons = skeletons[amount_of_skeletons_to_use:]

    # Check if the rest of the skeletons are similar to what the model predicted
    for i, (s1, s2) in enumerate(zip(expected_skeletons, untrusted_skeletons)):  # Start from the second skeleton
        if not compare_skeletons(s1, s2, similarity_threshold):
            return i  # Return the index of the first mismatch

    return -1  # All skeletons passed the validation


def rnn_generate_function(seq):
    return rnn_generate_skeletons(seq, 25 - len(seq))  # todo: make 25 dynamic number


if __name__ == "__main__":
    s1 = ProcessedSkeleton(None)
    initial_seq = [s1] * 25
    print(len(initial_seq))
    print(validate_skeletons(initial_seq, rnn_generate_function))  # todo: make it script parameter
