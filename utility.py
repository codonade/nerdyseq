def postfix(number: int) -> str:
  """Postfixes numbers correctly (1st, 2nd, 3rd, and nth)."""
  digit = int(str(number)[len(str(number)) - 1])
  if digit == 1 and (number < 4 or number > 20):
    return f"{number}st"
  elif digit == 2 and (number < 4 or number > 20):
    return f"{number}nd"
  elif digit == 3 and (number < 4 or number > 20):
    return f"{number}rd"
  else:
    return f"{number}th"
