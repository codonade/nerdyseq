from typing import override
from sequence import Sequence

class GeometricSequence(Sequence):
  """Sequence with terms obtained by mulltiplying the previous ones by a constant value."""
  @override
  def __init__(self, terms: list[float]) -> None:
    super().__init__(terms)
    # The common ratio between the sequence elements.
    self.r = self.a_2 / self.a_1

def identify_geometric_sequence(terms: list[float]) -> GeometricSequence | None:
  """Checks if a sequence is geometric and, if so, constructs GeometricSequence."""
  is_geometric = \
    terms[0] != 0 and \
    all(terms[i] / terms[i-1] == terms[1] / terms[0] \
      for i in range(2, len(terms)))
  return GeometricSequence(terms) if is_geometric else None

# TODO: Don't compute for `n` less than `sequence.len`
def compute_geometric_term(sequence: GeometricSequence, n: int) -> float:
  """Computes the nth geometric term for a GeometricSequence."""
  return sequence.a_1 * (sequence.r ** (n - 1))
