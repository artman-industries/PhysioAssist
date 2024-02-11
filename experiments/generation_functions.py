import numpy as np


def test_15(s):
    l = [1] * 7
    return np.array([l] * 15, dtype=float)


def deterministic_model_generation_function(seq):
    data_list = []

    for i in range(len(seq)):
        x = float(i) / len(seq)
        y = x - x ** 2
        # Create a tensor
        right_knee_angle = np.array(y)
        left_knee_angle = np.array(y)
        left_side_body_angle = np.array(180)
        right_side_body_angle = np.array(180)

        # Assign fixed values for the last three entries
        entry_5 = np.array(seq[0][5])
        entry_6 = np.array(seq[0][6])
        entry_7 = np.array(0)

        # Concatenate the entries to create the tensor
        squat_tensor = np.concatenate([right_knee_angle, left_knee_angle, left_side_body_angle,
                                       right_side_body_angle, entry_5, entry_6, entry_7])

        # Append the tensor to the list
        data_list.append(squat_tensor)

    return np.array(data_list)
