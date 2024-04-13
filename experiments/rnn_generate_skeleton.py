import numpy as np
import sys
sys.path.append('..')

import os

from processed_skeleton import ProcessedSkeleton
import torch
from pl_model import PLModel
from simple_rnn import RNNModel


def generate_skeletons(model, initial_skeletons, num_skeletons=24):
    """
    Generate a list of skeletons using a PyTorch Lightning model and an initial skeleton.

    Args:
        model (PLModel): A PyTorch Lightning model used for generating skeletons.
        initial_skeletons (list[ProcessedSkeleton]): A list of the initial skeletons from which to generate new skeletons.
        num_skeletons (int, optional): The number of skeletons to generate. Defaults to 24.

    Returns:
        list of Skeleton: A list containing the generated skeletons.

    Notes:
        This function takes the provided initial skeleton and generates additional skeletons using the pl_model.
        It generates 'num_skeletons' new skeletons based on the initial skeleton by repeatedly passing it
        through the model and using the model's predictions to create new skeletons.

        The function assumes that 'pl_model' has already been trained and is ready for inference.

    """
    generated_skeletons = []

    # Convert the initial skeletons to a format compatible with the model (tensor)
    initial_input = torch.stack([torch.from_numpy(s) for s in initial_skeletons]).unsqueeze(0)

    with torch.no_grad():
        # Generate 'num_skeletons' new skeletons
        for _ in range(num_skeletons):
            # Pass the initial skeleton through the pl_model to generate a new skeleton
            output = model(initial_input)

            # Convert the model's output to a NumPy array or tensor format for the new skeleton
            new_skeleton_array = output.squeeze(0).detach().numpy()

            # Create a new Skeleton object from the generated array
            new_skeleton = ProcessedSkeleton.from_numpy_array(new_skeleton_array[-1])
            current_pred = torch.from_numpy(new_skeleton.to_numpy_array()).unsqueeze(0).unsqueeze(0)

            # Append the new skeleton to the list
            generated_skeletons.append(new_skeleton_array[-1])

            # Update the initial_input to include the new prediction
            initial_input = torch.cat((initial_input, current_pred), dim=1)

    return generated_skeletons


def rnn_generate_skeletons(initial_seq: list, num_skeletons=24, checkpoint_path: str = None):
    if checkpoint_path is None:
        # Define the name of your project folder
        project_folder_name = "PhysioAssist"

        # Get the current working directory
        current_directory = os.getcwd()

        # Iterate upwards in the directory structure until the project folder is found
        while current_directory:
            if os.path.basename(current_directory) == project_folder_name:
                # If the project folder is found, construct the checkpoints path
                checkpoint_path = os.path.join(current_directory, "_training", "checkpoints")
                break
            # Move up one level in the directory structure
            current_directory = os.path.dirname(current_directory)

    checkpoint_dir = str(checkpoint_path)  # '../../_training/checkpoints'

    # Get a list of all checkpoint files in the directory
    checkpoint_files = [os.path.join(checkpoint_dir, f) for f in os.listdir(checkpoint_dir) if f.endswith('.ckpt')]

    # Choose the latest checkpoint file based on its modification time
    latest_checkpoint_path = max(checkpoint_files, key=os.path.getmtime)

    # TODO: load the model properly
    latest_model_checkpoint = torch.load(latest_checkpoint_path)
    # latest_model = load_model()

    num_attributes = 7  # todo: make it dynamic
    # Hyper parameters
    input_size = num_attributes
    hidden_size = num_attributes * 4
    output_size = num_attributes
    num_layers = 1
    learning_rate = 1e-3

    # Initialize the Lightning module
    rnn_model = RNNModel(input_size, hidden_size, output_size, num_layers)
    model = PLModel(rnn_model)
    model.load_state_dict(latest_model_checkpoint['state_dict'])
    generated_seq = generate_skeletons(model, initial_seq, num_skeletons=num_skeletons)
    return generated_seq
