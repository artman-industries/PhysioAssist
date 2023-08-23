import numpy as np
from torch.utils.data import DataLoader
from _training.dataset.dataset import SkeletonDataset
from __database.preprocess_database.database_api import DatabaseAPI
from __global.processed_skeleton import ProcessedSkeleton

# todo: get the skeleton list from the processed database
database_api = DatabaseAPI(None)
reps = []
for rep_id in database_api.get_rep_ids():
    skeleton_list = database_api.get_skeletons(rep_id, model_name='model1')
    processed_skeleton_list = [ProcessedSkeleton(skeleton) for skeleton in skeleton_list]
    rep = np.array([processed_skeleton.to_numpy_array() for processed_skeleton in processed_skeleton_list])
    reps.append(rep)
reps = np.array(reps)
# [np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]]),
#              np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15]])]

# Set a random seed for reproducibility
np.random.seed(42)

# Number of reps, time stamps, and attributes
num_reps = 50
num_time_stamps = 10
num_attributes = 7

# Generate the dataset
dataset = np.random.rand(num_reps, num_time_stamps, num_attributes) * 100  # .astype(float)

train_dataset = SkeletonDataset(dataset)
train_loader = DataLoader(train_dataset, batch_size=2, shuffle=False)

if __name__ == 'view_dataset':
    for inputs, targets in train_loader:
        print(f"Input Sequence shape:", inputs.shape)
        print("Input Sequence:", inputs)
        print("Target Sequence shape:", targets.shape)
        print("Target Sequence:", targets)
        break  # Print only the first batch
