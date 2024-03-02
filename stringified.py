def operation(constant: float, spacings: str = "") -> str:
  """Stringifies an operation (addition, subtraction) for a given constant."""
  if not constant:
    # NOTE: No need to stringify an operation on 0.
    return ""
  return f"{"+" if constant > 0.0 else "-"} {abs(constant)}{spacings}"

def algebraic(constant: float, variable: str, spacings: str = "") -> str:
  """Stringifies a given algebraic term."""
  if not constant:
    return ""
  elif constant == 1.0:
    return f"{variable}{spacings}"
  elif constant == -1.0:
    return f"-{variable}{spacings}"
  else:
    return f"{constant}{variable}{spacings}"

def algebraic_operation(constant: float, variable: str, spacings: str = "") -> str:
  """Stringifies an operation on a given algebraic term."""
  if not constant:
    # NOTE: No need to stringify an operation on 0.
    return ""
  elif constant == 1.0:
    return f"+ {variable}{spacings}"
  elif constant == -1.0:
    return f"- {variable}{spacings}"
  else:
    return f"{"+" if constant > 0.0 else "-"} {abs(constant)}{variable}{spacings}"
