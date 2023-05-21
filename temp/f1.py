import torch
import torch.nn as nn

class PositionalEncoder(nn.Module):
  r"""
  Sine-cosine positional encoder for input points.
  """
  def __init__(
    self,
    d_input: int,
    n_freqs: int,
    log_space: bool = False
  ):
    super().__init__()
    self.d_input = d_input
    self.n_freqs = n_freqs
    self.log_space = log_space
    self.d_output = d_input * (1 + 2 * self.n_freqs)
    self.embed_fns = [lambda x: x]

    # Define frequencies in either linear or log scale
    if self.log_space:
      freq_bands = 2.**torch.linspace(0., self.n_freqs - 1, self.n_freqs)
    else:
      freq_bands = torch.linspace(2.**0., 2.**(self.n_freqs - 1), self.n_freqs)

    # Alternate sin and cos
    for freq in freq_bands:
      self.embed_fns.append(lambda x, freq=freq: torch.sin(x * freq))
      self.embed_fns.append(lambda x, freq=freq: torch.cos(x * freq))
  
  def forward(
    self,
    x
  ) -> torch.Tensor:
    r"""
    Apply positional encoding to input.
    """
    return torch.concat([fn(x) for fn in self.embed_fns], dim=-1)

if __name__ == "__main__":
    embed_fns = [lambda x: x]

    # Define frequencies in either linear or log scale
    freq_bands = 2.**torch.linspace(0., 3, 8)

    # Alternate sin and cos
    print("freq: ")
    for freq in freq_bands:
      print(f"{freq}", end=", ")
      embed_fns.append(lambda x, freq=freq: torch.sin(x * freq))
      embed_fns.append(lambda x, freq=freq: torch.cos(x * freq))
    print("")

    for fn in embed_fns:
      input = 1
      output = fn(input)
      print(f"input: {input}, output: {output}")
