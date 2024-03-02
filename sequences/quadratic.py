from typing import override
from sequence import Sequence
from sequences.arithmetic import identify_arithmetic_sequence

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

  # TODO: Simplify string manipulation.
  @override
  def function(self) -> str:
    an_squared_str = f"{str(self.c_a)}n^2" if self.c_a != 1.0 else "n^2 "
    bn_str = (f"{"+" if self.c_b > 0.0 else "-"} {str(abs(self.c_b))}n " if self.c_b != 1.0 else "+ n ") if self.c_b else ""
    c_str = f"{"+" if self.c_c > 0.0 else "-"} {str(abs(self.c_c))} " if self.c_c else ""
    return f"Q(n) = {an_squared_str}{bn_str}{c_str}"

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

  return (sequence.c_a * n ** 2) + (sequence.c_b * n) + sequence.c_c
