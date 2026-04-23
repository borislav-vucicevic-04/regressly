from tkinter import filedialog
from tkinter import messagebox
from xhtml2pdf import pisa

def create_pdf(html: str):
  path = filedialog.asksaveasfilename(
    defaultextension=".pdf",
    filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
    title="Save your PDF as..."
  )

  if path:
    # Open the destination file in binary mode
    with open(path, "wb") as result_file:
      # Convert HTML string to PDF
      pisa_status = pisa.CreatePDF(
        src=html,       # The HTML to convert
        dest=result_file       # File handle to write to
      )
        
    # Check if there were errors
    if pisa_status.err:
      messagebox.showerror("Error", "Error occured while saving the file.")
      print(f"Error occurred during PDF generation:\n {pisa_status.err}")
    else:
      messagebox.showinfo("Success", f"The file has been succesfully saved at:\n {path}")
      print(f"Successfully saved to:\n {path}")