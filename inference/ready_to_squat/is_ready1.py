
# todo: make sure all the scalars here are fine
from __global.processed_skeleton import ProcessedSkeleton
from __global.utils import is_number_around


def is_ready_to_squat(skeleton: ProcessedSkeleton) -> bool:
    """
    Check if the skeleton is in a ready position to start a squat.

    Args:
        skeleton (ProcessedSkeleton): The processed skeleton object to check.

    Returns:
        bool: True if the skeleton is ready to start a squat, False otherwise.

    Notes:
        This function checks the following criteria:
        1. Both knee angles should be less than 90 degrees.
        2. The hip-to-ankle angle should be greater than or equal to 90 degrees.
        3. The ankle distance should be less than the knee distance.
    """
    # Check knee angles
    if is_number_around(skeleton.left_knee_angle, 180) and is_number_around(skeleton.right_knee_angle, 180):
        # Check hip-to-ankle angle
        if is_number_around(skeleton.hip_angle, 0):
            # Check ankle distance vs knee distance
            if is_number_around(skeleton.ankle_distance - skeleton.knee_distance, 0):
                return True

    return False
