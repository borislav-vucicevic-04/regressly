import customtkinter as ctk
from tksheet import Sheet
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
    ## label value controller
    self.lbl_input_size_var = ctk.StringVar(value=f"Current size: {self.input_size}")
    # SETUP MAINWINDOW
    self.__setup_mainwindow__()
    # CREATING FRAME FOR COMPONENTS
    self.__create_component_wrapper__()
    # TITLE LABEL
    self.__create_lbl_title__()
    # INTERFACE FOR SETTING THE FUNCTION INPUT SIZE
    self.__create_input_size_section__()
    # INTERFACE FOR SETTING FUNCTION WEIGHTS
    self.__create_weights_section__()
    # INTERFACE FOR THE DATASET
    self.__create_dataset_section__()
    # SECTION FOR CALCULATIONS
    self.__create_calculations_section__()
  def __setup_mainwindow__(self):
    self.mainwindow.title("My first CTK app")
    ## Desired window size
    window_width = 640
    window_height = 480

    ## Get screen size
    screen_width = self.mainwindow.winfo_screenwidth()
    screen_height = self.mainwindow.winfo_screenheight()

    ## Compute position
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    ## Set geometry
    self.mainwindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
    self.mainwindow.minsize(width=window_width, height=window_height)
  def __create_component_wrapper__(self):
    self.widget_wrapper: ctk.CTkFrame = ctk.CTkFrame(
      master=self.mainwindow,
      fg_color=Colors.WHITE
    )
    self.widget_wrapper.pack(fill="both", expand=True, padx=Spacing.PADX, pady=Spacing.PADY)
    self.widget_wrapper.grid_columnconfigure((0, 1), weight=1)
    self.widget_wrapper.grid_rowconfigure(7, weight=1)
  def __create_lbl_title__(self):
    self.lbl_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text_color=Colors.BLACK,
      text="REGRESSLY",
      anchor="center",
      font=Fonts.APP_TITLE
    )
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="nswe", columnspan=2)
  def __create_input_size_section__(self):
    ## Creting section title
    self.lbl_input_size_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text_color=Colors.BLACK,
      text="Set input size:",
      anchor="w",
      font=Fonts.SECTION_TITLE
    )
    self.lbl_input_size_title.grid(row=1, column=0, pady=(0, Spacing.PADY), sticky="nswe")

    ## adding decrease button
    self.btn_decrease_input = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Decrease input size",
      text_color=Colors.WHITE,
      fg_color=Colors.RED,
      hover_color=Colors.LIGHTRED,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_decrease_input.grid(row=2, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="nswe")
    self.btn_decrease_input.bind("<Button-1>", self.decrease_input_size)

    ## adding decrease button
    self.btn_increase_input = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Increase input size",
      text_color=Colors.WHITE,
      fg_color=Colors.GREEN,
      hover_color=Colors.LIGHTGREEN,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_increase_input.grid(row=2, column=1, padx=(Spacing.PADX, 0), pady=(0, Spacing.PADY), sticky="nswe")
    self.btn_increase_input.bind("<Button-1>", self.increase_input_size)
  def __create_weights_section__(self):
    # Creating section title
    self.lbl_weights_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text="Function weights:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    self.lbl_weights_title.grid(row=3, column=0, columnspan=2, pady=(0, Spacing.PADY), sticky="nswe")

    # Creating weights sheet wrapper
    self.weights_sheet_wrapper = ctk.CTkFrame(
      master=self.widget_wrapper,
      border_color=Colors.BLACK,
      corner_radius=0,
      fg_color=Colors.WHITE,
      border_width=1
    )
    self.weights_sheet_wrapper.grid(row=4, column=0, columnspan=2, sticky="nswe", padx=2, pady=(0, Spacing.PADY))
    
    # Creating weights sheet
    self.weights_sheet = Sheet(
      self.weights_sheet_wrapper,
      row_height=20,
      height=46,
      header=["w0", "w1", "w2", "w3"],
      data=[[1.0, 0.0, 0.0, 0.0]],
      frame_bg=Colors.BLACK
    )
    self.weights_sheet.enable_bindings((
      "single_select", 
      "row_select", 
      "column_width_resize", 
      "arrowkeys", 
      "right_click_popup_menu", 
      "copy", 
      "paste", 
      "edit_cell"
    ))
    self.weights_sheet.hide("y_scrollbar")
    self.weights_sheet.set_options(auto_resize_columns=True)
    self.weights_sheet.edit_validation(self.validate_cell_entry)
    self.weights_sheet.pack(fill="both", expand=True, padx=2, pady=(2, 3))
  def __create_dataset_section__(self):
    # Creating section title
    self.lbl_dataset_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text="Dataset:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    self.lbl_dataset_title.grid(row=5, column=0, columnspan=2, pady=(0, Spacing.PADY), sticky="nswe")

    # Creating button for deleting rows
    self.btn_delete_row = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Delete row",
      text_color=Colors.WHITE,
      fg_color=Colors.RED,
      hover_color=Colors.LIGHTRED,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_delete_row.grid(row=6, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="nswe")
    self.btn_delete_row.bind("<Button-1>", self.delete_row)

    # Creating button for deleting rows
    self.btn_add_row = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Add row",
      text_color=Colors.WHITE,
      fg_color=Colors.GREEN,
      hover_color=Colors.LIGHTGREEN,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_add_row.grid(row=6, column=1, padx=(Spacing.PADX, 0), pady=(0, Spacing.PADY), sticky="nswe")
    self.btn_add_row.bind("<Button-1>", self.add_row)

    # Creating dataset sheet wrapper
    self.dataset_sheet_wrapper = ctk.CTkFrame(
      master=self.widget_wrapper,
      border_color=Colors.BLACK,
      corner_radius=0,
      fg_color=Colors.WHITE,
      border_width=1
    )
    self.dataset_sheet_wrapper.grid(row=7, column=0, columnspan=2, sticky="nswe")
    
    # Creating weights sheet
    self.dataset_sheet = Sheet(
      self.dataset_sheet_wrapper,
      row_height=20,
      header=["x0", "x1", "x2", "x3", "y"],
      data=[[1.0, 0.0, 0.0, 0.0, 0.0]],
      frame_bg=Colors.BLACK
    )
    self.dataset_sheet.enable_bindings((
      "single_select", 
      "row_select", 
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
    self.dataset_sheet.pack(fill="both", expand=True, padx=2, pady=(2, 3))
  def __create_calculations_section__(self):
    # Creating section title
    self.lbl_calculations_title = ctk.CTkLabel(
      master=self.widget_wrapper,
      text="Calculations:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    self.lbl_calculations_title.grid(row=8, column=0, columnspan=2, sticky="nswe", pady=Spacing.PADY)

    # Creating button for calculating mse
    self.btn_calculate_mse = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Calculate MSE",
      text_color=Colors.WHITE,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_calculate_mse.grid(row=8, column=0, padx=(0, Spacing.PADX), pady=(Spacing.PADY, 0), sticky="nswe")
    self.btn_calculate_mse.bind("<Button-1>", self.calculate_mse)

    # Creating button for applying gradient descent
    self.btn_apply_gradient_descent = ctk.CTkButton(
      master=self.widget_wrapper,
      text="Apply gradient descent",
      text_color=Colors.WHITE,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE,
      cursor="hand2",
      font=Fonts.LABEL
    )
    self.btn_apply_gradient_descent.grid(row=8, column=1, padx=(Spacing.PADX, 0), pady=(Spacing.PADY, 0), sticky="nswe")
    self.btn_apply_gradient_descent.bind("<Button-1>", self.calculate_mse)

  
  # Method to run the application
  def run(self): pass
  def decrease_input_size(self, event): pass
  def increase_input_size(self, event): pass
  def validate_cell_entry(self, event): pass
  def delete_row(self, event): pass
  def add_row(self, event): pass
  def calculate_mse(self, event): pass