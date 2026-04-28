import customtkinter as ctk
from constants import Colors, Fonts, Spacing
from tksheet import Sheet

class WeightsSectionUI(ctk.CTkFrame):
  def __init__(self, master, precision: int = 2, **kwargs):
    super().__init__(master, **kwargs)
    self.__precision__ = precision
    
    # sticky="ew" makes the section frame fill the width of the widget_wrapper
    self.grid(row=3, column=0, columnspan=3, sticky="ew")
    
    # This tells the frame to expand column 0 to fill all available space
    self.grid_columnconfigure(0, weight=1)

    # Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text="Function weights:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    # sticky="w" to keep the title left-aligned
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="w")

    # Creating weights sheet wrapper
    self.__sheet_container__ = ctk.CTkFrame(
      master=self,
      border_color=Colors.BLACK,
      corner_radius=0,
      fg_color=Colors.WHITE,
      border_width=1
    )
    # sticky="nsew" here fills the allocated column space
    self.__sheet_container__.grid(row=1, column=0, sticky="nsew", padx=2, pady=(0, Spacing.PADY))
    
    # Creating weights sheet
    self.sheet = Sheet(
      self.__sheet_container__,
      row_height=20,
      height=46,
      header=["w0", "w1", "w2", "w3"],
      data=[[f"{1: .{self.__precision__}f}", f"{0: .{self.__precision__}f}", f"{0: .{self.__precision__}f}", f"{0: .{self.__precision__}f}"]],
      frame_bg=Colors.BLACK
    )
    self.sheet.enable_bindings((
      "single_select", 
      "row_select", 
      "column_width_resize", 
      "arrowkeys", 
      "right_click_popup_menu", 
      "copy", 
      "paste", 
      "edit_cell"
    ))
    self.sheet.hide("y_scrollbar")
    self.sheet.set_options(auto_resize_columns=True)
    self.sheet.edit_validation(self.__validate_cell_entry__)
    self.sheet.pack(fill="both", expand=True, padx=2, pady=(2, 3))

  def add_column_at(self, index: int, header: str): pass
  def apply_precision(self, precision: int): pass
  def deselect(self): pass
  def get_weights(self): pass
  def remove_column_at(self, index: int): pass
  def __validate_cell_entry__(self, event): pass