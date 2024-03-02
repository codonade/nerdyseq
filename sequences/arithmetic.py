from typing import override
from sequence import Sequence

class ArithmeticSequence(Sequence):
  """Sequence with terms obtained by adding a constant value to the previous ones."""
  @override
  def __init__(self, terms: list[float]) -> None:
    super().__init__(terms)
    # Common difference between the sequence elements.
    self.d = self.a_2 - self.a_1

  @override
  def function(self) -> str:
    # Difference between the first term and the common difference.
    d_1 = self.a_1 - self.d
    if not d_1:
      if self.d == 1:
        return "A(n) = n"
      return f"A(n) = {self.d}n"

    if self.d == 1:
      return f"A(n) = n {"+" if d_1 > 0 else "-"} {abs(d_1)}"
    return f"A(n) = {self.d}n {"+" if d_1 > 0 else "-"} {abs(d_1)}"

def identify_arithmetic_sequence(terms: list[float]) -> ArithmeticSequence | None:
  """Checks if a sequence is arithmetic and, if so, constructs ArithmeticSequence."""
  is_arithmetic = \
    all(terms[i] - terms[i-1] == terms[1] - terms[0] \
      for i in range(2, len(terms)))
  return ArithmeticSequence(terms) if is_arithmetic else None

def compute_arithmetic_term(sequence: ArithmeticSequence, n: int) -> float:
  """Computes the nth arithmetic term for an ArithmeticSequence."""
  if n <= len(sequence):
    # Skips unnecessary computation.
    return sequence.terms[n - 1]

  return sequence.a_1 + sequence.d * (n - 1)
