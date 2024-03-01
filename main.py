from sequences.arithmetic import compute_arithmetic_term, identify_arithmetic_sequence
from sequences.fibonacci import compute_fibonacci_term, identify_fibonacci_sequence
from sequences.geometric import compute_geometric_term, identify_geometric_sequence
from sequences.quadratic import compute_quadratic_term, identify_quadratic_sequence

def panic(message: str) -> None:
  print(message); exit(0)

terms = [float(string) for string in input().split()]
# NOTE: It's impossible to find a pattern with only one term!
if len(terms) < 2:
  panic("😠 Cannot identify sequences with less than 2 terms.")

# ~ Arithmetic Sequences.
arithmetic_sequence = identify_arithmetic_sequence(terms)
if arithmetic_sequence:
  n = int(input())
  print(compute_arithmetic_term(arithmetic_sequence, n))
else:

  # ~ Geometric Sequences.
  geometric_sequence = identify_geometric_sequence(terms)
  if geometric_sequence:
    n = int(input())
    print(compute_geometric_term(geometric_sequence, n))
  else:

    # ~ Fibonacci Sequences.
    fibonacci_sequence = identify_fibonacci_sequence(terms)
    if fibonacci_sequence:
      n = int(input())
      print(compute_fibonacci_term(fibonacci_sequence, n))
    else:

      # ~ Quadratic Sequences.
      quadratic_sequence = identify_quadratic_sequence(terms)
      if quadratic_sequence:
        n = int(input())
        print(compute_quadratic_term(quadratic_sequence, n))
      else:

        # ~ Unidentifiable Sequences.
        panic("😟 Couldn't identify this sequence.")
