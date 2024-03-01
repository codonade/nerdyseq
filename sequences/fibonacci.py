from typing import override
from sequence import Sequence

class FibonacciSequence(Sequence):
  """Sequence with terms obtained by mulltiplying the previous ones by a constant value."""
  # NOTE: Fibonacci sequences don't have any distinct properties.

def identify_fibonacci_sequence(terms: list[float]) -> FibonacciSequence | None:
  """Checks if a sequence is fibonacci and, if so, constructs FibonacciSequence."""
  is_fibonacci = True
  for i in range(2, len(terms)):
    if terms[i-1] + terms[i-2] != terms[i]:
      is_fibonacci = False
  return FibonacciSequence(terms) if is_fibonacci else None

# TODO: Don't compute for `n` less than `sequence.len`
def compute_fibonacci_term(sequence: FibonacciSequence, n: int) -> float:
  """Computes the nth fibonacci term for a FibonacciSequence."""
  if n == 1:
    return sequence.a_1
  elif n == 2:
    return sequence.a_2
  else:
    # The last computed nth term.
    a_n = 0.0
    # The two preceding terms.
    p_1, p_2 = sequence.a_1, sequence.a_2

    # Computes all the terms up to `n` to find `a_n`
    for _ in range(2, n):
      a_n = p_1 + p_2
      p_1, p_2 = p_2, a_n
    return a_n
