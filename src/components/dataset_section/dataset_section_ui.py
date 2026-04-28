import customtkinter as ctk
from constants import Colors, Fonts, Spacing
from tksheet import Sheet

class DatasetSectionUI(ctk.CTkFrame):
  def __init__(self, master, precision: int = 2, **kwargs):
    super().__init__(master, **kwargs)
    # Private component properties
    self.__precision__ = precision
    # Grid setup
    self.grid_columnconfigure(1, weight=1)
    self.grid_rowconfigure(1, weight=1)

    ## Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text="Dataset:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    self.lbl_title.grid(row=0, column=0, columnspan=2, pady=(0, Spacing.PADY), sticky="w")

    # Creating dataset sheet wrapper
    self.__sheet_container__ = ctk.CTkFrame(
      master=self,
      border_color=Colors.BLACK,
      corner_radius=0,
      fg_color=Colors.WHITE,
      border_width=1
    )
    # sticky="nsew" is critical here to fill the weighted row and column
    self.__sheet_container__.grid(row=1, column=0, columnspan=2, sticky="nsew")
    
    # Creating dataset sheet
    self.sheet = Sheet(
      self.__sheet_container__,
      row_height=20,
      header=["x0", "x1", "x2", "x3", "y"],
      data=[[f"{1: .2f}", f"{0: .2f}", f"{0: .2f}", f"{0: .2f}", f"{0: .2f}"]],
      frame_bg=Colors.BLACK
    )
    self.sheet.enable_bindings((
      "single_select", 
      "row_select", 
      "drag_select", 
      "column_width_resize", 
      "arrowkeys", 
      "right_click_popup_menu", 
      "copy", 
      "paste", 
      "edit_cell"
    ))
    self.sheet.set_options(auto_resize_columns=True)
    self.sheet.readonly_cells(column=0)
    self.sheet.edit_validation(self.__validate_cell_entry__)
    # pack(expand=True) ensures the sheet fills the wrapper frame
    self.sheet.pack(fill="both", expand=True, padx=2, pady=(2, 3))
  
  def add_column_at(self, index: int, header: str): pass
  def add_row(self): pass
  def apply_precision(self, precision: int): pass
  def delete_rows(self): pass
  def deselect(self): pass
  def get_inputs(self): pass
  def get_outputs(self): pass
  def remove_column_at(self, index: int): pass
  def __validate_cell_entry__(self, event): pass