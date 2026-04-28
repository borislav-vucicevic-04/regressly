import customtkinter as ctk
from constants import Colors, Fonts, Spacing

class PrecisionSection(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)

    # This tells the frame to expand column 0 to fill all available space
    self.grid_columnconfigure(0, weight=1)

    # creating value controller for the lbl_display
    self.lbl_display_var = ctk.StringVar(value="No text")

    # Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text="Change precision:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    # sticky="w" to keep the title left-aligned
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="w")

    ## Adding change button
    self.btn_change_precision = ctk.CTkButton(
      master=self,
      text="Change precision",
      text_color=Colors.WHITE,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    # Align to the left margin
    self.btn_change_precision.grid(row=1, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="w")

    ## Creating label for displaying the current precision
    self.lbl_display = ctk.CTkLabel(
      master=self,
      text_color=Colors.BLACK,
      textvariable=self.lbl_display_var,
      anchor="w", # Align text left
      font=Fonts.LABEL
    )
    # Align to the left margin
    self.lbl_display.grid(row=1, column=1, pady=(0, Spacing.PADY), sticky="w")

  def set_display(self, value: str):
    self.lbl_display_var.set(value=value)