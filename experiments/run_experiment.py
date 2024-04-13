import numpy as np
from infra.generation_functions import *
from infra.score_functions import mse, cosine_similarity, manhattan_distance
from infra.infrastructure import measure_squat_performance
import os
import pickle
from experiments.threshold_experiment import run_threshold_experiment
from experiments.losses_experience import run_losses_experiment
import matplotlib.pyplot as plt

DIRECTORY="Squats_real_video_Skeleton"

# data = deterministic_model_generation_function_trigo(25)
#
# headers = ['right_knee_angle', 'left_knee_angle', 'left_side_body_angle', 'right_side_body_angle', 'ankle_distance',
#            'knee_distance', 'hip_angle']
# visualize_rep(data, headers)

def eval_function_random_forest(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_15,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=10)

def eval_function_rnn(rep):
    return measure_squat_performance(rep, generation_function=rnn_model_15,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=10)

def eval_function_deterministic(rep):
    return measure_squat_performance(rep, generation_function=deterministic_model_15,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=10)

def eval_function_random_forest_manhattan(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_15,
                                     score_function=manhattan_distance, amount_of_skeletons_to_use_for_prediction=10)

def eval_function_random_forest_cosine(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_15,
                                     score_function=cosine_similarity, amount_of_skeletons_to_use_for_prediction=10)

def eval_function_random_forest_5(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_5,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=20)

def eval_function_random_forest_10(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_10,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=15)

def eval_function_random_forest_20(rep):
    return measure_squat_performance(rep, generation_function=random_forest_model_20,
                                     score_function=mse, amount_of_skeletons_to_use_for_prediction=5)
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


# # Extracting each variable data
# data = good_reps[6]
# frames = list(range(1, 26))
# variables = ["Right Knee Angle", "Left Knee Angle", "Left Side Body Angle", 
#              "Right Side Body Angle", "Ankle Distance", "Knee Distance", "Hip Angle"]
# variable_indices = range(len(variables))

# plt.figure(figsize=(12, 8))

# for i in variable_indices:
#     plt.subplot(3, 3, i+1)
#     plt.plot(frames, [frame[i] for frame in data], marker='o', linestyle='-')
#     plt.title(variables[i])
#     plt.xlabel("Frame")
#     plt.ylabel("Angle/Distance")
#     plt.grid(True)

# plt.tight_layout()
# plt.show()


## The first experiment decide which model to use
# results = run_losses_experiment(good_reps, bad_reps, [eval_function_rnn, eval_function_random_forest, eval_function_deterministic], 
#                                 [1000, 1000, 1000], ["RNN", "Random Forest", "Deterministic"])

# # The second experiment decide which distance function to use
# results = run_losses_experiment(good_reps, bad_reps, [eval_function_random_forest, eval_function_random_forest_manhattan, eval_function_random_forest_cosine],
#                                 [1000, 1000, 1000], ["MSE", "Manhattan", "Cosine"])

# # The third experiment decide how many frames to start with in the prediction
# results = run_losses_experiment(good_reps, bad_reps, [eval_function_random_forest_5, eval_function_random_forest_10, eval_function_random_forest, eval_function_random_forest_20],
#                                 [1000, 1000, 1000, 1000], ["Random Forest 5", "Random Forest 10", "Random Forest 15", "Random Forest 20"])

# The forth and last experiment decide the threshold
results = run_threshold_experiment(good_reps=good_reps, bad_reps=bad_reps,
                                   performance_evaluation_function=eval_function_random_forest_20,
                                   threshold_range=list(np.arange(0, 2000, 200)), model_name="Random Forest 20")