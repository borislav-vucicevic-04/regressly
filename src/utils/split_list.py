def split_list(list: list[any], chunk_size: int) -> list[list[any]]:
  if chunk_size <= 0: raise ValueError("The \"chunk_size\" must be a positive number.")
  return [list[i:i + chunk_size] for i in range(0, len(list), chunk_size)]
