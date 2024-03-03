from typing import override
from sequences import Sequence
from sequences.arithmetic import identify_arithmetic_sequence
import stringified

class QuadraticSequence(Sequence):
  """Sequence with terms obtained by applying a quadratic function to n."""
  @override
  def __init__(self, terms: list[float], d_s: list[float], d_d: float) -> None:
    super().__init__(terms)
    # Differences between the terms.
    self.d_s = d_s
    # Difference between the first two terms.
    self.d_1 = d_s[0]
    # Common difference between the differences of the terms.
    self.d_d = d_d

    # Constant coefficient of n squared.
    self.c_a = self.d_d / 2.0
    # Constant coefficient of bare n.
    self.c_b = self.d_1 - 3 * self.c_a
    # Third lonely constant.
    self.c_c = self.a_1 - (self.c_a + self.c_b)

  @override
  def function(self) -> str:
    a__n_squared_str = stringified.algebraic(self.c_a, "n²", " ")
    b__n_str = stringified.algebraic_operation(self.c_b, "n", " ")
    c_str = stringified.operation(self.c_c)
    return f"Q(n) = {a__n_squared_str}{b__n_str}{c_str}"

def identify_quadratic_sequence(terms: list[float]) -> QuadraticSequence | None:
  """Checks if a sequence is quadratic and, if so, constructs QuadraticSequence."""
  # Calculates the differences between the terms.
  d_s = [terms[i] - terms[i - 1] for i in range(1, len(terms))]
  # Calculates difference between the differences of the terms.
  d_d = [d_s[i] - d_s[i - 1] for i in range(1, len(d_s))]

  is_quadratic = \
    identify_arithmetic_sequence(d_s) and \
      all(d == d_d[0] for d in d_d)
  return QuadraticSequence(terms, d_s, d_d[0]) if is_quadratic else None

def compute_quadratic_term(sequence: QuadraticSequence, n: int) -> float:
  """Computes the nth quadratic term for a QuadraticSequence."""
  if n <= len(sequence):
    # Skips unnecessary computation.
    return sequence.terms[n - 1]
  # NOTE: an² + bn + c
  return (sequence.c_a * n ** 2) + (sequence.c_b * n) + sequence.c_c
