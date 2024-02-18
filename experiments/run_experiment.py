import numpy as np
from __global.utils import visualize_rep
from experiments.infra.generation_functions import *
from experiments.infra.score_functions import mse
from infra.infrastructure import measure_squat_performance
from experiments.threshold_experiment import run_threshold_experiment
from experiments.init_reps_experience import run_initial_reps_experiment


# data = deterministic_model_generation_function_trigo(25)
#
# headers = ['right_knee_angle', 'left_knee_angle', 'left_side_body_angle', 'right_side_body_angle', 'ankle_distance',
#            'knee_distance', 'hip_angle']
# visualize_rep(data, headers)

def eval_function(rep):
    return measure_squat_performance(rep, generation_function=deterministic_model_15,
                                     score_function=mse)


def temp_function(rep):
    return np.array([1, 2, 3, 4, 5, 6, 7, 8])


good_reps = np.random.rand(10, 25, 7)
bad_reps = np.random.rand(10, 25, 7)

# Run the experiment
# results = run_threshold_experiment(good_reps, bad_reps, temp_function, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

results = run_initial_reps_experiment(good_reps, bad_reps, [temp_function, temp_function], [0, 1])
