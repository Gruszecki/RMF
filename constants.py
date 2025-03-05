from dataclasses import dataclass


@dataclass
class Gender:
    MALE: int = 0
    FEMALE: int = 1
    OTHER: int = 2


@dataclass
class AgeRange:
    JUNIOR: int = 0
    MID: int = 1
    SENIOR: int = 2
