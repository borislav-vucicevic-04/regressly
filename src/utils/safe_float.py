def safe_float(value: any) -> float | None:
  try: return float(value)
  except Exception as e: return None