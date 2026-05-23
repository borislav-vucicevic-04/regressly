# Regressly

Regressly is a simple Python desktop application for linear regression analysis. It provides:
- interactive input of dataset features and outputs
- mean squared error (MSE) calculation
- mini-batch gradient descent weight updates
- optional PDF export for calculation steps
- precision control and dynamic input dimension adjustment

## Features

- Enter or update feature vectors and target values using a spreadsheet-style UI
- Adjust the number of input variables from 1 to 10
- Calculate predicted values and the mean squared error for the current dataset
- Apply gradient descent using a configurable learning rate, batch size and epoch count
- Export step-by-step solution details for MSE or gradient descent to PDF
- Change numeric precision for display and export

## Installation

1. Install Python 3.9 or newer.
2. Install required packages:

```powershell
python -m pip install customtkinter tksheet xhtml2pdf
```

## Running

From the repository root:

```powershell
python src/main.py
```

## Usage

- Use the `w0`, `w1`, ..., `xn`, `y` table entries to define your regression problem.
- Click **Calculate MSE** to compute the mean squared error for the current weights.
- Click **Apply Gradient Descent** to iteratively update weights with mini-batch gradient descent.
- Both operations offer optional PDF export with detailed computation steps.
- Use the precision dialog to change the number of displayed decimal places.
- Use input size controls to add or remove model features dynamically.

## Project Structure

- `src/main.py` — application entrypoint
- `src/app/` — app UI setup and window configuration
- `src/components/` — custom component widgets, dialogs, sections, and controls
- `src/constants/` — styling, UI constants and HTML templates
- `src/models/` — data models for parameters, gradient descent results, and PDF settings
- `src/utils/` — regression logic, error calculation, PDF generation, and helpers

## Dependencies

- `customtkinter` — modern Tkinter user interface
- `tksheet` — spreadsheet-style table widget
- `xhtml2pdf` — HTML-to-PDF export

## License

This project is licensed under the MIT License.