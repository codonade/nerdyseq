from enum import Enum

class Sequence(Enum):
  ARITHMETIC = 0
  GEOMETRIC = 1
  UNKNOWN = -1

# TODO: Switch to floats instead of integers.
def identify_sequence(sequence: list[int]) -> Sequence:
  if len(sequence) < 2:
    # If a sequence has one element, what are we supposed to do?
    print(f"Cannot identify a sequence with one element."); exit(0)

  # ~ Arithmetic Sequence Check.
  arithmetic_diff = sequence[1] - sequence[0]
  # NOTE: This difference should apply for the whole sequence.
  is_arithmetic =\
    all(sequence[i] - sequence[i-1] == arithmetic_diff\
        for i in range(2, len(sequence)))

  # ~ Geometric Sequence Check.
  if sequence[0] != 0:
    geometric_ratio = sequence[1] / sequence[0]
    # NOTE: This ratio should apply for the whole sequence.
    is_geometric =\
      all(sequence[i] / sequence[i-1] == geometric_ratio\
          for i in range(2, len(sequence)))
  else:
    is_geometric = False

  if is_arithmetic:
    return Sequence.ARITHMETIC
  elif is_geometric:
    return Sequence.GEOMETRIC
  else:
    print(f"Couldn't identify the sequence."); exit(0)

# TODO: Switch to floats instead of integers.
def compute_snth_term(sequence: list[int], n: int) -> int:
  sequence_type = identify_sequence(sequence)

  match sequence_type:
    case Sequence.ARITHMETIC:
      a = sequence[0]
      d = sequence[1] - a
      return a + (n - 1) * d
    case Sequence.GEOMETRIC:
      a = sequence[0]
      r = int(sequence[1] / a)
      return a * (r ** (n - 1))
    case Sequence.UNKNOWN:
      # NOTE: Case already handled by `identify_sequence`
      return 0

sequence = [
  # Splits the input by spaces.
  int(string) for string in input().split()]
# The term to compute (nth).
n = int(input())

print(compute_snth_term(sequence, n))
