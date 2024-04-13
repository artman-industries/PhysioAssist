import numpy as np


def measure_squat_performance(skeletons: np.array, score_function, generation_function,
                              amount_of_skeletons_to_use_for_prediction: int = 10, ):
    """
        Validate a list of skeletons to check if they "make sense" based on model predictions.

        Args:
            skeletons (2D np.array): The skeletons to validate. With shape of (N X D) where N is the number of skeletons and D is the skeleton dimention.
            score_function (function): A function used to measure the "distance" between 2 poses.
            amount_of_skeletons_to_use_for_prediction (int, optional): The Amount of skeletons to use for the prediction
            generation_function (function): A function used for generation the rest of the sequence depending on (amount_of_skeletons_to_use).

        Returns:
            np.array: scores for the repetition.
    """
    initial_skeleton = skeletons[0]
    # TODO: Check if the first skeleton is ready to squat

    # Generate a list of expected skeletons based on the model
    trusted_skeletons = skeletons[:amount_of_skeletons_to_use_for_prediction]
    expected_skeletons = generation_function(trusted_skeletons)
    untrusted_skeletons = skeletons[amount_of_skeletons_to_use_for_prediction:]

    scores = [score_function(s1, s2) for s1, s2 in zip(expected_skeletons, untrusted_skeletons)]
    scores = np.array(scores)

    return scores
