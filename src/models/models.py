from dataclasses import dataclass, field
from typing import Literal

@dataclass(kw_only=True)
class PrintSettings:
  page_orientation: Literal["landscape", "portrait"] = "portrait"
  page_size: Literal["A3", "A4", "A5", "B4", "B5", "letter", "legal", "ledger"] = "A4"
  margin_left: float = 1
  margin_top: float = 1
  margin_right: float = 1
  margin_bottom: float = 1
  units: Literal["cm", "in"] = "in"
  
@dataclass(kw_only=True)
class CreateMseStepsParams:
  precision: float
  weights: list[float]
  dataset: list[list[float]]
  real_values: list[float]
  predicted_values: list[float]
  errors: list[float]
  mse: float
  print_settings: PrintSettings = field(default_factory=PrintSettings)
