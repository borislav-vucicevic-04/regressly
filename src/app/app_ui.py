import customtkinter as ctk
from tksheet import Sheet
from components import *
from constants.constants import Colors
from constants.constants import Spacing
from constants.constants import Fonts

class AppUI:
  def __init__(self, master=None):
    self.mainwindow = ctk.CTk(fg_color=Colors.WHITE) # Creating main window
    
    self.input_size = 3 # current input size of the function
    self.precision = 2 # current precision

    self.__create_sections_container__() # Creating container for sections
    self.__create_title__() # Creating and positioning title label
    self.__create_sections__() # Creating sections
    self.__position_sections__() # Positioning sections
    self.__bind_methods__() # Biding App methods to children of section components
    self.__setup_mainwindow__() # Setting up the window
  
  def __create_sections_container__(self):
    self.sections_container: ctk.CTkFrame = ctk.CTkFrame(master=self.mainwindow, fg_color=Colors.WHITE)
    self.sections_container.pack(fill="both", expand=True, padx=Spacing.PADX, pady=Spacing.PADY)
    self.sections_container.grid_columnconfigure((0, 1), weight=1)
    self.sections_container.grid_rowconfigure(4, weight=1)

  def __create_title__(self):
    self.lbl_title = ctk.CTkLabel(
      master=self.sections_container,
      text_color=Colors.BLACK,
      text="REGRESSLY",
      anchor="center",
      font=Fonts.APP_TITLE
    )
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="nswe", columnspan=2)

  def __create_sections__(self):
    self.precision_section = PrecisionSection(master=self.sections_container, fg_color=Colors.WHITE)
    self.precision_section.set_display(f"Current precision: {self.precision}")
    self.calculations_section = CalculationsSection(master=self.sections_container, fg_color=Colors.WHITE)
    self.dataset_controls_section = DatasetControlsSection(master=self.sections_container, fg_color=Colors.WHITE)
    self.input_size_controls_section = InputSizeControlsSection(master=self.sections_container, fg_color=Colors.WHITE)
    self.weights_section = WeightsSection(master=self.sections_container, fg_color=Colors.WHITE, precision=self.precision)
    self.dataset_section = DatasetSection(master=self.sections_container, precision=self.precision, fg_color=Colors.WHITE)
  
  def __position_sections__(self):
    self.precision_section.grid(row=1, column=0, sticky="w")
    self.calculations_section.grid(row=1, column=1, sticky="w")
    self.dataset_controls_section.grid(row=2, column=1, sticky="w")
    self.input_size_controls_section.grid(row=2, column=0, sticky="w")
    self.weights_section.grid(row=3, column=0, columnspan=3, sticky="ew")
    self.dataset_section.grid(row=4, column=0, columnspan=3, sticky="nsew")

  def __bind_methods__(self):
    self.precision_section.btn_change_precision.bind("<Button-1>", self.change_precision)
    self.calculations_section.btn_calculate_mse.bind("<Button-1>", self.calculate_mse)
    self.calculations_section.btn_apply_gradient_descent.bind("<Button-1>", self.apply_gradient_descent)
    self.input_size_controls_section.btn_decrease.bind("<Button-1>", self.decrease_input_size)
    self.input_size_controls_section.btn_increase.bind("<Button-1>", self.increase_input_size)
    self.dataset_controls_section.btn_add_row.bind("<Button-1>", lambda e: self.dataset_section.add_row())
    self.dataset_controls_section.btn_delete_rows.bind("<Button-1>", lambda e: self.dataset_section.delete_rows())
    self.weights_section.sheet.extra_bindings([("cell_select", lambda e: self.dataset_section.deselect())])
    self.dataset_section.sheet.extra_bindings([("cell_select", lambda e: self.weights_section.deselect())])

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

  def run(self): pass
  def change_precision(self, event): pass
  def decrease_input_size(self, event): pass
  def increase_input_size(self, event): pass
  def calculate_mse(self, event): pass
  def apply_gradient_descent(self, event): pass