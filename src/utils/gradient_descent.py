from models import GradientDescentParams, GradientDescentResult

def gradient_descent(params: GradientDescentParams) -> GradientDescentResult:
  learning_rate, weights, dataset, errors = params

  gradient_components = []
  updated_weights = []

  for i in range(len(dataset)):
    entry = dataset[i]
    error = errors[i]
    row = [error * x for x in entry]
    gradient_components.append(row)

  transposed = [list(row) for row in zip(*gradient_components)]

  for i in range(len(weights)):

    updated_weights.append(weights[i] - learning_rate * sum(transposed[i]))

  return GradientDescentResult(updated_weights=updated_weights, gradient_components=gradient_components)