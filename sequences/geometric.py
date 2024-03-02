from typing import override
from sequence import Sequence

class GeometricSequence(Sequence):
  """Sequence with terms obtained by mulltiplying the previous ones by a constant value."""
  @override
  def __init__(self, terms: list[float]) -> None:
    super().__init__(terms)
    # Common ratio between the sequence elements.
    self.r = self.a_2 / self.a_1

  @override
  def function(self) -> str:
    # ~ Exponential Sequences.
    if self.r == self.a_1:
      return f"G(n) = {self.a_1}ⁿ"
    # ~ Geometric Sequences.
    return f"G(1) = {self.a_1}, G(n) = {self.r}⁽ⁿ−¹⁾"

def identify_geometric_sequence(terms: list[float]) -> GeometricSequence | None:
  """Checks if a sequence is geometric and, if so, constructs GeometricSequence."""
  is_geometric = \
    terms[0] != 0 and \
    all(terms[i] / terms[i-1] == terms[1] / terms[0] \
      for i in range(2, len(terms)))
  return GeometricSequence(terms) if is_geometric else None

def compute_geometric_term(sequence: GeometricSequence, n: int) -> float:
  """Computes the nth geometric term for a GeometricSequence."""
  if n <= len(sequence):
    # Skips unnecessary computation.
    return sequence.terms[n - 1]

  return sequence.a_1 * (sequence.r ** (n - 1))
