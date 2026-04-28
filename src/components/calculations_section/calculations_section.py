import customtkinter as ctk
from constants import Colors, Fonts, Spacing

class CalculationsSection(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)

    # Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text="Calculations:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    # Fixed: changed pady to (0, Spacing.PADY) to match Precision section
    self.lbl_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, Spacing.PADY))

    # Creating button for calculating mse
    self.btn_calculate_mse = ctk.CTkButton(
      master=self,
      text="Calculate MSE",
      text_color=Colors.WHITE,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    # Fixed: changed pady to (0, Spacing.PADY) so it doesn't push away from the title
    self.btn_calculate_mse.grid(row=1, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="w")

    # Creating button for applying gradient descent
    self.btn_apply_gradient_descent = ctk.CTkButton(
      master=self,
      text="Apply GD",
      text_color=Colors.WHITE,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    # Fixed: changed pady to (0, Spacing.PADY)
    self.btn_apply_gradient_descent.grid(row=1, column=1, padx=(Spacing.PADX, 0), pady=(0, Spacing.PADY), sticky="w")