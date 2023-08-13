import pytorch_lightning as pl
from _training.models.pl_model import PLModel
from _training.models.inner_models.simple_rnn import RNNModel
from _training.dataset.data_loader import train_loader

num_attributes = 7  # todo: make it dynamic
# Hyper parameters
input_size = num_attributes
hidden_size = num_attributes * 1
output_size = num_attributes
num_layers = 1
learning_rate = 1e-3

# Initialize the Lightning module
rnn_model = RNNModel(input_size, hidden_size, output_size, num_layers)
pl_model = PLModel(rnn_model)

# Initialize the Lightning Trainer
trainer = pl.Trainer(max_epochs=10)  # Adjust max_epochs

# Train the model
trainer.fit(pl_model, train_loader)
