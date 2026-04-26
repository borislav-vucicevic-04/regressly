from models import GradientDescentResult

def gradient_descent(*, learning_rate: float, weights: list[float], dataset:list[list[float]], errors: list[float]) -> GradientDescentResult:
  gradient_components = []
  updated_weights = []

  for i in range(len(dataset)):
    entry = dataset[i]
    error = errors[i]
    row = [error * x for x in entry]
    gradient_components.append(row)

  transposed = [list(row) for row in zip(*gradient_components)]

  for i in range(len(weights)):

    updated_weights.append(weights[i] + learning_rate * sum(transposed[i]))

  return GradientDescentResult(updated_weights=updated_weights, gradient_components=gradient_components)