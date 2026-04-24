from dataclasses import dataclass
from typing import Literal

@dataclass(kw_only=True)
class CreateMseStepsParams:
  precision: float
  weights: list[float]
  dataset: list[list[float]]
  real_values: list[float]
  predicted_values: list[float]
  errors: list[float]
  mse: float

@dataclass(kw_only=True)
class PrintSettings:
  page_orientation: Literal["horizontal", "vertical"] = "vertical"
  page_size: Literal["A3", "A4", "A5", "B4", "B5", "letter", "legal", "ledger"] = "A4"
  margin_left: float = 1
  margin_top: float = 1
  margin_right: float = 1
  margin_bottom: float = 1
  units: Literal["cm", "inch"] = "inch"