from math import inf
from sequences.arithmetic import compute_arithmetic_term, identify_arithmetic_sequence
from sequences.fibonacci import compute_fibonacci_term, identify_fibonacci_sequence
from sequences.geometric import compute_geometric_term, identify_geometric_sequence
from sequences.quadratic import compute_quadratic_term, identify_quadratic_sequence

def panic(message: str) -> None:
  print(message); exit(0)

terms = [float(string) for string in input("🧐 Enter the first terms: ").split()]
# NOTE: It's impossible to find a pattern with only one term!
if len(terms) < 2:
  panic("😠 Cannot identify sequences with less than 2 terms.")

# HACK: Certain paths may not define `n` so we define it here.
n = None
# The nth term to be computed.
a_n = inf

# ~ Arithmetic Sequences.
arithmetic_sequence = identify_arithmetic_sequence(terms)
if arithmetic_sequence:
  print(f"🥸  {terms} is an arithmetic sequence.")
  n = int(input("🧐 Enter the term number: "))
  a_n = compute_arithmetic_term(arithmetic_sequence, n)
else:

  # ~ Geometric Sequences.
  geometric_sequence = identify_geometric_sequence(terms)
  if geometric_sequence:
    print(f"🥸  {terms} is a geometric sequence.")
    n = int(input("🧐 Enter the term number: "))
    a_n = compute_geometric_term(geometric_sequence, n)
  else:

    # ~ Fibonacci Sequences.
    fibonacci_sequence = identify_fibonacci_sequence(terms)
    if fibonacci_sequence:
      print(f"🥸  {terms} is a fibonacci sequence.")
      n = int(input("🧐 Enter the term number: "))
      a_n = compute_fibonacci_term(fibonacci_sequence, n)
    else:

      # ~ Quadratic Sequences.
      quadratic_sequence = identify_quadratic_sequence(terms)
      if quadratic_sequence:
        print(f"🥸  {terms} is a quadratic sequence.")
        n = int(input("🧐 Enter the term number: "))
        a_n = compute_quadratic_term(quadratic_sequence, n)
      else:

        # ~ Unidentifiable Sequences.
        panic("😟 Couldn't identify this sequence.")

# TODO: Output proper number postfixes (1st, 2nd, 3rd, and nth).
print(f"🥸  The {n}th term for {terms} is {a_n}.")
