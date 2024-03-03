import math
import humanize.number

from sequences.arithmetic import compute_arithmetic_term, identify_arithmetic_sequence
from sequences.cubic import compute_cubic_term, identify_cubic_sequence
from sequences.fibonacci import compute_fibonacci_term, identify_fibonacci_sequence
from sequences.geometric import compute_geometric_term, identify_geometric_sequence
from sequences.quadratic import compute_quadratic_term, identify_quadratic_sequence
from sequences.unnamed import compute_unnamed_term, identify_unnamed_sequence

def panic(message: str) -> None:
  print(message); exit(0)

terms = [float(string) for string in input("🧐 Enter the first terms: ").split()]
# NOTE: It's impossible to find a pattern with only one term!
if len(terms) < 2:
  panic("😠 Cannot identify sequences with less than 2 terms.")

# HACK: Certain paths may not define `n` so we define it here.
n = -1
# Nth term to be computed.
a_n = math.inf

# ~ Arithmetic Sequences.
arithmetic_sequence = identify_arithmetic_sequence(terms)
if arithmetic_sequence:
  print(f"🥸  {terms} is an arithmetic sequence.")
  print(f"🥸  {arithmetic_sequence.function()}")
  n = int(input("🧐 Enter the term number: "))
  a_n = compute_arithmetic_term(arithmetic_sequence, n)
else:

  # ~ Geometric Sequences.
  geometric_sequence = identify_geometric_sequence(terms)
  if geometric_sequence:
    print(f"🥸  {terms} is a geometric sequence.")
    print(f"🥸  {geometric_sequence.function()}")
    n = int(input("🧐 Enter the term number: "))
    a_n = compute_geometric_term(geometric_sequence, n)
  else:

    # ~ Unnamed Sequences.
    unnamed_sequence = identify_unnamed_sequence(terms)
    if unnamed_sequence:
      print(f"🥸  {terms} is a unnamed sequence.")
      print(f"🥸  {unnamed_sequence.function()}")
      n = int(input("🧐 Enter the term number: "))
      a_n = compute_unnamed_term(unnamed_sequence, n)
    else:

      # ~ Fibonacci Sequences.
      fibonacci_sequence = identify_fibonacci_sequence(terms)
      if fibonacci_sequence:
        print(f"🥸  {terms} is a fibonacci sequence.")
        print(f"🥸  {fibonacci_sequence.function()}")
        n = int(input("🧐 Enter the term number: "))
        a_n = compute_fibonacci_term(fibonacci_sequence, n)
      else:

        # ~ Quadratic Sequences.
        quadratic_sequence = identify_quadratic_sequence(terms)
        if quadratic_sequence:
          print(f"🥸  {terms} is a quadratic sequence.")
          print(f"🥸  {quadratic_sequence.function()}")
          n = int(input("🧐 Enter the term number: "))
          a_n = compute_quadratic_term(quadratic_sequence, n)
        else:

          # ~ Cubic Sequences.
          cubic_sequence = identify_cubic_sequence(terms)
          if cubic_sequence:
            print(f"🥸  {terms} is a cubic sequence.")
            print(f"🥸  {cubic_sequence.function()}")
            n = int(input("🧐 Enter the term number: "))
            a_n = compute_cubic_term(cubic_sequence, n)
          else:

            # ~ Unidentifiable Sequences.
            panic("😟 Couldn't identify this sequence.")

# ~ Conclusion.
print(f"🥸  The {humanize.number.ordinal(n)} term for {terms} is {a_n}.")
