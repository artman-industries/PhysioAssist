from __global.processed_skeleton import ProcessedSkeleton
import torch


def generate_skeletons(model, initial_skeleton, num_skeletons=24):
    """
    Generate a list of skeletons using a PyTorch Lightning model and an initial skeleton.

    Args:
        model (PLModel): A PyTorch Lightning model used for generating skeletons.
        initial_skeleton (ProcessedSkeleton): The initial skeleton from which to generate new skeletons.
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

    # Convert the initial skeleton to a format compatible with the model (e.g., NumPy array or tensor)
    initial_input = torch.tensor(initial_skeleton.to_numpy_array(), dtype=torch.float64).unsqueeze(0)

    with torch.no_grad():
        # Generate 'num_skeletons' new skeletons
        for _ in range(num_skeletons):
            # Pass the initial skeleton through the pl_model to generate a new skeleton
            output = model(initial_input)

            # Convert the model's output to a NumPy array or tensor format for the new skeleton
            new_skeleton_array = output.squeeze(0).detach().numpy()

            # Create a new Skeleton object from the generated array
            new_skeleton = ProcessedSkeleton.from_numpy_array(new_skeleton_array)

            # Append the new skeleton to the list
            generated_skeletons.append(new_skeleton)

            # Update the initial_input for the next iteration
            initial_input = torch.tensor(new_skeleton.to_numpy_array(), dtype=torch.float64).unsqueeze(0)

    return generated_skeletons
