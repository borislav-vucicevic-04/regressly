def to_rounded_str(number: float, precision: int) -> str: 
  return f"{number:.{precision}f}".rstrip("0").rstrip(".")