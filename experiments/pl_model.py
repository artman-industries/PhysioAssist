import pytorch_lightning as pl
import torch
import torch.nn as nn


class PLModel(pl.LightningModule):
    """
    PyTorch Lightning module wrapper for training a neural network model.

    Args:
        model (nn.Module): The neural network model to be trained.
        learning_rate (float): Learning rate for the optimizer.

    Attributes:
        model (nn.Module): The neural network model to be trained.
        loss_fn (nn.Module): Loss function for computing the training loss.
        learning_rate (float): Learning rate for the optimizer.

    Example:
        input_size = 5
        hidden_size = 64
        output_size = 3
        num_layers = 2
        rnn_model = RNNModel(input_size, hidden_size, output_size, num_layers)
        pl_model = PLModel(rnn_model, learning_rate=0.001)
    """

    def __init__(self, model, learning_rate=1e-3):
        super(PLModel, self).__init__()

        # Assign the provided model
        self.model = model.double()

        # Define the loss function
        self.loss_fn = nn.MSELoss()

        # Set the learning rate for the optimizer
        self.learning_rate = learning_rate

    def forward(self, x):
        """
        Forward pass of the model.

        Args:
            x (torch.Tensor): Input tensor.

        Returns:
            torch.Tensor: Output tensor.
        """
        out = self.model(x.double())
        return out

    def configure_optimizers(self):
        """
        Configure the optimizer for training.

        Returns:
            torch.optim.Optimizer: Optimizer for training the model.
        """
        return torch.optim.Adam(self.parameters(), lr=self.learning_rate)

    def training_step(self, batch, batch_idx):
        """
        Training step for a single batch of data.

        Args:
            batch (tuple): Tuple containing input and target tensors.
            batch_idx (int): Index of the batch.

        Returns:
            torch.Tensor: The computed loss for the batch.
        """
        inputs, targets = batch
        outputs = self(inputs)
        loss = self.loss_fn(outputs, targets)
        self.log('train_loss', loss)
        return loss

    def test_step(self, batch, batch_idx):
        """
        Test step for a single batch of data.

        Args:
            batch (tuple): Tuple containing input and target tensors.
            batch_idx (int): Index of the batch.

        Returns:
            torch.Tensor: The computed loss for the batch during testing.
        """
        inputs, targets = batch
        outputs = self(inputs)
        loss = self.loss_fn(outputs, targets)
        self.log('test_loss', loss)
        return loss
