import customtkinter as ctk
from constants import Colors, Fonts, Spacing

class InputSizeControlsSection(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)

    ## Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text_color=Colors.BLACK,
      text="Change input size:",
      anchor="w",
      font=Fonts.SECTION_TITLE
    )
    # Align to the left margin
    self.lbl_title.grid(row=0, column=0, pady=(0, Spacing.PADY), sticky="w")

    ## adding decrease button
    self.btn_decrease = ctk.CTkButton(
      master=self,
      text="Decrease",
      text_color=Colors.WHITE,
      fg_color=Colors.RED,
      hover_color=Colors.LIGHTRED,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    # Changed sticky to "w"
    self.btn_decrease.grid(row=1, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="w")

    ## adding increase button
    self.btn_increase = ctk.CTkButton(
      master=self,
      text="Increase",
      text_color=Colors.WHITE,
      fg_color=Colors.GREEN,
      hover_color=Colors.LIGHTGREEN,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    # Changed sticky to "w"
    self.btn_increase.grid(row=1, column=1, padx=(Spacing.PADX, 0), pady=(0, Spacing.PADY), sticky="w")