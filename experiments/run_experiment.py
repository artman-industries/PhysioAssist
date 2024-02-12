import numpy as np

from __global.utils import visualize_rep
from infrastructure import measure_squat_performance
from generation_functions import *
from score_functions import *

reps = np.ones(shape=(20, 25, 7), dtype=float)
# data = deterministic_model_generation_function_trigo(25)
#
# headers = ['right_knee_angle', 'left_knee_angle', 'left_side_body_angle', 'right_side_body_angle', 'ankle_distance',
#            'knee_distance', 'hip_angle']
# visualize_rep(data, headers)

# squat_performance = measure_squat_performance(reps[1], score_function=mse, generation_function=deterministic_model_15,
#                                               amount_of_skeletons_to_use_for_prediction=10)
# print(squat_performance)

amount_of_frames = 25
squat_performances = []
for i in range(5, amount_of_frames):
    def det_model(rep):
        return deterministic_model_generation_function_trigo(amount_of_frames)[-i:]


    squat_performance = measure_squat_performance(reps[0], score_function=mse,
                                                  generation_function=det_model,
                                                  amount_of_skeletons_to_use_for_prediction=amount_of_frames - i)
    squat_performances.append(squat_performance)

squat_performances.reverse()
print([np.mean(s) for s in squat_performances])
