import customtkinter as ctk
from constants import Colors, Spacing, Fonts
from models import GradientDescentSettings


class GDSettingsDialogUI(ctk.CTkToplevel):

  def __init__(self, master):
    super().__init__(master)

    self.master = master;
    self.result: GradientDescentSettings | None = None

    # Window setup
    self.title("Gradient Descent Settings")
    self.configure(fg_color=Colors.BLACK)

    # Main window layout configuration to make wrapper cover 100%
    self.grid_columnconfigure(0, weight=1)
    self.grid_rowconfigure(0, weight=1)

    # Widget Wrapper Frame
    self.widget_wrapper = ctk.CTkFrame(self, fg_color=Colors.WHITE, corner_radius=0)
    self.widget_wrapper.grid(row=0, column=0, sticky="nsew")

    # Wrapper layout configuration
    self.widget_wrapper.grid_columnconfigure(0, weight=1)
    self.widget_wrapper.grid_columnconfigure(1, weight=2)
    self.widget_wrapper.grid_rowconfigure((0, 1, 2), weight=1)

    # Learning Rate Row
    self.lr_label = ctk.CTkLabel(
      self.widget_wrapper, text="Learning Rate:", font=Fonts.LABEL, text_color=Colors.BLACK
    )
    self.lr_label.grid(row=0, column=0, padx=Spacing.PADX, pady=Spacing.PADY, sticky="e")
    self.lr_entry = ctk.CTkEntry(
      self.widget_wrapper, placeholder_text="e.g. 0.01", text_color=Colors.BLACK, fg_color=Colors.WHITE, border_color=Colors.GRAY
    )
    self.lr_entry.grid(row=0, column=1, padx=Spacing.PADX, pady=Spacing.PADY, sticky="we")

    # Batch Size Row
    self.batch_label = ctk.CTkLabel(
      self.widget_wrapper, text="Batch Size:", font=Fonts.LABEL, text_color=Colors.BLACK
    )
    self.batch_label.grid(row=1, column=0, padx=Spacing.PADX, pady=Spacing.PADY, sticky="e")
    self.batch_entry = ctk.CTkEntry(
      self.widget_wrapper, placeholder_text="e.g. 32", text_color=Colors.BLACK, fg_color=Colors.WHITE, border_color=Colors.GRAY
    )
    self.batch_entry.grid(row=1, column=1, padx=Spacing.PADX, pady=Spacing.PADY, sticky="we")

    # Epochs Row
    self.epochs_label = ctk.CTkLabel(
      self.widget_wrapper, text="Epochs:", font=Fonts.LABEL, text_color=Colors.BLACK
    )
    self.epochs_label.grid(row=2, column=0, padx=Spacing.PADX, pady=Spacing.PADY, sticky="e")
    self.epochs_entry = ctk.CTkEntry(
      self.widget_wrapper, placeholder_text="e.g. 100", text_color=Colors.BLACK, fg_color=Colors.WHITE, border_color=Colors.GRAY
    )
    self.epochs_entry.grid(row=2, column=1, padx=Spacing.PADX, pady=Spacing.PADY, sticky="we")

    # Button Frame
    self.button_frame = ctk.CTkFrame(self.widget_wrapper, fg_color="transparent")
    self.button_frame.grid(row=3, column=0, columnspan=2, padx=Spacing.PADX, pady=Spacing.PADY, sticky="nsew")
    self.button_frame.grid_columnconfigure((0, 1), weight=1)

    # Cancel Button
    self.cancel_button = ctk.CTkButton(
      self.button_frame, text="Cancel", width=Spacing.BUTTON_WIDTH,
      fg_color=Colors.GRAY, hover_color=Colors.LIGHTGRAY, text_color=Colors.WHITE,
      font=Fonts.LABEL,
      command=self._handle_cancel
    )
    self.cancel_button.grid(row=0, column=0, padx=Spacing.PADX, pady=Spacing.PADY, sticky="e")

    # OK Button
    self.ok_button = ctk.CTkButton(
      self.button_frame, text="OK", width=Spacing.BUTTON_WIDTH,
      fg_color=Colors.BLUE, hover_color=Colors.LIGHTBLUE, text_color=Colors.WHITE,
      font=Fonts.LABEL,
      command=self._hanlde_ok
    )
    self.ok_button.grid(row=0, column=1, padx=Spacing.PADX, pady=Spacing.PADY, sticky="w")

    # Handle window close button (X)
    self.protocol("WM_DELETE_WINDOW", self._handle_cancel)

  def _hanlde_ok(self): pass
  def _handle_cancel(self): pass
  def showDialog(self) -> GradientDescentSettings | None: pass
