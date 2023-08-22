# import tensorflow_hub as hub
from __global.skeleton import Skeleton

# model = hub.load('https://bit.ly/metrabs_l')  # or _s
# print(model.joint_names)


def model1_predict_skeleton(frame):
    # prediction = model.detect_poses(frame, skeleton='smpl+head_30')
    # todo: need to convert "predicted_skeleton" to match the Skeleton class parameters
    # points = prediction['poses3d'][0, :, :]  # num_of_points, 3
    # Create a Skeleton object using attributes_array
    skeleton = None  # Skeleton(*attributes_array)
    return skeleton
