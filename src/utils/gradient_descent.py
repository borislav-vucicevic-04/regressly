from models import GradientDescentParams, GradientDescentResult, MiniBatchGradientDescentParams, MiniBatchGradientDescentResult, EpochResult
from dataclasses import astuple
from utils import split_list, hypothesis, calculate_errors

def gradient_descent(params: GradientDescentParams) -> GradientDescentResult:
  learning_rate, batch_size, epochs, weights, dataset, real_values = astuple(params)

  batches: list[list[float]] = split_list(dataset, batch_size)
  batch_number = len(batches)
  batch_real_values: list[float] = split_list(real_values, batch_size)
  updated_weights = weights
  epoch_results: list[EpochResult] = []

  for j in range(epochs):
    batch_results: list[MiniBatchGradientDescentResult] = []

    for i in range(batch_number):
      mini_batch_params = MiniBatchGradientDescentParams(
        learning_rate=learning_rate,
        weights=updated_weights,
        batch=batches[i],
        batch_real_values=batch_real_values[i]
      )
      
      mini_batch_result = _minibatch_gradient_descent(mini_batch_params)
      updated_weights = mini_batch_result.updated_weights
      batch_results.append(mini_batch_result)
    
    epoch_results.append(EpochResult(updated_weights=updated_weights, batch_results=batch_results))

  return GradientDescentResult(updated_weights=updated_weights, epoch_results=epoch_results)

def _minibatch_gradient_descent(params: MiniBatchGradientDescentParams) -> MiniBatchGradientDescentResult:
  learning_rate, weights, batch, batch_real_values = astuple(params)

  batch_predicted_values = hypothesis(weights=weights, dataset=batch)
  batch_errors = calculate_errors(real_values=batch_real_values, predicted_values=batch_predicted_values)
  
  batch_gradient_components = list(map(lambda entry, error: [error * x for x in entry], batch, batch_errors))
  transposed = [list(row) for row in zip(*batch_gradient_components)]
  gradients = [sum(transposed[i]) / len(transposed[i]) for i in range(len(transposed))]
  updated_weights = list(map(lambda weight, gradient: weight + learning_rate * gradient, weights, gradients))

  return MiniBatchGradientDescentResult(
    weights=weights,
    batch=batch,
    batch_real_values=batch_real_values,
    batch_predicted_values=batch_predicted_values,
    batch_errors=batch_errors,
    updated_weights=updated_weights,
    batch_gradients=gradients,
    batch_gradient_components=batch_gradient_components
  )