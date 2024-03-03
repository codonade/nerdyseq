from typing import override
from sequences import Sequence
import stringified

class ArithmeticSequence(Sequence):
  """Sequence with terms obtained by adding a constant value to the previous ones."""
  @override
  def __init__(self, terms: list[float]) -> None:
    super().__init__(terms)
    # Common difference between the sequence elements.
    self.d = self.a_2 - self.a_1
    # Difference between the first term and the common difference.
    self.d_1 = self.a_1 - self.d

  @override
  def function(self) -> str:
    if self.d == 0:
      # ~ Constant Arithmetic Sequences.
      return f"A(n) = {self.a_1}"
    # ~ Ordinary Arithmetic Sequences.
    return f"A(n) = {stringified.algebraic(self.d, "n")} {stringified.operation(self.d_1)}"

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
  # NOTE: a₁ + d × (n - 1)
  return sequence.a_1 + sequence.d * (n - 1)
