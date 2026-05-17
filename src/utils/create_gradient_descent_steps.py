from models import CreateGradientDescentStepsParams, MiniBatchGradientDescentResult, EpochResult
from dataclasses import astuple, asdict
from constants import HtmlTemplates
from utils.create_pdf import create_pdf

def create_gradient_descent_steps(params: CreateGradientDescentStepsParams):
  vector_of_weights = _create_vector_of_weights(weights=params.weights, precision=params.precision)
  hypothesis = _create_hypothesis(weights=params.weights, precision=params.precision)
  dataset = _create_dataset(dataset=params.dataset, real_values=params.real_values, precision=params.precision)
  epochs_sections = _create_epoch_sections(epoch_results=params.gradient_descent_result.epoch_results, learning_rate=params.learning_rate, precision=params.precision)
  final_result = _create_vector_of_weights(weights=params.gradient_descent_result.updated_weights, precision=params.precision)
  
  contents = HtmlTemplates.GRADIENT_DESCENT_STEPS
  contents = contents.replace("$weights", vector_of_weights)
  contents = contents.replace("$function_formula", hypothesis)
  contents = contents.replace("$dataset_table", dataset)
  contents = contents.replace("$learning_rate", str(params.learning_rate))
  contents = contents.replace("$batch_size", str(params.batch_size))
  contents = contents.replace("$epochs", str(params.epochs))
  contents = contents.replace("$epoch_sections", epochs_sections)
  contents = contents.replace("$final_result", final_result)
  contents = contents.replace("$page_orientation", params.print_settings.page_orientation)
  contents = contents.replace("$page_size", params.print_settings.page_size)
  contents = contents.replace("$margin_left", f"{params.print_settings.margin_left}{params.print_settings.units}")
  contents = contents.replace("$margin_top", f"{params.print_settings.margin_top}{params.print_settings.units}")
  contents = contents.replace("$margin_right", f"{params.print_settings.margin_right}{params.print_settings.units}")
  contents = contents.replace("$margin_bottom", f"{params.print_settings.margin_bottom}{params.print_settings.units}")
  create_pdf(contents)

def _create_vector_of_weights(weights: list[float], precision: float):
  rounded = list(map(lambda val: f"{val: .{precision}f}", weights))
  return ", ".join(rounded)

def _create_hypothesis(weights: list[float], precision: float):
  result = ""

  if weights[0] == 1: result = "x<sub>0</sub>"
  elif weights[0] == -1: result = f"- x<sub>0</sub>"
  elif weights[0] == 0: result = ""
  else: result = f"{weights[0]: .{precision}f} • x<sub>0</sub>"

  for i in range(1, len(weights)):
    if weights[i] == 1: result += f"+ x<sub>{i}</sub>"
    elif weights[i] == -1: result += f"- x<sub>{i}</sub>"
    elif weights[i] == 0: result += ""
    else: result += f"+ {weights[i]: .{precision}f} • x<sub>{i}</sub>"

  return result

def _create_dataset(dataset: list[list[float]], real_values: float, precision: float):
  table = "<table>"

  # Generating the header rows
  table += "<thead><tr>"
  for i in range(len(dataset[0])): table += f"<th>x<sub>{i}</sub></th>"
  table += "<th>y</th>"
  table += "</tr></thead>"

  # Generating body
  table += "<tbody>"
  
  for i in range(len(dataset)):
    table += "<tr>"
    for j in range(len(dataset[i])): table += f"<td>{dataset[i][j]: .{precision}f}</td>"
    table += f"<td>{real_values[i]: .{precision}f}</td>"
    table += "</tr>"

  table += "</tbody>"
  table += "</table>"

  return table

def _create_epoch_sections(epoch_results: list[EpochResult], learning_rate: float, precision: float):
  content = "";

  for i in range(len(epoch_results)):
    section = f"<h2>Epoch {i + 1}</h2>"
    for j in range(len(epoch_results[i].batch_results)):
      batch_result = epoch_results[i].batch_results[j]
      section += _create_batch_section(j + 1, batch_result, learning_rate, precision)
    
    content += section
  
  return content

def _create_batch_section(batch_number: int, batch_result: MiniBatchGradientDescentResult, learning_rate: float, precision: float):
  section = f"<h3>Batch {batch_number}</h3>"
  section += f"<p><strong>Initial weights</strong>: {_create_vector_of_weights(batch_result.weights, precision)}</p>"
  # creating mini-batch
  section += "<table>"
  # Generating the header rows
  section += "<thead><tr>"
  for i in range(len(batch_result.batch[0])): section += f"<th>x<sub>{i}</sub></th>"

  section += "<th>y</th>"
  section += "<th>h</th>"
  section += "<th>δ (y - h)</th>"
  for i in range(len(batch_result.batch[0])): section += f"<th>x<sub>{i}</sub> • δ<sub>{i}</sub></th>"
  section += "</tr></thead>"
  # Generating body
  section += "<tbody>"
  for i in range(len(batch_result.batch)):
    section += "<tr>"
    for j in range(len(batch_result.batch[i])): section += f"<td>{batch_result.batch[i][j]: .{precision}f}</td>"
    section += f"<td>{batch_result.batch_real_values[i]: .{precision}f}</td>"
    section += f"<td>{batch_result.batch_predicted_values[i]: .{precision}f}</td>"
    section += f"<td>{batch_result.batch_errors[i]: .{precision}f}</td>"
    for j in range(len(batch_result.batch_gradient_components[i])): section += f"<td>{batch_result.batch_gradient_components[i][j]: .{precision}f}</td>"
    section += "</tr>"
  section += "</tbody>"
  section += "</table>"

  # adding updated weights
  for i in range(len(batch_result.updated_weights)):
    section += f"<p> w<sub>i</sub> ←  {batch_result.weights[i]: .{precision}f} + {learning_rate} • ({batch_result.batch_gradients[i]: .{precision}f}) = {batch_result.updated_weights[i]: .{precision}f}</p>"

  section += f"<p><strong>Updated weights</strong>: {_create_vector_of_weights(batch_result.updated_weights, precision)}</p>"

  return section;