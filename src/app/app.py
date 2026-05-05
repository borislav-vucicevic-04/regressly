import customtkinter as ctk

from .app_ui import AppUI
from constants.constants import Colors
from tkinter import messagebox
from utils import *
from models import CreateMseStepsParams
from components import PrintDialog, PrecisionDialog

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
    
    learning_rate = 0

    # Forcing user to choose learnign rate
    while True:
      learning_rate = self.__get_learning_rate__()
      # Exit method if user clicked Cancel (cancellation indicated by None value)
      if learning_rate is None: return;
      # break the loop if user submitted valid value
      elif learning_rate >= 0: break;
      # Otherwise show error
      else: messagebox.showerror("Learning rate error", "The learning rate must be a number greather than or equal to 0.")

    # Otherwise continue with the calculation
    weights = self.weights_section.get_weights()
    dataset = self.dataset_section.get_inputs()
    real_values = self.dataset_section.get_outputs()
    predicted_values = hypothesis(weights, dataset)
    errors = calculate_errors(real_values, predicted_values)
    gradient_descent_result = gradient_descent(
      learning_rate=learning_rate, 
      weights=weights, 
      errors=errors, 
      dataset=dataset
    )

    messagebox.showinfo("Applying gradient descent", f"Updated weights: {", ".join([f"{weight: .{self.precision}f}" for weight in gradient_descent_result.updated_weights])}")
  
  def __get_learning_rate__(self) -> float | None:
    # 1. Create the dialog
    dialog = ctk.CTkInputDialog(text="Please provide value for learning rate.", title="Learning rate")
    
    # 2. Force dimensions update for centering
    dialog.update_idletasks()
    
    # 3. Calculate center position relative to self.mainwindow
    main_x = self.mainwindow.winfo_rootx()
    main_y = self.mainwindow.winfo_rooty()
    main_w = self.mainwindow.winfo_width()
    main_h = self.mainwindow.winfo_height()
    
    dlg_w = dialog.winfo_width()
    dlg_h = dialog.winfo_height()
    
    x = main_x + (main_w // 2) - (dlg_w // 2)
    y = main_y + (main_h // 2) - (dlg_h // 2)
    
    # 4. Position dialog and capture input
    dialog.geometry(f"+{x}+{y}")
    raw_input = dialog.get_input()
    
    # 5. Logic: None = Cancel, -1 = Error, int = Success
    if raw_input is None: return None
      
    try:
      value = float(raw_input)
      if value >= 0: return value
      else: return -1 # Out of range
    except Exception as e:
      return -1 # Not a number