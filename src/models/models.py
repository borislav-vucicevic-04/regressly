from dataclasses import dataclass

@dataclass(kw_only=True)
class CreateMseStepsParams:
    weights: list[float]
    dataset: list[list[float]]
    real_values: list[float]
    predicted_values: list[float]
    errors: list[float]
    mse: float
