def hypothesis(weights: list[float], dataset: list[list[float]]) -> list[float]:
  predicted_values: list[float] = []

  for entry in dataset:
    predicted_value = 0;

    for i in range(len(entry)): predicted_value += weights[i] * entry[i]

    predicted_values.append(predicted_value)
  
  return predicted_values