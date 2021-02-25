from dataclasses import dataclass

@dataclass
class Street:
    name: str
    length: int
    start_intersection: int
    end_intersection: int

@dataclass
class Car:
    path: list
