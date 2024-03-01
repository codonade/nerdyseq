def is_sequence_arithmetic(sequence: list[float]) -> bool:
  return all(sequence[i] - sequence[i-1] == sequence[1] - sequence[0] \
      for i in range(2, len(sequence)))

def compute_nth_arithmetic_term(sequence: list[float], n: int) -> float:
  f = sequence[0]
  d = sequence[1] - f
  return f + d * (n - 1)
