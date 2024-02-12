import numpy as np

from __global.utils import visualize_rep
from infrastructure import measure_squat_performance
from generation_functions import *
from score_functions import *

skeletons = np.ones(shape=(25, 7), dtype=float)
data = deterministic_model_generation_function_sin(25)
headers = ['right_knee_angle', 'left_knee_angle', 'left_side_body_angle', 'right_side_body_angle', 'ankle_distance',
           'knee_distance', 'hip_angle']
visualize_rep(data, headers)
# s = measure_squat_performance(skeletons, score_function=mse, generation_function=test_15,
#                               amount_of_skeletons_to_use_for_prediction=10)
# print(s)
