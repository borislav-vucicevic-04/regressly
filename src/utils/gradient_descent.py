from models import GradientDescentParams, GradientDescentResult
from dataclasses import astuple

def gradient_descent(params: GradientDescentParams) -> GradientDescentResult:
  learning_rate, weights, dataset, errors = astuple(params)
  
  gradient_components = list(map(lambda entry, error: [error * x for x in entry], dataset, errors))
  transposed = [list(row) for row in zip(*gradient_components)]
  gradients = [sum(transposed[i]) / len(transposed[i]) for i in range(len(transposed))]
  updated_weights = list(map(lambda weight, gradient: weight + learning_rate * gradient, weights, gradients))

  return GradientDescentResult(updated_weights=updated_weights, gradient_components=gradient_components)