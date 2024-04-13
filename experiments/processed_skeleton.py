import numpy as np
from enum import Enum
import math
from skeleton import Skeleton


class AngleUnit(Enum):
    RADIANS = 'radians'
    DEGREES = 'degrees'


class ProcessedSkeleton:
    """
    A class representing a processed frame based on FrameRepresentation.
    """

    def __init__(self, skeleton: Skeleton, unit=AngleUnit.DEGREES):
        """
        Initializes a ProcessedFrameRepresentation instance.

        Args:
            skeleton (FrameRepresentation): The FrameRepresentation instance to process.
            unit (AngleUnit, optional): The unit of the angle representation. Defaults to AngleUnit.DEGREES.

        """
        self.unit = unit
        if skeleton is None:
            # Initialize attributes to default values
            self.right_knee_angle = 0.0
            self.left_knee_angle = 0.0
            self.left_side_body_angle = 0.0
            self.right_side_body_angle = 0.0
            self.ankle_distance = 0.0
            self.knee_distance = 0.0
            self.hip_angle = 0.0
        else:
            self.right_knee_angle = self.calculate_angle(skeleton.right_hip, skeleton.right_knee, skeleton.right_ankle)
            self.left_knee_angle = self.calculate_angle(skeleton.left_hip, skeleton.left_knee, skeleton.left_ankle)
            self.left_side_body_angle = self.calculate_angle(skeleton.left_shoulder, skeleton.left_hip,
                                                             skeleton.left_knee)
            self.right_side_body_angle = self.calculate_angle(skeleton.right_shoulder, skeleton.right_hip,
                                                              skeleton.right_knee)
            self.ankle_distance = self.calculate_distance(skeleton.left_ankle, skeleton.right_ankle)
            self.knee_distance = self.calculate_distance(skeleton.left_knee, skeleton.right_knee)
            self.hip_angle = self.calculate_hip_ankle_angle(skeleton.right_hip, skeleton.left_hip, skeleton.right_ankle,
                                                            skeleton.left_ankle)

    def calculate_distance(self, point1: np.ndarray, point2: np.ndarray) -> float:
        """
        Calculate the Euclidean distance between two points.

        Args:
            point1 (np.ndarray): The position of the first point.
            point2 (np.ndarray): The position of the second point.

        Returns:
            float: The Euclidean distance between the two points.
        """
        return np.linalg.norm(point1 - point2)

    def calculate_angle(self, a: np.ndarray, b: np.ndarray, c: np.ndarray,
                        unit: AngleUnit = AngleUnit.DEGREES) -> float:
        """
        Calculate the angle between points a, b, and c.

        Args:
            a (np.ndarray): Array representing point a with dimension d.
            b (np.ndarray): Array representing point b with dimension d.
            c (np.ndarray): Array representing point c with dimension d.
            unit (AngleUnit, optional): The unit of the angle representation (degrees or radians).
                    Defaults to AngleUnit.RADIANS.

        Returns:
            float: The angle between points ABC in the specified unit.
        """
        if a.shape != b.shape or b.shape != c.shape:
            raise ValueError("Dimensions of a, b, and c must be equal.")

        # Calculate vectors ab and bc
        ab = b - a
        bc = c - b

        # Calculate dot product of ab and bc
        dot_product = np.dot(ab, bc)

        # Calculate magnitudes of ab and bc
        magnitude_ab = np.linalg.norm(ab)
        magnitude_bc = np.linalg.norm(bc)

        # Calculate the angle using the dot product and magnitudes
        angle_rad = np.arccos(dot_product / (magnitude_ab * magnitude_bc))

        if unit == AngleUnit.DEGREES:
            angle = math.degrees(angle_rad)
        else:
            angle = angle_rad
        return angle

    def calculate_hip_ankle_angle(self, right_hip, left_hip, right_ankle, left_ankle):
        """
        Calculate the angle between the lines formed by the hips and the ankles.

        Args:
            right_hip (np.ndarray): The position of the right hip.
            left_hip (np.ndarray): The position of the left hip.
            right_ankle (np.ndarray): The position of the right ankle.
            left_ankle (np.ndarray): The position of the left ankle.
            unit (AngleUnit, optional): The unit of the angle representation. Defaults to AngleUnit.DEGREES.

        Returns:
            float: The angle between the lines formed by the hips and the ankles in the specified unit.
        """
        # Calculate vectors for hip and ankle lines
        hip_line = right_hip - left_hip
        ankle_line = right_ankle - left_ankle

        # Calculate dot product of hip line and ankle line
        dot_product = np.dot(hip_line, ankle_line)

        # Calculate magnitudes of hip line and ankle line
        magnitude_hip_line = np.linalg.norm(hip_line)
        magnitude_ankle_line = np.linalg.norm(ankle_line)

        # Calculate the angle using the dot product and magnitudes
        angle_rad = np.arccos(dot_product / (magnitude_hip_line * magnitude_ankle_line))

        if self.unit == AngleUnit.DEGREES:
            angle = math.degrees(angle_rad)
        else:
            angle = angle_rad

        return angle

    def to_numpy_array(self) -> np.ndarray:
        """
        Convert the processed skeleton attributes to a NumPy array.

        Returns:
            np.ndarray: A 1D NumPy array containing the processed skeleton attributes.
        """
        attributes = [
            self.right_knee_angle,
            self.left_knee_angle,
            self.left_side_body_angle,
            self.right_side_body_angle,
            self.ankle_distance,
            self.knee_distance,
            self.hip_angle
        ]

        return np.array(attributes)

    @classmethod
    def from_numpy_array(cls, np_array: np.ndarray, unit=AngleUnit.DEGREES):
        """
        Create a ProcessedSkeleton instance from a 1D NumPy array.

        Args:
            np_array (np.ndarray): The 1D NumPy array containing attribute values.
            unit (AngleUnit, optional): The unit of the angle representation. Defaults to AngleUnit.DEGREES.
        Returns:
            ProcessedSkeleton: A new ProcessedSkeleton instance initialized with the values from the array.
        """
        instance = cls(None, unit)
        instance.right_knee_angle, \
        instance.left_knee_angle, \
        instance.left_side_body_angle, \
        instance.right_side_body_angle, \
        instance.ankle_distance, \
        instance.knee_distance, \
        instance.hip_angle = np_array

        return instance
