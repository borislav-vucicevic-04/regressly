import customtkinter as ctk

from .app_ui import AppUI
from constants.constants import Colors
from tkinter import messagebox, simpledialog
from utils import *
from models import CreateMseStepsParams
from components import PrintDialog

class App(AppUI):
  def __init__(self, master=None):
    super().__init__(master)
  
  def run(self):
    self.mainwindow.mainloop()
  
  def change_precision(self, event):
    proceed = messagebox.askokcancel(
      title="Change the precision",
      message="Please keep in mind that this will round all weights and numbers in the dataset, and that this action is irreversible. To reverse it, you will need to change the precision again and manually retype the data!",
      icon="warning"
    )

    # GUARDING CLAUSE: if user changed the mind and pressed cancel, exit the method immediately
    if not proceed: return

    #OTHERWISE: Change the precision
    newPrecision = 0;

    while True:
      result = self.__get_precision__()
      
      if result is None: break # Stop if user hits Cancel
      elif result == -1: messagebox.showerror("Error", "You must enter a number between 0 and 5.")
      else:
        self.precision = result
        break # Success
    
    self.precision_section.set_display(f"Current precision: {self.precision}")
    self.__apply_precision__()

  def decrease_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 1: return

    # Otherwise, continue the execution
    self.weights_sheet.delete_columns(columns=[self.input_size])
    self.dataset_sheet.delete_columns(columns=[self.input_size])
    self.input_size -= 1
    self.mainwindow.mainloop()
  
  def increase_input_size(self, event):
    # GUARDING CLAUSE:
    # If the input size is equal to one, exit the method
    if self.input_size == 10: return

    # Otherwise, continue the execution
    dataset_filler_values = [f"{0: .{self.precision}f}"] * self.dataset_sheet.total_rows()
    self.input_size += 1
    self.weights_sheet.headers([f"w{i}" for i in range(self.input_size + 1)])
    self.weights_sheet.insert_column(column=[f"{0: .{self.precision}f}"], idx=self.input_size)
    self.dataset_sheet.headers([f"x{i}" for i in range(self.input_size + 1)] + ["y"])
    self.dataset_sheet.insert_column(column=dataset_filler_values, idx=self.input_size)

  def validate_cell_entry(self, event):
    try:
      value = float(event.value) 
      return f"{value: .{self.precision}f}"
    except ValueError:
      return None
    
  def add_row(self, event):
    new_row_idx = self.dataset_sheet.get_total_rows()
    dataset_filler_values = [f"{1: .{self.precision}f}"] + ([f"{0: .{self.precision}f}"] * (self.dataset_sheet.total_columns() - 1))
    self.dataset_sheet.insert_row(row=dataset_filler_values, idx=self.dataset_sheet.total_rows())
    self.dataset_sheet.readonly_cells(row=new_row_idx, column=0, readonly=True)
  
  def delete_rows(self, event):
    selected_rows = self.dataset_sheet.get_selected_rows()

    if selected_rows:
      self.dataset_sheet.delete_rows(rows=selected_rows)
    else:
      messagebox.showerror(title="Error while deleting rows", message="You should select at least one row.")

  def calculate_mse(self, event):
    generate_pdf = messagebox.askyesnocancel("Calculate mean squared error", "Do you want to generate the PDF file with steps on how to find the solution as well?")

    # GUARDING CLAUSE: If user presses cancel button, it means we changed his mind and we should exit the method
    if generate_pdf is None:
      return

    # Otherwise continue with the calculation
    weights = self.__get_weights__()
    dataset = self.__get_dataset__()
    real_values = self.__get_real_values()
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
    weights = self.__get_weights__()
    dataset = self.__get_dataset__()
    real_values = self.__get_real_values()
    predicted_values = hypothesis(weights, dataset)
    errors = calculate_errors(real_values, predicted_values)
    gradient_descent_result = gradient_descent(
      learning_rate=learning_rate, 
      weights=weights, 
      errors=errors, 
      dataset=dataset
    )

    messagebox.showinfo("Applying gradient descent", f"Updated weights: {", ".join([f"{weight: .{self.precision}f}" for weight in gradient_descent_result.updated_weights])}")

  def on_select_dataset_sheet(self, event):
    self.weights_sheet.deselect()
    self.weights_sheet.redraw()
  
  def on_select_weights_sheet(self, event):
    self.dataset_sheet.deselect()
    self.dataset_sheet.redraw()

  def __get_weights__(self) -> list[float]:
    return [float(elem) for elem in self.weights_sheet.get_data()]

  def __get_real_values(self) -> list[float]:
    return [float(elem) for elem in self.dataset_sheet.get_column_data(self.dataset_sheet.total_columns() - 1)]
  
  def __get_dataset__(self) -> list[list[float]]:
    all_rows = self.dataset_sheet.get_sheet_data()

    # Slice the row first, then convert each element in that slice to a float
    dataset = [
      [float(cell) for cell in row[:int(self.input_size + 1)]] 
      for row in all_rows
    ]

    return dataset
  
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
      

  def __apply_precision__(self):
    # Applying precision to weights
    weights = self.__get_weights__()
    dataset = self.__get_dataset__()
    real_values = self.__get_real_values()
    updated_weights_sheet = [[f"{elem:.{self.precision}f}" for elem in weights]]
    updated_dataset_sheet = []

    for i in range(len(dataset)):
      rounded_dataset = [f"{elem:.{self.precision}f}" for elem in dataset[i]]
      rounded_real_value = f"{real_values[i]:.{self.precision}f}"
      updated_dataset_sheet.append(rounded_dataset + [rounded_real_value])

    self.weights_sheet.set_sheet_data(updated_weights_sheet)
    self.dataset_sheet.set_sheet_data(updated_dataset_sheet)

    self.weights_sheet.refresh()
    self.dataset_sheet.refresh()
  
  def __get_precision__(self):
    # 1. Create the dialog
    dialog = ctk.CTkInputDialog(text="Enter a number (0-5):", title="Change Precision")
    
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
      value = int(raw_input)
      if 0 <= value <= 5: return value
      else: return -1 # Out of range
    except Exception as e:
      return -1 # Not a number