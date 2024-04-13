from sklearn.metrics import mean_squared_error
import numpy as np


def cosine_similarity(vector1, vector2):
    dot_product = np.dot(vector1, vector2)
    norm_vector1 = np.linalg.norm(vector1)
    norm_vector2 = np.linalg.norm(vector2)
    similarity = dot_product / (norm_vector1 * norm_vector2)
    return similarity


def manhattan_distance(a, b):
    return sum(abs(a - b))


def mse(a, b):
    return mean_squared_error(a, b)
