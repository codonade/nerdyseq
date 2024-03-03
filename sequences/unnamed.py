from typing import override
from sequence import Sequence
from sequences.geometric import GeometricSequence, identify_geometric_sequence
import stringified

class UnnamedSequence(Sequence):
  """Sequence with terms obtained by mulltiplying the previous ones by a constant value."""
  @override
  def __init__(self, terms: list[float], d_s: GeometricSequence) -> None:
    super().__init__(terms)

    # Sequence of differences between the terms.
    self.d_s = d_s
    # Common differences between the differences and the terms.
    self.d_a = self.a_1 - self.d_s.a_1

  @override
  def function(self) -> str:
    return f"U(n) = {self.d_s.a_1} × {self.d_s.r}⁽ⁿ−¹⁾ {stringified.operation(self.d_a)}"

def identify_unnamed_sequence(terms: list[float]) -> UnnamedSequence | None:
  """Checks if a sequence is unnamed and, if so, constructs UnnamedSequence."""
  # Calculates the differences between the terms.
  d_s = [terms[i] - terms[i - 1] for i in range(1, len(terms))]

  # NOTE: Differences between the terms should form a geometric sequence.
  geometric_sequence = identify_geometric_sequence(d_s)
  return UnnamedSequence(terms, geometric_sequence) if geometric_sequence else None

def compute_unnamed_term(sequence: UnnamedSequence, n: int) -> float:
  """Computes the nth unnamed term for a UnnamedSequence."""
  if n <= len(sequence):
    # Skips unnecessary computation.
    return sequence.terms[n - 1]

  return sequence.d_s.a_1 * (sequence.d_s.r ** (n - 1)) + sequence.d_a
