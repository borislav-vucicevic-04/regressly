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

@dataclass(kw_only=True)
class GradientDescentSettings:
  learning_rate: float
  batch_size: int
  epochs: int

@dataclass(kw_only=True)
class GradientDescentParams:
  learning_rate: float
  batch_size: int
  epochs: int
  weights: list[float]
  dataset:list[list[float]]
  real_values: list[float]

@dataclass(kw_only=True)
class GradientDescentResult:
  updated_weights: list[float]
  epoch_results: list[EpochResult]

@dataclass(kw_only=True)
class EpochResult:
  updated_weights: list[float]
  batch_results: list[MiniBatchGradientDescentResult]

@dataclass(kw_only=True)
class MiniBatchGradientDescentParams:
  learning_rate: float
  weights: list[float]
  batch:list[list[float]]
  batch_real_values: list[float]

@dataclass(kw_only=True) 
class MiniBatchGradientDescentResult:
  updated_weights: list[float]
  batch_gradient_components: list[list[float]]

@dataclass(kw_only=True)
class CreateGradientDescentStepsParams:
  weights: list[float]
  dataset: list[list[float]]
  real_values: list[float]
  predicted_values: list[float]
  errors: list[float]
  learning_rate: float
  gradient_components: list[list[float]]
  updated_weights: list[float]
  print_settings: PrintSettings = field(default_factory=PrintSettings)