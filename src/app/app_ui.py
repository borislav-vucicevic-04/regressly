import customtkinter as ctk

class AppUI:
  def __init__(self, master=None):
    # creating the main window
    self.mainwindow = ctk.CTk()
    self.mainwindow.title("My first CTK app")
    # Desired window size
    window_width = 640
    window_height = 480

    # Get screen size
    screen_width = self.mainwindow.winfo_screenwidth()
    screen_height = self.mainwindow.winfo_screenheight()

    # Compute position
    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    # Set geometry
    self.mainwindow.geometry(f"{window_width}x{window_height}+{x}+{y}")
    self.mainwindow.minsize(width=window_width, height=window_height)
  
  # Method to run the application
  def run(self): pass