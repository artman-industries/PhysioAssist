import numpy as np
from torch.utils.data import DataLoader, random_split
from _training.dataset.dataset import SkeletonDataset
from __database.preprocess_database.database_api import DatabaseAPI
from __global.processed_skeleton import ProcessedSkeleton
import plotly.graph_objects as go
from PIL import Image, ImageDraw, ImageFont

def visualize_points_with_names(skeleton_list):
    for skeleton in skeleton_list[:5]:
        x_coords = []
        y_coords = []
        z_coords = []
        names = []
        for attr_name, attr_value in skeleton.__dict__.items():
            if(attr_value is not None):
                x_coords.append(attr_value[0])
                y_coords.append(attr_value[1])
                z_coords.append(attr_value[2])
                names.append(attr_name)

        fig = go.Figure(data=[go.Scatter3d(
            x=x_coords,
            y=y_coords,
            z=z_coords,
            mode='markers',
            marker=dict(
                size=12,
                color=z_coords,                # set color to an array/list of desired values
                colorscale='Viridis',   # choose a colorscale
                opacity=0.8
            ),
            text=list(names),
            hoverinfo='text'
        )])
        fig.show()
# todo: get the skeleton list from the processed database
database_api = DatabaseAPI(None)
reps = []
for rep_id in database_api.get_rep_ids():
    skeleton_list = database_api.get_skeletons(rep_id, model_name='model1')  # todo: change the model_name
    processed_skeleton_list = [ProcessedSkeleton(skeleton) for skeleton in skeleton_list]
    # visualize_points_with_names(skeleton_list)
    rep = np.array([processed_skeleton.to_numpy_array() for processed_skeleton in processed_skeleton_list])
    reps.append(rep)
reps = np.array(reps)

# Set a random seed for reproducibility
np.random.seed(42)

# Number of reps, time stamps, and attributes
num_reps = 50
num_time_stamps = 10
num_attributes = 7

# Generate the dataset
# reps = np.random.rand(num_reps, num_time_stamps, num_attributes) * 100  # todo: remove it when the dataset is ready in the db

# Define the ratio for splitting the dataset (e.g., 80% train, 20% test)
train_ratio = 0.8
test_ratio = 1 - train_ratio

# Calculate the sizes of the train and test splits
train_size = int(train_ratio * len(reps))
test_size = len(reps) - train_size

# Split the dataset into train and test sets using NumPy
train_data = reps[:train_size]
test_data = reps[train_size:]

# Create train and test SkeletonDataset
train_dataset = SkeletonDataset(train_data)
test_dataset = SkeletonDataset(test_data)

# Create DataLoader instances for the train and test datasets
batch_size = 2
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=False)
test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

if __name__ == '__main__':
    for inputs, targets in train_loader:
        print(f"Input Sequence shape:", inputs.shape)
        print("Input Sequence:", inputs)
        print("Target Sequence shape:", targets.shape)
        print("Target Sequence:", targets)
        break  # Print only the first batch

    for inputs, targets in test_loader:
        print(f"Input Sequence shape:", inputs.shape)
        print("Input Sequence:", inputs)
        print("Target Sequence shape:", targets.shape)
        print("Target Sequence:", targets)
        break
