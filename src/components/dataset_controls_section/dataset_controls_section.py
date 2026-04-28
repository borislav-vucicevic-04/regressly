import customtkinter as ctk
from constants import Colors, Fonts, Spacing

class DatasetControlsSection(ctk.CTkFrame):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    # Creating section title
    self.lbl_title = ctk.CTkLabel(
      master=self,
      text="Dataset controls:",
      text_color=Colors.BLACK,
      font=Fonts.SECTION_TITLE,
      anchor="w"
    )
    # Fixed: changed pady to (0, Spacing.PADY) to match Precision section
    self.lbl_title.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, Spacing.PADY))

    ## Creating button for deleting rows
    self.btn_delete_rows = ctk.CTkButton(
      master=self,
      text="Delete row",
      text_color=Colors.WHITE,
      fg_color=Colors.RED,
      hover_color=Colors.LIGHTRED,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    self.btn_delete_rows.grid(row=1, column=0, padx=(0, Spacing.PADX), pady=(0, Spacing.PADY), sticky="w")

    ## Creating button for adding rows
    self.btn_add_row = ctk.CTkButton(
      master=self,
      text="Add row",
      text_color=Colors.WHITE,
      fg_color=Colors.GREEN,
      hover_color=Colors.LIGHTGREEN,
      cursor="hand2",
      width=Spacing.BUTTON_WIDTH,
      font=Fonts.LABEL
    )
    self.btn_add_row.grid(row=1, column=1, padx=(Spacing.PADX, 0), pady=(0, Spacing.PADY), sticky="w")