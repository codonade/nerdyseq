from enum import Enum
from math import inf

from sequences.arithmetic import compute_nth_arithmetic_term, is_sequence_arithmetic
from sequences.fibonacci import compute_nth_fibonacci_term, is_sequence_fibonacci
from sequences.geometric import compute_nth_geometric_term, is_sequence_geometric
from sequences.quadratic import compute_nth_quadratic_term, is_sequence_quadratic

class Sequence(Enum):
  ARITHMETIC = 0
  GEOMETRIC = 1
  QUADRATIC = 2
  FIBONACCI = 3

def identify_sequence(sequence: list[float]) -> Sequence:
  if len(sequence) < 2:
    # If a sequence has one element, what are we supposed to do?
    print(f"Cannot identify a sequence with one element."); exit(1)

  if is_sequence_arithmetic(sequence):
    return Sequence.ARITHMETIC
  elif is_sequence_geometric(sequence):
    return Sequence.GEOMETRIC
  elif is_sequence_fibonacci(sequence):
    return Sequence.FIBONACCI
  elif is_sequence_quadratic(sequence):
    return Sequence.QUADRATIC
  else:
    print(f"Couldn't identify the sequence."); exit(1)

def compute_nths_term(sequence: list[float], n: int) -> float:
  sequence_type = identify_sequence(sequence)

  match sequence_type:
    case Sequence.ARITHMETIC:
      return compute_nth_arithmetic_term(sequence, n)
    case Sequence.GEOMETRIC:
      return compute_nth_geometric_term(sequence, n)
    case Sequence.QUADRATIC:
      return compute_nth_quadratic_term(sequence, n)
    case Sequence.FIBONACCI:
      return compute_nth_fibonacci_term(sequence, n)

sequence = [
  # Splits the input by spaces.
  float(string) for string in input().split()]
# The term to compute (nth).
n = int(input())

print(compute_nths_term(sequence, n))
