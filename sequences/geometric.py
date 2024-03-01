def is_sequence_geometric(sequence: list[float]) -> bool:
  return \
    sequence[0] != 0 and \
    all(sequence[i] / sequence[i-1] == sequence[1] / sequence[0] \
      for i in range(2, len(sequence)))

def compute_nth_geometric_term(sequence: list[float], n: int) -> float:
  f = sequence[0]
  r = sequence[1] / f
  return f * (r ** (n - 1))
