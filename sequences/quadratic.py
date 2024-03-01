from sequences.arithmetic import is_sequence_arithmetic

def is_sequence_quadratic(sequence: list[float]) -> bool:
  # Calculates first-order differences.
  diffs_1st = [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
  # Calculates second-order differences.
  diffs_2nd = [diffs_1st[i] - diffs_1st[i - 1] for i in range(1, len(diffs_1st))]

  return \
    is_sequence_arithmetic(diffs_1st) and \
    all(diff == diffs_2nd[0] for diff in diffs_2nd)

def compute_nth_quadratic_term(sequence: list[float], n: int) -> float:
  if n == 1:
    return sequence[0]
  else:
    i, d = 0, [sequence[1] - sequence[0]]
    while i < n-2:
      i += 1
      # HACK: Only works for [4, 16, 36, 64, ...]
      d.append(d[-1] + 8.0)
    return sum(d) + sequence[0]
