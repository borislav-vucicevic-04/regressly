from .gdsettings_dialog_ui import GDSettingsDialogUI
from models import GradientDescentSettings
from utils import safe_float, safe_int
from tkinter import messagebox

class GDSettingsDialog(GDSettingsDialogUI):
  def __init__(self, master):
    super().__init__(master)

  def _hanlde_ok(self):
    try:
      learning_rate = safe_float(self.lr_entry.get())
      batch_size = safe_int(self.batch_entry.get())
      epochs = safe_int(self.epochs_entry.get())

      if learning_rate is None: raise ValueError("You must enter a valid floating point number for \"learning rate\".")
      if learning_rate <= 0: raise ValueError("\"Learning rate\" must a be positive number.")
      if batch_size is None: raise ValueError("You must enter a valid integer number for \"batch size\".")
      if batch_size <= 0: raise ValueError("\"Batch size\" must be a positive number.")
      if epochs is None: raise ValueError("You must enter a valid integer number for \"epochs\".")
      if epochs <= 0: raise ValueError("\"Epochs\" must be a positive number.")

      self.result = GradientDescentSettings(
        learning_rate=learning_rate,
        batch_size=batch_size,
        epochs=epochs
      )
      self.destroy();
    except ValueError as error:
      messagebox.showerror("Gradient Descent Settings", error)

  def _handle_cancel(self):
    self.result = None
    self.destroy()

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