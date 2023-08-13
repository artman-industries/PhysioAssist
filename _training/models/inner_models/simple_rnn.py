import torch.nn as nn


class RNNModel(nn.Module):
    """
    Recurrent Neural Network (RNN) model for sequence prediction.

    Args:
        input_size (int): Number of input features in each time step.
        hidden_size (int): Number of features in the hidden state of the RNN.
        output_size (int): Number of output features from the RNN.
        num_layers (int): Number of recurrent layers.

    Attributes:
        rnn (nn.RNN): The RNN layer.
        fc (nn.Linear): Fully connected layer for output.

    Example:
        input_size = 5
        hidden_size = 64
        output_size = 5
        num_layers = 2
        rnn_model = RNNModel(input_size, hidden_size, output_size, num_layers)
    """

    def __init__(self, input_size, hidden_size, output_size, num_layers):
        super(RNNModel, self).__init__()

        # Create the RNN layer
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)

        # Create the fully connected (FC) output layer
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        """
        Forward pass of the RNN model.

        Args:
            x (torch.Tensor): Input tensor of shape (batch_size, sequence_length, input_size).

        Returns:
            torch.Tensor: Output tensor of shape (batch_size, sequence_length, output_size).
        """
        out, _ = self.rnn(x)
        batch_size, sequence_length, hidden_size = out.size()

        # Apply the fully connected layer to each time step's output
        out = out.reshape(batch_size * sequence_length, hidden_size)  # Reshape for FC layer
        final_output = self.fc(out)
        final_output = final_output.reshape(batch_size, sequence_length, -1)  # Reshape back

        return final_output
