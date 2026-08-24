import customtkinter as ctk

from .app_ui import AppUI
from constants.constants import Colors
from tkinter import messagebox
from utils import *
from models import CreateMseStepsParams, GradientDescentParams, CreateGradientDescentStepsParams
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

    # GUARDING CLAUSE: 
    # If user canceled, exit the method
    if newPrecision is None: return

    # OTHERWISE: 
    # Change the precision
    self.precision_section.set_display(f"Current precision: {newPrecision}")
    self.weights_section.apply_precision(newPrecision)
    self.dataset_section.apply_precision(newPrecision)
    self.precision = newPrecision

  def decrease_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 1: return

    # OTHERWISE:
    # continue removing the columns from sheets
    self.weights_section.remove_column_at(self.input_size)
    self.dataset_section.remove_column_at(self.input_size)
    self.input_size -= 1

  def increase_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 10: return

    # OTHERWISE:
    # continue adding columns to sheets
    self.input_size += 1
    self.weights_section.add_column_at(index=self.input_size, header=f"w{self.input_size}")
    self.dataset_section.add_column_at(index=self.input_size, header=f"x{self.input_size}")

  def calculate_mse(self, event):
    generate_pdf = messagebox.askyesnocancel("Calculate mean squared error", "Do you want to generate the PDF file with steps on how to find the solution as well?")

    # GUARDING CLAUSE: 
    # If value is none, it means user pressed the Cancel button,
    # so we immediatelly exit the method
    if generate_pdf is None:
      return

    # OTHERWISE:
    # We continue with the calculation
    weights = self.weights_section.get_weights()
    dataset = self.dataset_section.get_inputs()
    real_values = self.dataset_section.get_outputs()
    predicted_values = hypothesis(weights, dataset)
    errors = calculate_errors(real_values, predicted_values)
    mse = mean_squared_error(errors)

    # GUARDING CLAUSE:
    # If user does not want to generate a pdf report, display the value in the messagebox
    # and immediately exit the function
    if not generate_pdf:
      messagebox.showinfo("Calculated mean squared error", f"Mean squared error for this dataset is {to_rounded_str(mse, self.precision)}")
      return

    # OTHERWISE:
    # Continue preparing the the printing settings
    dialog = PrintDialog(self.mainwindow)
    dialog.showDialog()
    print_settings = dialog.getPrintSettings()

    # We have to check if print settings are not None.
    # They will be none only when user has pressed the Cancel button
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

  def apply_gradient_descent(self, event):
    generate_pdf = messagebox.askyesnocancel("Apply gradient descent", "Do you want to generate the PDF file with steps on how to find the solution as well?")

    # GUARDING CLAUSE: 
    # When value is None, means user pressed the Cancel button, and we have to exit the method.
    if generate_pdf is None:
      return

    # OTHERWISE:
    # Continue execution.
    dialog = GDSettingsDialog(master=self.mainwindow);
    dialog.showDialog()
    gdsettings = dialog.result;

    # GUARDING CLAUSE:
    # If the value is none, user pressed the Cancel button, so we immediatelly exit the method
    if gdsettings is None: return;

    # OTHERWISE:
    # We continue with the calculation
    weights = self.weights_section.get_weights()
    dataset = self.dataset_section.get_inputs()
    real_values = self.dataset_section.get_outputs()
    gradient_descent_result = gradient_descent(GradientDescentParams(
      learning_rate=gdsettings.learning_rate,
      batch_size=gdsettings.batch_size,
      epochs=gdsettings.epochs,
      weights=weights, 
      real_values=real_values, 
      dataset=dataset
    ))

    # GUARDING CLAUSE:
    # If user does not want to generate a pdf report, display the value in the messagebox
    # and immediately exit the function
    if not generate_pdf:
      messagebox.showinfo("Applying gradient descent", f"Updated weights: {", ".join([f"{weight: .{self.precision}f}" for weight in gradient_descent_result.updated_weights])}")
      return

    # OTHERWISE:
    # Continue executing the function
    print_dialog = PrintDialog(self.mainwindow)
    print_dialog.showDialog()
    print_settings = print_dialog.getPrintSettings()

    # GUARDING CLAUSE:
    # We have to check if the print settings are not None.
    # They are none only when the user has pressed the Cancel button.
    if print_settings is None:
      return

    # OTHERWISE:
    # Create the file
    create_gradient_descent_steps(CreateGradientDescentStepsParams(
      precision=self.precision,
      weights=weights,
      dataset=dataset,
      real_values=real_values,
      learning_rate=gdsettings.learning_rate,
      batch_size=gdsettings.batch_size,
      epochs=gdsettings.epochs,
      gradient_descent_result=gradient_descent_result,
      print_settings=print_settings
    ))
