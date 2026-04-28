from .weights_section_ui import WeightsSectionUI

class WeightsSection(WeightsSectionUI):
  def __init__(self, master, precision = 2, **kwargs):
    super().__init__(master, precision, **kwargs)

  def add_column_at(self, index, header):
    self.sheet.insert_column(idx=index, column=[f"{0: .{self.__precision__}f}"])
    self.sheet.headers(header, index=index)
    self.deselect()

  def apply_precision(self, precision):
    # Applying precision to weights
    weights = self.get_weights()
    updated_weights = [[f"{elem:.{precision}f}" for elem in weights]]
    self.sheet.set_sheet_data(updated_weights)
    self.sheet.refresh()
    self.__precision__ = precision

  def deselect(self):
    self.sheet.deselect()
    self.sheet.redraw()

  def get_weights(self) -> list[float]:
    return [float(elem) for elem in self.sheet.get_data()]
  
  def remove_column_at(self, index):
    self.sheet.delete_columns(columns=[index])

  def __validate_cell_entry__(self, event):
    try:
      value = float(event.value) 
      return f"{value: .{self.__precision__}f}"
    except ValueError:
      return None