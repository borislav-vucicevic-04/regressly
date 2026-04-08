def mean_squared_error(errors: list[float]) -> float:
  mse = 0

  for error in errors: mse += error * error

  return mse