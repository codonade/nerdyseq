from enum import Enum
from math import inf

from arithmetic import compute_nth_arithmetic_term, is_arithmetic_sequence
from fibonacci import compute_nth_fibonacci_term, is_fibonacci_sequence
from geometric import compute_nth_geometric_term, is_geometric_sequence

class Sequence(Enum):
  ARITHMETIC = 0
  GEOMETRIC = 1
  FIBONACCI = 2
  UNKNOWN = -1

def identify_sequence(sequence: list[float]) -> Sequence:
  if len(sequence) < 2:
    # If a sequence has one element, what are we supposed to do?
    # TODO: Fix error code number (1, not 0).
    print(f"Cannot identify a sequence with one element."); exit(0)

  if is_arithmetic_sequence(sequence):
    return Sequence.ARITHMETIC
  elif is_geometric_sequence(sequence):
    return Sequence.GEOMETRIC
  elif is_fibonacci_sequence(sequence):
    return Sequence.FIBONACCI
  else:
    # TODO: Fix error code number (1, not 0).
    print(f"Couldn't identify the sequence."); exit(0)

def compute_nths_term(sequence: list[float], n: int) -> float:
  sequence_type = identify_sequence(sequence)

  match sequence_type:
    case Sequence.ARITHMETIC:
      return compute_nth_arithmetic_term(sequence, n)
    case Sequence.GEOMETRIC:
      return compute_nth_geometric_term(sequence, n)
    case Sequence.FIBONACCI:
      return compute_nth_fibonacci_term(sequence, n)
    case Sequence.UNKNOWN:
      # NOTE: Case already handled by `identify_sequence`
      return inf

sequence = [
  # Splits the input by spaces.
  float(string) for string in input().split()]
# The term to compute (nth).
n = int(input())

print(compute_nths_term(sequence, n))
