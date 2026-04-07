import customtkinter as ctk
from .app_ui import AppUI

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
    self.weights_sheet.insert_column(column=[0.0], idx=self.input_size)
    self.dataset_sheet.insert_column(column=dataset_filler_values, idx=self.input_size)
