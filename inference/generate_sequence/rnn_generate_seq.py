import os

from __global.processed_skeleton import ProcessedSkeleton
import torch
from _training.train import load_model
from _training.models.pl_model import PLModel
from _training.models.inner_models.simple_rnn import RNNModel


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
    initial_input = torch.stack([torch.from_numpy(s.to_numpy_array()) for s in initial_skeletons]).unsqueeze(0)

    with torch.no_grad():
        # Generate 'num_skeletons' new skeletons
        for _ in range(num_skeletons):
            print(f'{initial_input.shape=}')
            # Pass the initial skeleton through the pl_model to generate a new skeleton
            output = model(initial_input)

            # Convert the model's output to a NumPy array or tensor format for the new skeleton
            new_skeleton_array = output.squeeze(0).detach().numpy()

            # Create a new Skeleton object from the generated array
            new_skeleton = ProcessedSkeleton.from_numpy_array(new_skeleton_array[-1])
            current_pred = torch.from_numpy(new_skeleton.to_numpy_array()).unsqueeze(0)

            # Append the new skeleton to the list
            generated_skeletons.append(new_skeleton)

            # Update the initial_input to include the new prediction
            # initial_input = torch.tensor(new_skeleton.to_numpy_array(), dtype=torch.float64).unsqueeze(0)
            # initial_input = torch.cat((initial_input, torch.from_numpy(new_skeleton.to_numpy_array()).unsqueeze(0)), dim=1)
            initial_input = torch.cat((initial_input, current_pred), dim=1)

    return generated_skeletons


if __name__ == '__main__':
    checkpoint_dir = 'checkpoints'
    # TODO: load the model properly
    # Get a list of all checkpoint files in the directory
    checkpoint_files = [os.path.join(checkpoint_dir, f) for f in os.listdir(checkpoint_dir) if f.endswith('.ckpt')]

    # Choose the latest checkpoint file based on its modification time
    latest_checkpoint_path = max(checkpoint_files, key=os.path.getmtime)

    latest_model_checkpoint = torch.load(latest_checkpoint_path)
    print(latest_model_checkpoint.keys())
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

    s1 = ProcessedSkeleton(None)
    s2 = ProcessedSkeleton(None)
    seq = generate_skeletons(model, [s1, s2])
