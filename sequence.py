class Sequence:
  """Abstract representation of any sequence."""
  # NOTE: Abstract.
  def __init__(self, terms: list[float]) -> None:
    self.terms = terms
    # First two terms of the sequence.
    self.a_1, self.a_2 = self.terms[0], self.terms[1]

  # NOTE: Not overridable.
  def __len__(self) -> int:
    """How many terms does this sequence have?"""
    return len(self.terms)

  # NOTE: Abstract.
  def function(self) -> str:
    """Outputs the mathematical representation of this sequence."""
    raise NotImplementedError()
