from typing import override
from sequence import Sequence

class FibonacciSequence(Sequence):
  """Sequence with terms obtained by mulltiplying the previous ones by a constant value."""
  @override
  def __init__(self, terms: list[float]) -> None:
    super().__init__(terms)
    # The term before the last.
    self.l_1 = self.terms[-2]
    # The last term.
    self.l_2 = self.terms[-1]

def identify_fibonacci_sequence(terms: list[float]) -> FibonacciSequence | None:
  """Checks if a sequence is fibonacci and, if so, constructs FibonacciSequence."""
  is_fibonacci = True
  for i in range(2, len(terms)):
    if terms[i-1] + terms[i-2] != terms[i]:
      is_fibonacci = False
  return FibonacciSequence(terms) if is_fibonacci else None

def compute_fibonacci_term(sequence: FibonacciSequence, n: int) -> float:
  """Computes the nth fibonacci term for a FibonacciSequence."""
  if n <= len(sequence):
    print("😁 Gotcha! ", end="")
    # Skips unnecessary computation.
    return sequence.terms[n - 1]

  # The last computed nth term.
  a_n = sequence.terms[-1]
  # The two preceding terms.
  p_1, p_2 = sequence.l_1, sequence.l_2

  # NOTE: `n - 1` because we already have an initial computed value.
  for _ in range(len(sequence) - 1, n - 1):
    a_n = p_1 + p_2
    p_1, p_2 = p_2, a_n
  return a_n
