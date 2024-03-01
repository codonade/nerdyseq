from typing import override
from sequence import Sequence
from sequences.arithmetic import identify_arithmetic_sequence

class QuadraticSequence(Sequence):
  """Sequence with terms obtained by applying a quadratic function to n."""
  @override
  def __init__(self, terms: list[float], d_s: list[float], d_d: float) -> None:
    super().__init__(terms)
    # The differences between the terms.
    self.d_s = d_s
    # The constant difference between the differences of the terms.
    self.d_d = d_d

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
    print("😁 Gotcha! ", end="")
    # Skips unnecessary computation.
    return sequence.terms[n - 1]

  # The differences between the terms.
  d_s = sequence.d_s
  # NOTE: `n - 1` because we already have an initial computed value.
  for _ in range(len(sequence) - 1, n - 1):
    d_s.append(d_s[-1] + sequence.d_d)
  return sum(d_s) + sequence.a_1
