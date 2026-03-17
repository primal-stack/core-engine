# utils.py
from typing import List, Optional, Tuple

def calculate_distance(point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
    """Calculate the Euclidean distance between two points."""
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def parse_coordinates(coords: str) -> Tuple[float, float]:
    """Parse a string of comma-separated coordinates into a tuple of floats."""
    try:
        x, y = map(float, coords.split(","))
        return x, y
    except ValueError:
        raise ValueError("Invalid coordinates")

def split_list(lst: List[str], sep: str) -> List[List[str]]:
    """Split a list of strings into sublists based on a separator."""
    return [sublist.split(sep) for sublist in lst]

def uniqueify_list(lst: List[str]) -> List[str]:
    """Remove duplicates from a list while preserving order."""
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]