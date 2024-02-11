import numpy as np

from infrastructure import measure_squat_performance
from generation_functions import *
from score_functions import *

skeletons = np.ones(shape=(25, 7), dtype=float)
s = measure_squat_performance(skeletons, score_function=mse, generation_function=test_15,
                              amount_of_skeletons_to_use_for_prediction=10)
print(s)
