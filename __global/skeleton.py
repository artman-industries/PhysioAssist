import numpy as np
import json


class Skeleton:
    """
    A class representing a frame.
    """

    def __init__(
            self,
            pelvis: np.ndarray = None,
            left_hip: np.ndarray = None,
            right_hip: np.ndarray = None,
            belly: np.ndarray = None,
            left_knee: np.ndarray = None,
            right_knee: np.ndarray = None,
            spine: np.ndarray = None,
            left_ankle: np.ndarray = None,
            right_ankle: np.ndarray = None,
            thorax: np.ndarray = None,
            left_toe: np.ndarray = None,
            right_toe: np.ndarray = None,
            neck: np.ndarray = None,
            left_claw: np.ndarray = None,
            right_claw: np.ndarray = None,
            head: np.ndarray = None,
            left_shoulder: np.ndarray = None,
            right_shoulder: np.ndarray = None,
            left_elbow: np.ndarray = None,
            right_elbow: np.ndarray = None,
            left_wrist: np.ndarray = None,
            right_wrist: np.ndarray = None,
            left_hand: np.ndarray = None,
            right_hand: np.ndarray = None,
            nose: np.ndarray = None,
            left_eye: np.ndarray = None,
            left_ear: np.ndarray = None,
            right_eye: np.ndarray = None,
            right_ear: np.ndarray = None,

            # right_shoulder: np.ndarray,
            # left_shoulder: np.ndarray,
            # right_elbow: np.ndarray,
            # left_elbow: np.ndarray,
            # right_wrist: np.ndarray,
            # left_wrist: np.ndarray,
            # right_hip: np.ndarray,
            # left_hip: np.ndarray,
            # right_knee: np.ndarray,
            # left_knee: np.ndarray,
            # right_ankle: np.ndarray,
            # left_ankle: np.ndarray,
            data = None
    ):
        """
        Initializes a Skeleton instance.

        Args:
            right_shoulder np.ndarray: The position of the right shoulder.
            left_shoulder np.ndarray: The position of the left shoulder.
            right_elbow np.ndarray: The position of the right elbow.
            left_elbow np.ndarray: The position of the left elbow.
            right_wrist np.ndarray: The position of the right wrist.
            left_wrist np.ndarray: The position of the left wrist.
            right_hip np.ndarray: The position of the right hip.
            left_hip np.ndarray: The position of the left hip.
            right_knee np.ndarray: The position of the right knee.
            left_knee np.ndarray: The position of the left knee.
            right_ankle np.ndarray: The position of the right ankle.
            left_ankle np.ndarray: The position of the left ankle.
            # data: The original data that created the frame
        """

        self.pelvis = pelvis
        self.left_hip = left_hip
        self.right_hip = right_hip
        self.belly = belly
        self.left_knee = left_knee
        self.right_knee = right_knee
        self.spine = spine
        self.left_ankle = left_ankle
        self.right_ankle = right_ankle
        self.thorax = thorax
        self.left_toe = left_toe
        self.right_toe = right_toe
        self.neck = neck
        self.left_claw = left_claw
        self.right_claw = right_claw
        self.head = head
        self.left_shoulder = left_shoulder
        self.right_shoulder = right_shoulder
        self.left_elbow = left_elbow
        self.right_elbow = right_elbow
        self.left_wrist = left_wrist
        self.right_wrist = right_wrist
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.nose = nose
        self.left_eye = left_eye
        self.left_ear = left_ear
        self.right_eye = right_eye
        self.right_ear = right_ear
        self.data = data
        # self.right_shoulder = right_shoulder
        # self.left_shoulder = left_shoulder
        # self.right_elbow = right_elbow
        # self.left_elbow = left_elbow
        # self.right_wrist = right_wrist
        # self.left_wrist = left_wrist
        # self.right_hip = right_hip
        # self.left_hip = left_hip
        # self.right_knee = right_knee
        # self.left_knee = left_knee
        # self.right_ankle = right_ankle
        # self.left_ankle = left_ankle

        # self.data = data

    @classmethod
    def from_json(cls, json_str):
        """
        Creates a new Skeleton instance from a JSON string.

        Args:
            json_str (str): The JSON string representing the Skeleton instance.

        Returns:
            Skeleton: The created Skeleton instance.
        """
        json_data = json.loads(json_str)

        return cls(
            right_shoulder=np.array(json_data['right_shoulder']),
            left_shoulder=np.array(json_data['left_shoulder']),
            right_elbow=np.array(json_data['right_elbow']),
            left_elbow=np.array(json_data['left_elbow']),
            right_wrist=np.array(json_data['right_wrist']),
            left_wrist=np.array(json_data['left_wrist']),
            right_hip=np.array(json_data['right_hip']),
            left_hip=np.array(json_data['left_hip']),
            right_knee=np.array(json_data['right_knee']),
            left_knee=np.array(json_data['left_knee']),
            right_ankle=np.array(json_data['right_ankle']),
            left_ankle=np.array(json_data['left_ankle'])
        )

    def to_json(self):
        """
        Converts the Skeleton instance to a JSON string.

        Returns:
            str: The JSON representation of the Skeleton instance.
        """
        return json.dumps(self.to_dict())

    def to_dict(self):
        """
        Converts the Skeleton instance to a dictionary with attributes as lists.

        Returns:
            dict: A dictionary containing the attributes of the Skeleton instance as lists.
        """
        attributes = {}

        for attr_name, attr_value in self.__dict__.items():
            if np.isscalar(attr_value):
                attributes[attr_name] = attr_value.tolist() if isinstance(attr_value, np.ndarray) else attr_value
            else:
                attributes[attr_name] = attr_value.tolist()

        return attributes  # Returning a dictionary of lists

    @classmethod
    def from_dict(cls, data_dict):
        """
        Creates a new Skeleton instance from a dictionary.

        Args:
            data_dict (dict): The dictionary representing the Skeleton instance.

        Returns:
            Skeleton: The created Skeleton instance.
        """
        return cls(
            right_shoulder=np.array(data_dict['right_shoulder']),
            left_shoulder=np.array(data_dict['left_shoulder']),
            right_elbow=np.array(data_dict['right_elbow']),
            left_elbow=np.array(data_dict['left_elbow']),
            right_wrist=np.array(data_dict['right_wrist']),
            left_wrist=np.array(data_dict['left_wrist']),
            right_hip=np.array(data_dict['right_hip']),
            left_hip=np.array(data_dict['left_hip']),
            right_knee=np.array(data_dict['right_knee']),
            left_knee=np.array(data_dict['left_knee']),
            right_ankle=np.array(data_dict['right_ankle']),
            left_ankle=np.array(data_dict['left_ankle'])
        )

    def to_numpy_vector(self):
        """
        Converts the attributes of the Skeleton instance into a numpy vector.

        Returns:
            numpy.ndarray: A numpy vector containing the attributes.
        """
        attributes = []

        for attr_name, attr_value in self.__dict__.items():
            if np.isscalar(attr_value):
                attributes.append(attr_value)
            else:
                attributes.extend(attr_value)

        return np.array(attributes)

    def to_numpy_matrix(self):
        """
        Converts the attributes of the Skeleton instance into a numpy vector.

        Returns:
            numpy.ndarray: A numpy vector containing the attributes.
        """
        attributes = []

        for attr_name, attr_value in self.__dict__.items():
            if np.isscalar(attr_value):
                print('error')  # todo: raise an error
                # attributes.append(attr_value)
            else:
                attributes.append(attr_value)

        return np.array(attributes)


# rs = np.array([1, 2])
# ls = np.array([3, 2])
# moc = np.array([0, 0])
# skeleton = Skeleton(right_shoulder=rs, left_shoulder=ls, right_knee=moc, left_hip=moc, right_hip=moc, right_ankle=moc,
#                     left_ankle=moc, right_elbow=moc, left_elbow=moc, right_wrist=moc, left_wrist=moc, left_knee=moc)
# print(skeleton.to_json())
# # print(skeleton.to_dict())
# print(skeleton.to_numpy_matrix())
