import customtkinter as ctk
from constants import Colors, Spacing, Fonts
from models import GDSettings

class GDSettingsDialogUI(ctk.CTkToplevel):
  def __init__(self, master, batch_size_maximum: int):
    super().__init__(master)
    self.master = master
    self.title("GD Settings")
    self.configure(fg_color=Colors.WHITE)
    # Data
    self.results = None
    self.batch_size_maximum = batch_size_maximum
    # 1. Widget Wrapper
    self.widget_wrapper = ctk.CTkFrame(self, fg_color="transparent")
    self.widget_wrapper.pack(fill="both", expand=True, padx=Spacing.PADX, pady=Spacing.PADY)
    # Labels
    self.lbl_epochs = ctk.CTkLabel(self.widget_wrapper, text="Number of epochs:", font=Fonts.LABEL, text_color=Colors.BLACK)
    self.lbl_batch = ctk.CTkLabel(self.widget_wrapper, text="Batch size:", font=Fonts.LABEL, text_color=Colors.BLACK)
    self.lbl_learning_rate = ctk.CTkLabel(self.widget_wrapper, text="Learning rate:", font=Fonts.LABEL, text_color=Colors.BLACK)
    # Entries
    self.entry_epochs = ctk.CTkEntry(self.widget_wrapper)
    self.entry_batch = ctk.CTkEntry(self.widget_wrapper)
    self.entry_learning_rate = ctk.CTkEntry(self.widget_wrapper)
    # Buttons Frame and Buttons
    self.btn_frame = ctk.CTkFrame(self.widget_wrapper, fg_color="transparent")
    self.cancel_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="Cancel", 
      fg_color=Colors.GRAY,
      hover_color=Colors.LIGHTGRAY,
      font=Fonts.LABEL,
      command=self.__handle_cancel__
    )
    self.ok_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="OK", 
      command=self.__handle_ok__,
      font=Fonts.LABEL,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE
    )
    # Configure Grid
    self.widget_wrapper.grid_columnconfigure(0, weight=0)
    self.widget_wrapper.grid_columnconfigure(1, weight=1)
    # Row 0: Epochs
    self.lbl_epochs.grid(row=0, column=0, sticky="w", pady=Spacing.PADY)
    self.entry_epochs.grid(row=0, column=1, sticky="ew", padx=(Spacing.PADX, 0), pady=Spacing.PADY)
    # Row 1: Batch Size
    self.lbl_batch.grid(row=1, column=0, sticky="w", pady=Spacing.PADY)
    self.entry_batch.grid(row=1, column=1, sticky="ew", padx=(Spacing.PADX, 0), pady=Spacing.PADY)
    # Row 2: Learning Rate
    self.lbl_learning_rate.grid(row=2, column=0, sticky="w", pady=Spacing.PADY)
    self.entry_learning_rate.grid(row=2, column=1, sticky="ew", padx=(Spacing.PADX, 0), pady=Spacing.PADY)
    # Row 3: Buttons
    self.btn_frame.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(Spacing.PADY * 2, 0))
    self.btn_frame.grid_columnconfigure((0, 1), weight=1)
    self.cancel_btn.grid(row=0, column=0, padx=Spacing.PADX, sticky="ew")
    self.ok_btn.grid(row=0, column=1, padx=Spacing.PADX, sticky="ew")
    # Window Finalization
    self.geometry("400x240")
    self.resizable(False, False)
    self.grab_set()

  def __handle_ok__(self): pass
  def __handle_cancel__(self): pass
  def getSettings(self) -> GDSettings | None: pass
  def showDialog(self): pass
