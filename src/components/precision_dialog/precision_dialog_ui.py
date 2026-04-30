import customtkinter as ctk
from constants import Colors, Spacing, Fonts

class PrecisionDialogUI(ctk.CTkToplevel):
  def __init__(self, master):
    super().__init__(master)
    
    self.master = master
    self.title("Precision Settings")
    self.configure(fg_color=Colors.WHITE)
    
    # Data
    self.base_number = 3.14159265359
    self.result_precision = None
    
    # 1. Widget Wrapper
    self.widget_wrapper = ctk.CTkFrame(self, fg_color="transparent")
    self.widget_wrapper.pack(fill="both", expand=True, padx=Spacing.PADX, pady=Spacing.PADY)
    
    # Configure grid - rows have no weight so they don't expand vertically
    self.widget_wrapper.grid_columnconfigure(0, weight=1)
    self.widget_wrapper.grid_rowconfigure((0, 1, 2, 3), weight=0)

    # 2. Message Label (Row 0)
    self.message_label = ctk.CTkLabel(
      self.widget_wrapper, 
      text="Please keep in mind that this will round all weights and numbers in the dataset, and that this action is irreversible. To reverse it, you will need to change the precision again and manually retype the data!",
      font=Fonts.LABEL,
      wraplength=310,
      justify="left",
      text_color=Colors.BLACK
    )
    self.message_label.grid(row=0, column=0, sticky="ew", pady=(0, Spacing.PADY))

    # 3. Precision Slider (Row 1)
    self.slider_var = ctk.IntVar(value=2)
    self.slider = ctk.CTkSlider(
      self.widget_wrapper,
      from_=2,
      to=10,
      number_of_steps=8,
      variable=self.slider_var,
      command=self.__update_preview__,
      button_color=Colors.BLUE,
      button_hover_color=Colors.LIGHTBLUE
    )
    self.slider.grid(row=1, column=0, sticky="ew", padx=Spacing.PADX, pady=Spacing.PADY)
    
    # 4. Preview Label (Row 2)
    self.preview_label_var = ctk.StringVar(value=f"Rounded value: {self.base_number:.2f}")
    self.preview_label = ctk.CTkLabel(
      self.widget_wrapper, 
      textvariable=self.preview_label_var,
      font=Fonts.LABEL,
      anchor="center",
      text_color=Colors.BLACK
    )
    self.preview_label.grid(row=2, column=0, sticky="ew", pady=(Spacing.PADY, Spacing.PADY))

    # 5. Buttons Frame (Row 3)
    self.btn_frame = ctk.CTkFrame(self.widget_wrapper, fg_color="transparent")
    self.btn_frame.grid(row=3, column=0, sticky="ew", pady=(Spacing.PADY, 0))
    self.btn_frame.grid_columnconfigure((0, 1), weight=1)

    self.cancel_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="Cancel", 
      fg_color=Colors.GRAY,
      hover_color=Colors.LIGHTGRAY,
      font=Fonts.LABEL,
      command=self.__handle_cancel__
    )
    self.cancel_btn.grid(row=0, column=0, padx=Spacing.PADX, sticky="ew")

    self.ok_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="OK", 
      command=self.__handle_ok__,
      font=Fonts.LABEL,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE
    )
    self.ok_btn.grid(row=0, column=1, padx=Spacing.PADX, sticky="ew")

    # Window Finalization - Reduced height to fit content tightly
    self.geometry("350x240") 
    self.resizable(False, False)

  def __update_preview__(self, value): pass
  def __handle_ok__(self): pass
  def __handle_cancel__(self): pass
  def getPrecision(self) -> int | None: pass
  def showDialog(self): pass
