import pytorch_lightning as pl
from sklearn.ensemble import RandomForestRegressor
from _training.models.pl_model import PLModel
from _training.models.inner_models.simple_rnn import RNNModel
from _training.dataset.data_loader import get_train_test_split_rnn, split_test_train_and_inside
from sklearn.metrics import mean_squared_error
from datetime import datetime
import os
import numpy as np

# Define the directory where the checkpoint files are saved
checkpoint_dir = 'checkpoints'


def load_model(checkpoint_directory=checkpoint_dir, checkpoint_file=None):
    # Check if the directory exists and contains any checkpoint files
    if os.path.exists(checkpoint_dir) and os.listdir(checkpoint_dir):
        # Get a list of all checkpoint files in the directory
        checkpoint_files = [os.path.join(checkpoint_dir, f) for f in os.listdir(checkpoint_dir) if f.endswith('.ckpt')]

        # Choose the latest checkpoint file based on its modification time
        latest_checkpoint = max(checkpoint_files, key=os.path.getmtime)

        # Load the model from the latest checkpoint file
        if checkpoint_file is not None:
            # if specified, load the checkpoint file
            pl_model = PLModel.load_from_checkpoint(checkpoint_path=checkpoint_file)
        else:
            # if not specified, load the latest checkpoint
            pl_model = PLModel.load_from_checkpoint(checkpoint_path=latest_checkpoint)
        return pl_model, latest_checkpoint
    else:
        return None, None


def train_model(model, load=False, checkpoint_given_filename=None):
    train_loader, test_loader = get_train_test_split_rnn()
    if load:
        # Load the model from the latest checkpoint file
        pl_model, loaded_checkpoint_filename = load_model(checkpoint_filename=checkpoint_given_filename)
    if not load or pl_model is None:
        pl_model = PLModel(model)

    # Initialize the Lightning Trainer
    trainer = pl.Trainer(max_epochs=100)  # Adjust max_epochs

    # Train the model
    trainer.fit(pl_model, train_loader)
    trainer.test(dataloaders=train_loader)
    trainer.test(dataloaders=test_loader)

    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Define the checkpoint filename with the values of the hyper parameters -
    if load and loaded_checkpoint_filename is not None:
        checkpoint_filename_list = loaded_checkpoint_filename.split('_')
    else:
        checkpoint_filename_list = checkpoint_given_filename.split('_')
    checkpoint_filename_list[1] = now
    checkpoint_filename = '_'.join(checkpoint_filename_list)
    checkpoint_path = os.path.join(checkpoint_dir, checkpoint_filename)

    # Save the checkpoint
    trainer.save_checkpoint(checkpoint_path)
    return pl_model


def train_rnn_model():
    # No checkpoint files found, train a new model from scratch
    num_attributes = 7  # todo: make it dynamic
    # Hyper parameters
    input_size = num_attributes
    hidden_size = num_attributes * 4
    output_size = num_attributes
    num_layers = 1
    learning_rate = 1e-3

    # Initialize the Lightning module
    rnn_model = RNNModel(input_size, hidden_size, output_size, num_layers)
    checkpoint_filename = f'rnn_{0}_input{input_size}_hidden{hidden_size}_output{output_size}_layers{num_layers}_lr{learning_rate}.ckpt'
    train_model(rnn_model, False, checkpoint_filename)
    # possible to call with load=True and checkpoint_filename that we want to load


def random_forest_model_train():
    X_train, y_train, X_test, y_test = split_test_train_and_inside(0.8, 0.5)

    # Create the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # Evaluate the model - just for checking reasonable
    print(f'Accuracy: {mean_squared_error(y_test, predictions)}')


if __name__ == '__main__':
    train_rnn_model()
