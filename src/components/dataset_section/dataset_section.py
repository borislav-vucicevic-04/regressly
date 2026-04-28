from .dataset_section_ui import DatasetSectionUI
from tkinter import messagebox

class DatasetSection(DatasetSectionUI):
  def __init__(self, master, precision = 2, **kwargs):
    super().__init__(master, precision, **kwargs)

  def add_column_at(self, index, header):
    filler_values = [f"{0: .{self.__precision__}f}"] * self.sheet.get_total_rows()
    self.sheet.insert_column(idx=index, column=filler_values)
    self.sheet.headers(header, index=index)
    self.sheet.headers("y", index=(self.sheet.get_total_columns() - 1))
    self.deselect()

  def add_row(self):
    new_row_idx = self.sheet.get_total_rows()
    dataset_filler_values = [f"{1: .{self.__precision__}f}"] + ([f"{0: .{self.__precision__}f}"] * (self.sheet.total_columns() - 1))
    self.sheet.insert_row(row=dataset_filler_values, idx=self.sheet.total_rows())
    self.sheet.readonly_cells(row=new_row_idx, column=0, readonly=True)

  def apply_precision(self, precision):
    inputs = self.get_inputs()
    outputs = self.get_outputs()
    updated_dataset_sheet = []

    for i in range(len(inputs)):
      rounded_inputs = [f"{elem:.{precision}f}" for elem in inputs[i]]
      rounded_output = f"{outputs[i]:.{precision}f}"
      updated_dataset_sheet.append(rounded_inputs + [rounded_output])

    self.sheet.set_sheet_data(updated_dataset_sheet)
    self.sheet.refresh()
    self.__precision__ = precision

  def delete_rows(self):
    selected_rows = self.sheet.get_selected_rows()
    selected_rows_count = len(selected_rows)
    
    if selected_rows_count == 0: 
      messagebox.showerror(title="Error while deleting rows", message="You should select at least one row.")
      return
    
    if selected_rows_count == self.sheet.get_total_rows(): 
      messagebox.showerror(title="Error while deleting rows", message="You cannot delete all rows.")
      return
    
    confirmation = messagebox.askyesno(
      title="Delete rows", 
      message="Are you sure you want to delete selected rows?", 
      icon="warning",
      default="no"
    )
    
    if confirmation: self.sheet.delete_rows(rows=selected_rows)

  def deselect(self):
    self.sheet.deselect()
    self.sheet.redraw()

  def get_inputs(self) -> list[list[float]]:
    input_size = self.sheet.total_columns() - 1
    all_rows = self.sheet.get_sheet_data()

    # Slice the row first, then convert each element in that slice to a float
    inputs = [
      [float(cell) for cell in row[:input_size]] 
      for row in all_rows
    ]

    return inputs

  def get_outputs(self) -> list[float]:
    return [float(elem) for elem in self.sheet.get_column_data(self.sheet.total_columns() - 1)]

  def remove_column_at(self, index):
    self.sheet.delete_columns(columns=[index])

  def __validate_cell_entry__(self, event):
    try:
      value = float(event.value) 
      return f"{value: .{self.__precision__}f}"
    except ValueError:
      return None