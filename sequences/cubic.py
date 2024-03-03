from typing import override
from sequences import Sequence
from sequences.quadratic import QuadraticSequence, identify_quadratic_sequence
import stringified

class CubicSequence(Sequence):
  """Sequence with terms obtained by applying a cubic function to n."""
  @override
  def __init__(self, terms: list[float], d_s: QuadraticSequence) -> None:
    super().__init__(terms)

    # Sequence of differences between the terms.
    self.d_s = d_s
    # Difference between the first two terms.
    self.d_s_1 = d_s.a_1
    # Difference between the first two differences of the terms.
    self.d_s_d_1 = d_s.d_s[0]
    # Top-most common difference.
    self.d_d = self.d_s.d_d

    # Constant coefficient of n cubed.
    self.c_a = self.d_d / 6.0
    # Constant coefficient of n squared.
    self.c_b = (self.d_s_d_1 - 12 * self.c_a) / 2.0
    # Constant coefficient of bare n.
    self.c_c = self.d_s_1 - ((7.0 * self.c_a) + (3.0 * self.c_b))
    # Third lonely constant.
    self.c_d = self.a_1 - (self.c_a + self.c_b + self.c_c)

  @override
  def function(self) -> str:
    a__n_cubed_str = stringified.algebraic(self.c_a, "n³", " ")
    b__n_squared_str = stringified.algebraic_operation(self.c_b, "n²", " ")
    c__n_str = stringified.algebraic_operation(self.c_c, "n", " ")
    d_str = stringified.operation(self.c_d)
    return f"C(n) = {a__n_cubed_str}{b__n_squared_str}{c__n_str}{d_str}"

def identify_cubic_sequence(terms: list[float]) -> CubicSequence | None:
  """Checks if a sequence is cubic and, if so, constructs CubicSequence."""
  # Calculates the differences between the terms.
  d_s = [terms[i] - terms[i - 1] for i in range(1, len(terms))]
  # NOTE: Differences between the terms should form a quadratic sequence.
  quadratic_sequence = identify_quadratic_sequence(d_s)
  return CubicSequence(terms, quadratic_sequence) if quadratic_sequence else None

def compute_cubic_term(sequence: CubicSequence, n: int) -> float:
  """Computes the nth cubic term for a CubicSequence."""
  if n <= len(sequence):
    # Skips unnecessary computation.
    return sequence.terms[n - 1]
  # NOTE: an³ + bn² + cn + d
  return (sequence.c_a * n ** 3) + (sequence.c_b * n ** 2) + (sequence.c_c * n) + sequence.c_d
