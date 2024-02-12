import math

import numpy as np


def test_15(s):
    l = [1] * 7
    return np.array([l] * 15, dtype=float)


def _deterministic_model_generation_function(math_function, amount_of_frames):
    data_list = []

    for i in range(amount_of_frames):
        x = float(i) / amount_of_frames
        # y = 1 - (x - x ** 2)
        y = math_function(x)

        # Create a tensor
        right_knee_angle = y
        left_knee_angle = y
        left_side_body_angle = 1
        right_side_body_angle = 1

        # Assign fixed values for the last three entries
        entry_5 = 5
        entry_6 = 6
        # entry_5 = np.array(seq[0][5])
        # entry_6 = np.array(seq[0][6])
        entry_7 = 0

        # Concatenate the entries to create the tensor
        squat_tensor = np.array([right_knee_angle, left_knee_angle, left_side_body_angle,
                                 right_side_body_angle, entry_5, entry_6, entry_7])

        # Append the tensor to the list
        data_list.append(squat_tensor)

    return np.array(data_list)


def parabola(x):
    return 90 * (x ** 2 - x + 2)


def deterministic_model_generation_function_parabola(amount_of_frames):
    return _deterministic_model_generation_function(parabola, amount_of_frames)


def sin(x):
    return 180 - 90 * math.sin(math.pi * x)


def deterministic_model_generation_function_sin(amount_of_frames):
    return _deterministic_model_generation_function(sin, amount_of_frames)