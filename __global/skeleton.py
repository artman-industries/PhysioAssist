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
        Initializes a FrameRepresentation instance.

        Args:
            right_shoulder np.ndarray: The position of the right shoulder. Defaults to None.
            left_shoulder np.ndarray: The position of the left shoulder. Defaults to None.
            right_elbow np.ndarray: The position of the right elbow. Defaults to None.
            left_elbow np.ndarray: The position of the left elbow. Defaults to None.
            right_wrist np.ndarray: The position of the right wrist. Defaults to None.
            left_wrist np.ndarray: The position of the left wrist. Defaults to None.
            right_hip np.ndarray: The position of the right hip. Defaults to None.
            left_hip np.ndarray: The position of the left hip. Defaults to None.
            right_knee np.ndarray: The position of the right knee. Defaults to None.
            left_knee np.ndarray: The position of the left knee. Defaults to None.
            right_ankle np.ndarray: The position of the right ankle. Defaults to None.
            left_ankle np.ndarray: The position of the left ankle. Defaults to None.

            data: The original data that created the frame
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
        Creates a new FrameRepresentation instance from a JSON string.

        Args:
            json_str (str): The JSON string representing the FrameRepresentation instance.

        Returns:
            FrameRepresentation: The created FrameRepresentation instance.
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
        return json.dumps(self.__dict__)

    def to_numpy_vector(self):
        """
        Converts the attributes of the FrameRepresentation instance into a numpy vector.

        Returns:
            numpy.ndarray: A numpy vector containing the attributes.
        """
        attributes = []

        # Retrieve all the attributes dynamically
        for attr_name, attr_value in self.__dict__.items():
            if np.isscalar(attr_value):
                attributes.append(attr_value)
            else:
                attributes.extend(attr_value)

        return np.array(attributes)
