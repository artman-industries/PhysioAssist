import math
import sys 
sys.path.append('..')
import numpy as np
import rnn_generate_skeleton
from joblib import load

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
        ankle_distance = 400
        knee_distance = 450
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
    return (120 * math.sin(math.pi * x))


def trigo_body(x):
    return (100 * math.sin(math.pi * x))


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


def deterministic_model_20_p(s):
    return deterministic_model_generation_function_parabola(25)[-20:]


def deterministic_model_15_p(s):
    return deterministic_model_generation_function_parabola(25)[-15:]


def deterministic_model_10_p(s):
    return deterministic_model_generation_function_parabola(25)[-10:]


def deterministic_model_5_p(s):
    return deterministic_model_generation_function_parabola(25)[-5:]

def rnn_model_20(s):
    return rnn_generate_skeleton.rnn_generate_skeletons(s,20,r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra')

def rnn_model_15(s):
    return rnn_generate_skeleton.rnn_generate_skeletons(s,15,r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra')

def rnn_model_10(s):
    return rnn_generate_skeleton.rnn_generate_skeletons(s,10,r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra')

def rnn_model_5(s):
    return rnn_generate_skeleton.rnn_generate_skeletons(s,5,r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra')

def random_forest_model_5(s):
    predicted = load(r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra\random_forest_model20.joblib').predict(s.reshape(1,-1))
    return predicted.reshape(5,7)

def random_forest_model_10(s):
    predicted =  load(r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra\random_forest_model15.joblib').predict(s.reshape(1,-1))
    return predicted.reshape(10,7)

def random_forest_model_15(s):
    predicted =  load(r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra\random_forest_model10.joblib').predict(s.reshape(1,-1))
    return predicted.reshape(15,7)

def random_forest_model_20(s):
    predicted = load(r'C:\Users\Alon\Documents\Studies\Spring 2023\Project in Artificial Intellijence\PhysioAssist\experiments\infra\random_forest_model5.joblib').predict(s.reshape(1,-1))
    return predicted.reshape(20,7)