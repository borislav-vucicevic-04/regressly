from .weights_section_ui import WeightsSectionUI
from utils import to_rounded_str, safe_float

class WeightsSection(WeightsSectionUI):
  def __init__(self, master, precision = 2, **kwargs):
    super().__init__(master, precision, **kwargs)

  def add_column_at(self, index, header):
    self.sheet.insert_column(idx=index, column=[to_rounded_str(0, self.__precision__)])
    self.sheet.headers(header, index=index)
    self.deselect()

  def apply_precision(self, precision):
    # Applying precision to weights
    weights = self.get_weights()
    updated_weights = list(map(lambda weight: to_rounded_str(weight, self.__precision__), weights))
    self.sheet.set_sheet_data([updated_weights])
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
    value = safe_float(event.value)
    if value is not None: return to_rounded_str(value, self.__precision__)
    else: return None