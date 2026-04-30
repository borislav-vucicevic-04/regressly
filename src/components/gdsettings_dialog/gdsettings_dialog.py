from .gdsettings_dialog_ui import GDSettingsDialogUI
from tkinter import messagebox
from models import GDSettings
from re import match

class GDSettingsDialog(GDSettingsDialogUI):
  def __init__(self, master, batch_size_maximum):
    super().__init__(master, batch_size_maximum=batch_size_maximum)

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

  def getSettings(self):
    return self.results

  def __handle_ok__(self):
    try:
      pattern = r"^\d*\.?\d+$"
      epochs = self.entry_epochs.get()
      batch_size = self.entry_batch.get()
      learning_rate = self.entry_learning_rate.get()

      if not epochs.isdigit(): 
        raise ValueError("The number of epochs must be positive integer.")
      if not batch_size.isdigit(): 
        raise ValueError("The batch size must be positive integer.")
      if int(batch_size) > self.batch_size_maximum: 
        raise ValueError("The batch size must be less than or equal to the total number of entries.")
      if not bool(match(pattern, learning_rate)):
        raise ValueError("The learning rate must be a number greather than or equal to 0.")
      
      self.results = GDSettings(
        epochs=int(epochs),
        batch_size=int(batch_size),
        learning_rate=float(learning_rate)
      )
      self.destroy()
    except ValueError as e:
      messagebox.showerror("Gradient Descent Settings", e)

  def __handle_cancel__(self):
    self.results = None
    self.destroy()