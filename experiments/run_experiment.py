import numpy as np
from infra.generation_functions import *
from infra.score_functions import mse
from infra.infrastructure import measure_squat_performance
import os
import pickle
from experiments.threshold_experiment import run_threshold_experiment
from experiments.losses_experience import run_losses_experiment

DIRECTORY="Squats_real_video_Skeleton"

# data = deterministic_model_generation_function_trigo(25)
#
# headers = ['right_knee_angle', 'left_knee_angle', 'left_side_body_angle', 'right_side_body_angle', 'ankle_distance',
#            'knee_distance', 'hip_angle']
# visualize_rep(data, headers)

def eval_function(rep):
    return measure_squat_performance(rep, generation_function=deterministic_model_15,
                                     score_function=mse)


def temp_function(rep):
    np.random.seed(1)
    return np.random.rand(10)

good_reps = []
bad_reps = []
for filename in os.listdir(DIRECTORY):
    if filename.endswith("_skeleton.pkl"):
        with open(os.path.join(DIRECTORY, filename), 'rb') as file:
            data = pickle.load(file)
            if filename.startswith("Wrong_"):
                bad_reps.append(data)
            else:
                if(np.array(data).shape == (1,25,7)):
                    data = np.array(data).reshape(25,7)
                good_reps.append(data)
print(f'Number of good reps: {len(good_reps)}')
print(f'Number of bad reps: {len(bad_reps)}')
print("Shape of good reps: ", np.array(good_reps).shape)
print("Shape of bad reps: ", np.array(bad_reps).shape)

# Run the experiment
results = run_threshold_experiment(good_reps=good_reps, bad_reps=bad_reps,
                                   performance_evaluation_function=eval_function,
                                   threshold_range=list(np.arange(0, 1000, 100)))

# results = run_losses_experiment(good_reps, bad_reps, [temp_function, temp_function], [0, 1])
