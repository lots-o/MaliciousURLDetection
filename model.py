import torch
import torch.nn as nn


##############################################Recurrent Neural Net####################################################
class TemplateRNN(nn.Module):
    """Recurrent Neural Net Template"""

    def __init__(
        self,
        cell: str,
        feature_dim: int,
        hidden_dim: int,
        num_layers: int,
        drop_out: float,
        bidirectional: bool = False,
    ):
        super(TemplateRNN, self).__init__()
        params = dict(
            input_size=feature_dim,
            hidden_size=hidden_dim,
            num_layers=num_layers,
            batch_first=True,
            dropout=drop_out,
            bidirectional=bidirectional,
        )
        if cell == "rnn":
            self.rnn = nn.RNN(**params)
        elif cell == "lstm":
            self.rnn = nn.LSTM(**params)
        elif cell == "gru":
            self.rnn = nn.GRU(**params)

        self.cell = cell
        self.n_direction = 2 if bidirectional else 1
        self.hidden_dim = hidden_dim
        self.num_layers = num_layers


class EncoderRNN(TemplateRNN):
    """Recurrent Neural Net Encoder"""

    def __init__(self, *args, **kwargs):
        super(EncoderRNN, self).__init__(*args, **kwargs)

    def forward(self, x):
        """
        x = (batch_size, vocab_size, feature_dim)
        hidden = (self.n_direction * self.num_layers, batch_size, self.hidden_dim)
        """
        if self.cell in ["rnn", "gru"]:
            _, hidden = self.rnn(x)

        elif self.cell == "lstm":
            _, (hidden, _) = self.rnn(x)

        return (
            torch.cat([hidden[-2], hidden[-1]], dim=1)
            if self.n_direction == 2
            else hidden[-1]
        )  # (batch_size, self.hidden_dim * self.n_direction)


##############################################/Recurrent Neural Net####################################################
