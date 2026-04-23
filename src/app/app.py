import customtkinter as ctk

from .app_ui import AppUI
from CTkMessagebox import CTkMessagebox
from constants.constants import Colors
from tkinter import messagebox
from utils import *
from models import CreateMseStepsParams

class App(AppUI):
  def __init__(self, master=None):
    super().__init__(master)
  
  def run(self):
    self.mainwindow.mainloop()
  
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
    dataset_filler_values = [0.0] * self.dataset_sheet.total_rows()
    self.input_size += 1
    self.weights_sheet.headers([f"w{i}" for i in range(self.input_size + 1)])
    self.weights_sheet.insert_column(column=[0.0], idx=self.input_size)
    self.dataset_sheet.headers([f"x{i}" for i in range(self.input_size + 1)] + ["y"])
    self.dataset_sheet.insert_column(column=dataset_filler_values, idx=self.input_size)

  def validate_cell_entry(self, event):
    try:
      return float(event.value)
    except ValueError:
      return None
    
  def add_row(self, event):
    new_row_idx = self.dataset_sheet.get_total_rows()
    dataset_filler_values = [1.0] + ([0.0] * (self.dataset_sheet.total_columns() - 1))
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
      create_mse_steps(CreateMseStepsParams(
        weights=weights,
        dataset=dataset,
        real_values=real_values,
        predicted_values=predicted_values,
        errors=errors,
        mse=mse
      ))
    else:
      messagebox.showinfo("Calculated mean squared error", f"Mean squared error for this dataset is {mse}")

  def on_select_dataset_sheet(self, event):
    self.weights_sheet.deselect()
    self.weights_sheet.redraw()
  def on_select_weights_sheet(self, event):
    self.dataset_sheet.deselect()
    self.dataset_sheet.redraw()

  def __get_weights__(self) -> list[float]:
    return self.weights_sheet.get_data()

  def __get_real_values(self) -> list[float]:
    return self.dataset_sheet.get_column_data(self.dataset_sheet.total_columns() - 1)
  
  def __get_dataset__(self) -> list[list[float]]:
    all_rows = self.dataset_sheet.get_sheet_data()
    dataset = [row[:int(self.input_size + 1)] for row in all_rows]

    return dataset