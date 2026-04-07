from dataclasses import dataclass

@dataclass(frozen=True)
class Colors:
  WHITE: str = "#fefefe"
  GRAY: str = "#aeaeae"
  BLACK: str = "#131313"
  RED: str = "#ed2c2c"
  LIGHTRED: str = "#EF4444"
  GREEN: str = "#3f8d43"
  LIGHTGREEN: str = "#66BB6A"
  BLUE: str = "#1F6AA5"
  LIGHTBLUE: str = "#3B8ED0"


@dataclass(frozen=True)
class Spacing:
  PADX: int = 12
  PADY: int = 12

@dataclass(frozen=True)
class Fonts:
  APP_TITLE: str = ("Arial", 24, "bold")
  SECTION_TITLE: str = ("Arial", 14, "bold")
  LABEL: str = ("Arial", 13, "bold")