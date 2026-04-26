from models import CreateMseStepsParams
from utils.create_pdf import create_pdf
from constants.constants import HtmlTemplates

def create_mse_steps(params: CreateMseStepsParams):
  function_formula = create_weights(params.weights, params.precision)
  dataset_table = create_dataset_table(params)
  contents = HtmlTemplates.MSE_STEPS
  contents = contents.replace("$weights", f"({", ".join([f"{val: .{params.precision}f}" for val in params.weights])})")
  contents = contents.replace("$function_formula", function_formula)
  contents = contents.replace("$dataset_table", dataset_table)
  contents = contents.replace("$mse_result", f"{params.mse: .{params.precision}f}")
  contents = contents.replace("$page_orientation", params.print_settings.page_orientation)
  contents = contents.replace("$page_size", params.print_settings.page_size)
  contents = contents.replace("$margin_left", f"{params.print_settings.margin_left}{params.print_settings.units}")
  contents = contents.replace("$margin_top", f"{params.print_settings.margin_top}{params.print_settings.units}")
  contents = contents.replace("$margin_right", f"{params.print_settings.margin_right}{params.print_settings.units}")
  contents = contents.replace("$margin_bottom", f"{params.print_settings.margin_bottom}{params.print_settings.units}")
  create_pdf(contents)


def create_weights(weights: list[float], precision: float):
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

def create_dataset_table(params: CreateMseStepsParams):
  table = "<table>"

  # Generating the header rows
  table += "<thead><tr>"

  for i in range(len(params.dataset[0])): table += f"<th>x<sub>{i}</sub></th>"

  table += "<th>y</th>"
  table += "<th>h</th>"
  table += "<th>δ (y - h)</th>"
  table += "<th>δ<sup>2</sup> (y - h)<sup>2</sup></th>"

  table += "</tr></thead>"

  # Generating body
  table += "<tbody>"
  
  for i in range(len(params.dataset)):
    table += "<tr>"

    for j in range(len(params.dataset[i])): table += f"<td>{params.dataset[i][j]: .{params.precision}f}</td>"
    table += f"<td>{params.real_values[i]: .{params.precision}f}</td>"
    table += f"<td>{params.predicted_values[i]: .{params.precision}f}</td>"
    table += f"<td>{params.errors[i]: .{params.precision}f}</td>"
    table += f"<td>{params.errors[i] * params.errors[i]: .{params.precision}f}</td>"

    table += "</tr>"

  table += "</tbody>"
  table += "</table>"

  return table