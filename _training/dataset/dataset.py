import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


class SkeletonDataset(Dataset):
    """
    Custom dataset class for trajectory prediction using variable-length sequences.

    Args:
        data (List[np.ndarray]): List of 2D NumPy arrays representing skeletons.

    Attributes:
        data (List[np.ndarray]): List of 2D NumPy arrays representing skeletons.

    Example:
        skeleton_list = [np.array([[1, 2, 3], [4, 5, 6]]), np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])]
        dataset = SkeletonDataset(skeleton_list)
    """

    def __init__(self, data):
        self.data = data

    def __len__(self):
        """
        Get the total number of samples in the dataset.

        Returns:
            int: Total number of samples in the dataset.
        """
        return len(self.data)

    def __getitem__(self, idx):
        """
        Get an individual sample from the dataset.

        Args:
            idx (int): Index of the sample to retrieve.

        Returns:
            tuple: A tuple containing input sequence and target sequence.
        """
        # Extract input sequence by excluding the last time step
        input_seq = self.data[idx][0:-1, :]

        # Convert input sequence to a PyTorch tensor
        input_seq = torch.from_numpy(input_seq)  # .to(torch.double)

        # Extract target sequence by excluding the first time step
        target_seq = self.data[idx][1:, :]

        # Convert target sequence to a PyTorch tensor
        target_seq = torch.from_numpy(target_seq)  # .to(torch.double)

        return input_seq, target_seq
