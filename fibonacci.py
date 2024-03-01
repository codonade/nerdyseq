def is_fibonacci_sequence(sequence: list[float]) -> bool:
  for i in range(2, len(sequence)):
    if sequence[i-1] + sequence[i-2] != sequence[i]:
      return False
  return True

def compute_nth_fibonacci_term(sequence: list[float], n: int) -> float:
  if n == 1:
    return sequence[0]
  elif n == 2:
    return sequence[1]
  else:
    # The current term number, and the nth term.
    # HACK: Starting the loop at 2 - is it the best thing to do?
    i, a = 2, 0.0
    # The two preceding terms, typically starting from 0 and 1.
    b, c = sequence[0], sequence[1]

    # Computes all the terms up to `n` to find `a_n`
    while i < n:
      a = b + c
      b, c = c, a
      i += 1
    return a
