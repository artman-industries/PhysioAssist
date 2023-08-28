import tensorflow_hub as hub
from __global.skeleton import Skeleton
import tensorflow as tf

model = hub.load('https://bit.ly/metrabs_l')  # or _s
NAME_DICT = {'pelv': 'pelvis', 'lhip': 'left_hip', 'rhip': 'right_hip', 'bell': 'belly', 'lkne': 'left_knee',
             'rkne': 'right_knee', 'spin': 'spine', 'lank': 'left_ankle', 'rank': 'right_ankle', 'thor': 'thorax',
             'ltoe': 'left_toe', 'rtoe': 'right_toe', 'neck': 'neck', 'lcla': 'left_claw', 'rcla': 'right_claw',
             'head': 'head', 'lsho': 'left_shoulder', 'rsho': 'right_shoulder', 'lelb': 'left_elbow',
             'relb': 'right_elbow', 'lwri': 'left_wrist', 'rwri': 'right_wrist', 'lhan': 'left_hand',
             'rhan': 'right_hand', 'nose': 'nose', 'leye': 'left_eye', 'lear': 'left_ear', 'reye': 'right_eye',
             'rear': 'right_ear', 'rfoo': 'right_foot', 'lfoo': 'left_foot', 'htop': 'head_top', 'lthu': 'left_thumb',
             'rthu': 'right_thumb', 'lfin': 'left_finger', 'rfin': 'right_finger'}


def model1_predict_skeleton(frame, skeleton='smpl+head_30'):
    tf_frame = tf.image.decode_image(tf.io.read_file(frame))
    prediction = model.detect_poses(tf_frame, skeleton=skeleton)  # we assume only one person in frame
    coords = prediction['poses3d'][0].numpy()
    coord_dict = {}
    for i, joint_name in enumerate(model.per_skeleton_joint_names[skeleton].numpy().astype(str)):
        coord_dict[NAME_DICT[joint_name[:4]]] = coords[0, i]
    skeleton = Skeleton(
        pelvis=coord_dict['pelvis'],
        left_hip=coord_dict['left_hip'],
        right_hip=coord_dict['right_hip'],
        belly=coord_dict['belly'],
        left_knee=coord_dict['left_knee'],
        right_knee=coord_dict['right_knee'],
        spine=coord_dict['spine'],
        left_ankle=coord_dict['left_ankle'],
        right_ankle=coord_dict['right_ankle'],
        thorax=coord_dict['thorax'],
        left_toe=coord_dict['left_toe'],
        right_toe=coord_dict['right_toe'],
        neck=coord_dict['neck'],
        left_claw=coord_dict['left_claw'],
        right_claw=coord_dict['right_claw'],
        head=coord_dict['head'],
        left_shoulder=coord_dict['left_shoulder'],
        right_shoulder=coord_dict['right_shoulder'],
        left_elbow=coord_dict['left_elbow'],
        right_elbow=coord_dict['right_elbow'],
        left_wrist=coord_dict['left_wrist'],
        right_wrist=coord_dict['right_wrist'],
        left_hand=coord_dict['left_hand'],
        right_hand=coord_dict['right_hand'],
        nose=coord_dict['nose'],
        left_eye=coord_dict['left_eye'],
        left_ear=coord_dict['left_ear'],
        right_eye=coord_dict['right_eye'],
        right_ear=coord_dict['right_ear'],
        data=prediction
    )
    return skeleton

# def predict_skeletons(frame_list: list) -> list:
#     """
#     Process a list of 3D NumPy arrays using the given model and create a list of Skeleton objects.
#
#     Args:
#         frame_list (list): A list of 3D NumPy arrays representing frames.
#         model: The model used for processing the frames.
#
#     Returns:
#         list: A list of Skeleton objects.
#     """
#     skeletons = []
#     ##############################
#     # Note: it will be different #
#     ##############################
#     # todo:make it as batch calculation
#     for frame in frame_list:
#         # Process the frame using the model to get predicted skeleton
#         preds = model.detect_poses(frame, skeleton='smpl+head_30')
#         # todo: need to convert "predicted_skeleton" to match the Skeleton class parameters
#         points = preds['poses3d'][0, :, :]  # num_of_points, 3
#         # Create a Skeleton object using attributes_array
#         skeleton = None  # Skeleton(*attributes_array)
#
#         skeletons.append(skeleton)
#
#     return skeletons
