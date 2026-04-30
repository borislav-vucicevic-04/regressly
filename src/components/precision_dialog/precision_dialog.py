from .precision_dialog_ui import PrecisionDialogUI

class PrecisionDialog(PrecisionDialogUI):
  def __init__(self, master):
    super().__init__(master)
  
  def __handle_ok__(self):
    self.result_precision = self.slider_var.get()
    self.destroy()
  
  def __handle_cancel__(self):
    self.result_precision = None
    self.destroy()
  
  def __update_preview__(self, value: int):
    self.preview_label_var.set(f"Rounded value: {self.base_number: .{int(value)}f}")

  def getPrecision(self):
    return self.result_precision
  
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