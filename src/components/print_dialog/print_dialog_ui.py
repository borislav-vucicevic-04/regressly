import customtkinter as ctk
from constants import Colors, Spacing, Fonts
from models import PrintSettings

class PrintDialogUI(ctk.CTkToplevel):
  def __init__(self, master):
    super().__init__(master)
    
    self.__print_settings__ = PrintSettings()
    self.master = master
    self.title("Print Options")
    self.configure(fg_color=Colors.WHITE)
    
    # 1. Widget Wrapper
    self.widget_wrapper = ctk.CTkFrame(self, fg_color="transparent")
    self.widget_wrapper.pack(
      fill="both", 
      expand=True, 
      padx=Spacing.PADX, 
      pady=Spacing.PADY
    )
    
    # Configure columns for the grid
    self.widget_wrapper.grid_columnconfigure(0, weight=1)
    self.widget_wrapper.grid_columnconfigure(1, weight=1)

    # Helper function to create rows
    def add_row(label_text, widget, row):
      lbl = ctk.CTkLabel(self.widget_wrapper, text=label_text, anchor="w", font=Fonts.LABEL)
      lbl.grid(row=row, column=0, sticky="ew", padx=Spacing.PADX, pady=Spacing.PADY)
      widget.grid(row=row, column=1, sticky="ew", padx=Spacing.PADX, pady=Spacing.PADY)

    # 2. Page Orientation (Read-only)
    self.orient_cb = ctk.CTkComboBox(self.widget_wrapper, values=["vertical", "horizontal"], state="readonly")
    self.orient_cb.set("vertical")
    add_row("Page Orientation:", self.orient_cb, 0)

    # 3. Page Size (Read-only)
    self.size_cb = ctk.CTkComboBox(self.widget_wrapper, values=["A3", "A4", "A5", "B4", "B5", "letter", "legal", "ledger"], state="readonly")
    self.size_cb.set("A4")
    add_row("Page Size:", self.size_cb, 1)

    # 4. Margins (Left, Top, Right, Bottom) - Using DoubleVars
    self.var_left = ctk.DoubleVar(value=1.00)
    self.var_top = ctk.DoubleVar(value=1.00)
    self.var_right = ctk.DoubleVar(value=1.00)
    self.var_bottom = ctk.DoubleVar(value=1.00)

    self.m_left = ctk.CTkEntry(self.widget_wrapper, textvariable=self.var_left)
    add_row("Margin Left:", self.m_left, 2)

    self.m_top = ctk.CTkEntry(self.widget_wrapper, textvariable=self.var_top)
    add_row("Margin Top:", self.m_top, 3)

    self.m_right = ctk.CTkEntry(self.widget_wrapper, textvariable=self.var_right)
    add_row("Margin Right:", self.m_right, 4)

    self.m_bottom = ctk.CTkEntry(self.widget_wrapper, textvariable=self.var_bottom)
    add_row("Margin Bottom:", self.m_bottom, 5)

    # 5. Units (Read-only)
    self.units_cb = ctk.CTkComboBox(self.widget_wrapper, values=["inch", "cm"], state="readonly")
    self.units_cb.set("inch")
    add_row("Units:", self.units_cb, 6)

    # 6. Buttons Frame
    self.btn_frame = ctk.CTkFrame(self.widget_wrapper, fg_color="transparent")
    self.widget_wrapper.grid_rowconfigure(7, weight=1) 
    self.btn_frame.grid(row=7, column=0, columnspan=2, sticky="nsew", pady=(Spacing.PADY * 2))
    
    self.btn_frame.grid_columnconfigure((0, 1), weight=1)
    self.btn_frame.grid_rowconfigure(0, weight=1)

    self.cancel_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="Cancel", 
      fg_color=Colors.GRAY,
      hover_color=Colors.LIGHTGRAY,
      font=Fonts.LABEL,
      command=self.__handle_cancel__
    )
    self.cancel_btn.grid(row=0, column=0, padx=Spacing.PADX, sticky="nsew")

    self.print_btn = ctk.CTkButton(
      master=self.btn_frame, 
      text="Print", 
      command=self.__handle_print__,
      font=Fonts.LABEL,
      fg_color=Colors.BLUE,
      hover_color=Colors.LIGHTBLUE
    )
    self.print_btn.grid(row=0, column=1, padx=Spacing.PADX, sticky="nsew")

    # Window Finalization
    self.geometry("450x460") 
    self.resizable(False, False) 
    self.withdraw()

  def showDialog(self): pass
  def getPrintSettings(self) -> PrintSettings | None: pass
  def __handle_print__(self): pass
  def __handle_cancel__(self): pass
