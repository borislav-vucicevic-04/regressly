def safe_int(value: any) -> int | None:
  try: return int(value)
  except Exception as e: return None