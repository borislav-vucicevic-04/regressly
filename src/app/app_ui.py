import customtkinter as ctk
from tksheet import Sheet
from components import *
from constants.constants import Colors
from constants.constants import Spacing
from constants.constants import Fonts

class AppUI:
  def __init__(self, master=None):
    # CREATING MAIN WINDOW
    self.mainwindow = ctk.CTk(fg_color=Colors.WHITE)
    # CREATING APP PROPERTIES
    ## current input size of the function
    self.input_size = 3
    ## current precision
    self.precision = 2
    ## label value controller
    self.lbl_precision_var = ctk.StringVar(value=f"Current precision: {self.precision}")
    # SETUP MAINWINDOW
    self.__setup_mainwindow__()
    # CREATING FRAME FOR COMPONENTS
    self.__create_widget_wrapper__()
    # TITLE LABEL
    self.__create_lbl_title__()
    # INTERFACE FOR SETTING THE PRECISION OF NUMBERS
    self.__create_precision_section__()
    # SECTION FOR CALCULATIONS
    self.__create_calculations_section__()
    # SECTION FOR DATASET CONTROLS
    self.__create_dataset_controls_section__()
    # INTERFACE FOR SETTING THE FUNCTION INPUT SIZE
    self.__create_input_size_section__()
    # INTERFACE FOR SETTING FUNCTION WEIGHTS
    self.__create_weights_section__()
    # INTERFACE FOR THE DATASET
    self.__create_dataset_section__()
  def __setup_mainwindow__(self):
    self.mainwindow.title("My first CTK app")
    ## Desired window size
    window_width = Spacing.WINDOW_WIDTH
    window_height = Spacing.WINDOW_HEIGHT

    ## Get screen size
    screen_width = self.mainwindow.winfo_screenwidth()
    screen_height = self.mainwindow.winfo_screenheight()

    ## Compute position
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    ## Set geometry
    self.mainwindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
    self.mainwindow.minsize(width=window_width, height=window_height)
  def __create_widget_wrapper__(self):
    self.widget_wrapper: ctk.CTkFrame = ctk.CTkFrame(
      master=self.mainwindow,
      fg_color=Colors.WHITE
    )
    self.widget_wrapper.pack(fill="both", expand=True, padx=Spacing.PADX, pady=Spacing.PADY)
    self.widget_wrapper.grid_columnconfigure((0, 1), weight=1)
    self.widget_wrapper.grid_rowconfigure(4, weight=1)
  def __create_lbl_title__(self):
    self.lbl_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text_color=Colors.BLACK,
      text="REGRESSLY",
      anchor="center",
      font=Fonts.APP_TITLE
    )
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="nswe", columnspan=2)
  def __create_precision_section__(self):
    self.precision_section = PrecisionSection(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE
    )
    # Ensure the frame sits on the left of the wrapper
    self.precision_section.grid(row=1, column=0, sticky="w")
    self.precision_section.set_display(f"Current precision: {self.precision}")
    self.precision_section.btn_change_precision.bind("<Button-1>", self.change_precision)

  def __create_input_size_section__(self):
    # creating section frame
    self.input_size_controls_section = InputSizeControlsSection(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE
    )
    # Ensure the frame sits on the left of its grid cell
    self.input_size_controls_section.grid(row=2, column=0, sticky="w")
    self.input_size_controls_section.btn_decrease.bind("<Button-1>", self.decrease_input_size)
    self.input_size_controls_section.btn_increase.bind("<Button-1>", self.increase_input_size)
  def __create_calculations_section__(self):
    self.calculations_section = CalculationsSection(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE
    )
    # Ensure the section frame itself aligns to the left of its grid cell
    self.calculations_section.grid(row=1, column=1, sticky="w")
    self.calculations_section.btn_calculate_mse.bind("<Button-1>", self.calculate_mse)
    self.calculations_section.btn_apply_gradient_descent.bind("<Button-1>", self.apply_gradient_descent)
  def __create_dataset_controls_section__(self):
    self.dataset_controls_section = DatasetControlsSection(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE
    )
    # Ensure the section frame itself aligns to the left of its grid cell
    self.dataset_controls_section.grid(row=2, column=1, sticky="w")
    self.dataset_controls_section.btn_add_row.bind("<Button-1>", self.add_row)
    self.dataset_controls_section.btn_delete_rows.bind("<Button-1>", self.delete_rows)

  def __create_weights_section__(self):  
    self.weights_section = WeightsSection(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE,
      precision=self.precision
    )
    # sticky="ew" makes the section frame fill the width of the widget_wrapper
    self.weights_section.grid(row=3, column=0, columnspan=3, sticky="ew")
    self.weights_section.sheet.extra_bindings([("cell_select", self.on_select_weights_sheet)])
    
  def __create_dataset_section__(self):
    self.frame_dataset_section = ctk.CTkFrame(
      master=self.widget_wrapper,
      fg_color=Colors.WHITE
    )
    # sticky="nsew" allows the section itself to grow portraitly within widget_wrapper
    self.frame_dataset_section.grid(row=4, column=0, columnspan=3, sticky="nsew")
    
    # Configure column 1 to take up landscape space
    self.frame_dataset_section.grid_columnconfigure(1, weight=1)
    
    # NEW: Configure row 2 (the sheet row) to take up all remaining portrait space
    self.frame_dataset_section.grid_rowconfigure(1, weight=1)

    ## Creating section title
    self.lbl_dataset_title = ctk.CTkLabel(
      master=self.frame_dataset_section,
      text="Dataset:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    self.lbl_dataset_title.grid(row=0, column=0, columnspan=2, pady=(0, Spacing.PADY), sticky="w")

    # Creating dataset sheet wrapper
    self.dataset_sheet_wrapper = ctk.CTkFrame(
      master=self.frame_dataset_section,
      border_color=Colors.BLACK,
      corner_radius=0,
      fg_color=Colors.WHITE,
      border_width=1
    )
    # sticky="nsew" is critical here to fill the weighted row and column
    self.dataset_sheet_wrapper.grid(row=1, column=0, columnspan=2, sticky="nsew")
    
    # Creating dataset sheet
    self.dataset_sheet = Sheet(
      self.dataset_sheet_wrapper,
      row_height=20,
      header=["x0", "x1", "x2", "x3", "y"],
      data=[[f"{1: .2f}", f"{0: .2f}", f"{0: .2f}", f"{0: .2f}", f"{0: .2f}"]],
      frame_bg=Colors.BLACK
    )
    self.dataset_sheet.enable_bindings((
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
    self.dataset_sheet.set_options(auto_resize_columns=True)
    self.dataset_sheet.readonly_cells(column=0)
    self.dataset_sheet.edit_validation(self.validate_cell_entry)
    self.dataset_sheet.extra_bindings([("cell_select", self.on_select_dataset_sheet)])
    # pack(expand=True) ensures the sheet fills the wrapper frame
    self.dataset_sheet.pack(fill="both", expand=True, padx=2, pady=(2, 3))
  
  # Method to run the application
  def run(self): pass
  def change_precision(self, event): pass
  def decrease_input_size(self, event): pass
  def increase_input_size(self, event): pass
  def validate_cell_entry(self, event): pass
  def delete_rows(self, event): pass
  def add_row(self, event): pass
  def calculate_mse(self, event): pass
  def apply_gradient_descent(self, event): pass
  def on_select_dataset_sheet(self, event): pass
  def on_select_weights_sheet(self, event): pass