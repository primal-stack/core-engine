from enum import Enum
from typing import Dict, List, Tuple

class LogLevel(Enum):
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4

class Logger:
    def __init__(self, log_level: LogLevel = LogLevel.INFO):
        self.log_level = log_level

    def debug(self, message: str) -> None:
        print(f"DEBUG: {message}")

    def info(self, message: str) -> None:
        print(f"INFO: {message}")

    def warning(self, message: str) -> None:
        print(f"WARNING: {message}")

    def error(self, message: str) -> None:
        print(f"ERROR: {message}")

class SortedDict(Dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._keys = list(self.keys())

    def __iter__(self):
        return iter(sorted(self._keys))

    def __getitem__(self, key):
        if key in self:
            return self[key]
        else:
            raise KeyError(key)

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float):
        return Vector2D(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float):
        return Vector2D(self.x / scalar, self.y / scalar)