from .print_dialog_ui import PrintDialogUI
from models import PrintSettings
from tkinter import messagebox

class PrintDialog(PrintDialogUI):
  def __init__(self, master):
    super().__init__(master)
    
  def showDialog(self):
    # 1. Force the dialog to calculate its geometry
    self.update_idletasks()
    
    # 2. Get master window position and size
    m_x = self.master.winfo_rootx()
    m_y = self.master.winfo_rooty()
    m_w = self.master.winfo_width()
    m_h = self.master.winfo_height()
    
    # 3. Get this dialog's size
    d_w = self.winfo_width()
    d_h = self.winfo_height()
    
    # 4. Calculate center coordinates
    x = m_x + (m_w // 2) - (d_w // 2)
    y = m_y + (m_h // 2) - (d_h // 2)
    
    # 5. Position and show
    self.geometry(f"+{x}+{y}")
    self.deiconify()
    self.grab_set() # Modal: blocks interaction with master
    
    # Wait until this window is destroyed
    self.wait_window(self)
  
  def getPrintSettings(self):
    return self.__print_settings__
  
  def __handle_cancel__(self):
    self.__print_settings__ = None
    self.destroy()

  def __handle_print__(self):
    try:
      self.__print_settings__ = PrintSettings(
        page_orientation=self.orient_cb.get(),
        page_size=self.size_cb.get(),
        margin_left=self.var_left.get(),
        margin_top=self.var_top.get(),
        margin_right=self.var_right.get(),
        margin_bottom=self.var_bottom.get(),
        units=self.units_cb.get()
      )
      self.destroy()
    except Exception as e:
      messagebox.showerror("Error has occured", "You must enter a valid number for margins.", parent=self)
  
  def __handle_cancel__(self):
    self.__print_settings__ = None
    self.destroy()