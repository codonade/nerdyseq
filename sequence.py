class Sequence:
  """Abstract representation of any sequence."""
  def __init__(self, terms: list[float]) -> None:
    self.terms = terms
    # The first two terms of the sequence.
    self.a_1, self.a_2 = self.terms[0], self.terms[1]

  def __len__(self) -> int:
    """How many terms are in this sequence?"""
    return len(self.terms)
