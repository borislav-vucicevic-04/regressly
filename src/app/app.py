import customtkinter as ctk

from .app_ui import AppUI
from constants.constants import Colors
from tkinter import messagebox
from utils import *
from models import CreateMseStepsParams, GradientDescentParams
from components import PrintDialog, PrecisionDialog, GDSettingsDialog

class App(AppUI):
  def __init__(self, master=None):
    super().__init__(master)
  
  def run(self):
    self.mainwindow.mainloop()
  
  def change_precision(self, event):
    # Open the dialog to change the precision
    dialog = PrecisionDialog(self.mainwindow)
    dialog.showDialog()
    newPrecision = dialog.getPrecision();

    # GUARDING CLAUSE: If user canceled, exit the method
    if newPrecision is None: return

    # OTHERWISE: Change the precision
    self.precision_section.set_display(f"Current precision: {newPrecision}")
    self.weights_section.apply_precision(newPrecision)
    self.dataset_section.apply_precision(newPrecision)
    self.precision = newPrecision

  def decrease_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 1: return

    # Otherwise, continue the execution
    self.weights_section.remove_column_at(self.input_size)
    self.dataset_section.remove_column_at(self.input_size)
    self.input_size -= 1

  def increase_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 10: return

    # Otherwise, continue the execution
    self.input_size += 1
    self.weights_section.add_column_at(index=self.input_size, header=f"w{self.input_size}")
    self.dataset_section.add_column_at(index=self.input_size, header=f"x{self.input_size}")

  def calculate_mse(self, event):
    generate_pdf = messagebox.askyesnocancel("Calculate mean squared error", "Do you want to generate the PDF file with steps on how to find the solution as well?")

    # GUARDING CLAUSE: If user presses cancel button, it means we changed his mind and we should exit the method
    if generate_pdf is None:
      return

    # Otherwise continue with the calculation
    weights = self.weights_section.get_weights()
    dataset = self.dataset_section.get_inputs()
    real_values = self.dataset_section.get_outputs()
    predicted_values = hypothesis(weights, dataset)
    errors = calculate_errors(real_values, predicted_values)
    mse = mean_squared_error(errors)

    if generate_pdf:
      dialog = PrintDialog(self.mainwindow)
      dialog.showDialog()
      print_settings = dialog.getPrintSettings()

      if print_settings is not None:
        create_mse_steps(CreateMseStepsParams(
          precision=self.precision,
          weights=weights,
          dataset=dataset,
          real_values=real_values,
          predicted_values=predicted_values,
          errors=errors,
          mse=mse,
          print_settings=print_settings
        ))
    else:
      messagebox.showinfo("Calculated mean squared error", f"Mean squared error for this dataset is {mse}")

  def apply_gradient_descent(self, event):
    generate_pdf = messagebox.askyesnocancel("Apply gradient descent", "Do you want to generate the PDF file with steps on how to find the solution as well?")

    # GUARDING CLAUSE: If user presses cancel button, it means we changed his mind and we should exit the method
    if generate_pdf is None:
      return
    
    dialog = GDSettingsDialog(master=self.mainwindow);
    dialog.showDialog()
    gdsettings = dialog.result;

    
    if gdsettings is None: return;

    # Otherwise continue with the calculation
    weights = self.weights_section.get_weights()
    dataset = self.dataset_section.get_inputs()
    real_values = self.dataset_section.get_outputs()
    gradient_descent_result = gradient_descent(GradientDescentParams(
      learning_rate=gdsettings.learning_rate,
      batch_size=gdsettings.batch_size,
      weights=weights, 
      real_values=real_values, 
      dataset=dataset
    ))

    messagebox.showinfo("Applying gradient descent", f"Updated weights: {", ".join([f"{weight: .{self.precision}f}" for weight in gradient_descent_result.updated_weights])}")