def calculate_errors(real_values: list[float], predicted_values: list[float]) -> list[float]:
  errors = []

  for i in range(len(real_values)): errors.append(real_values[i] - predicted_values[i])

  return errors