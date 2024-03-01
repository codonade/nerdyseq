class Sequence:
  """Abstract representation of any sequence."""
  def __init__(self, terms: list[float]) -> None:
    self.terms = terms
    # The length of the sequence.
    self.len = len(self.terms)
    # The first two terms of the sequence.
    self.a_1, self.a_2 = self.terms[0], self.terms[1]
