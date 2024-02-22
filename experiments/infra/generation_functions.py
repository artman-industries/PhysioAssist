import math

import numpy as np


def _deterministic_model_abstract_generation_function(knee_angle_function, body_angle_function, amount_of_frames):
    data_list = []

    for i in range(amount_of_frames):
        x = float(i) / amount_of_frames
        # y = 1 - (x - x ** 2)
        y_knee = knee_angle_function(x)
        y_body = body_angle_function(x)

        # Create a tensor
        right_knee_angle = y_knee
        left_knee_angle = y_knee
        left_side_body_angle = y_body
        right_side_body_angle = y_body
        ankle_distance = 0.8
        knee_distance = 1.25 - y_knee / 540
        hip_angle = 0

        # Concatenate the entries to create the tensor
        squat_tensor = np.array([right_knee_angle, left_knee_angle, left_side_body_angle,
                                 right_side_body_angle, ankle_distance, knee_distance, hip_angle])

        # Append the tensor to the list
        data_list.append(squat_tensor)

    return np.array(data_list)


def parabola(x):
    return 90 * (x ** 2 - x + 2)


def deterministic_model_generation_function_parabola(amount_of_frames):
    return _deterministic_model_abstract_generation_function(parabola, parabola, amount_of_frames)


def trigo_knees(x):
    return (180 - 90 * math.sin(math.pi * x)) / 360


def trigo_body(x):
    return (180 - 45 * math.sin(math.pi * x)) / 360


def deterministic_model_generation_function_trigo(amount_of_frames):
    return _deterministic_model_abstract_generation_function(trigo_knees, trigo_body, amount_of_frames)


def deterministic_model_20(s):
    return deterministic_model_generation_function_trigo(25)[-20:]


def deterministic_model_15(s):
    return deterministic_model_generation_function_trigo(25)[-15:]


def deterministic_model_10(s):
    return deterministic_model_generation_function_trigo(25)[-10:]


def deterministic_model_5(s):
    return deterministic_model_generation_function_trigo(25)[-5:]
