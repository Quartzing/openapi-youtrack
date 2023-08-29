from enum import Enum


class IssueLinkDirection(str, Enum):
    BOTH = "BOTH"
    INWARD = "INWARD"
    OUTWARD = "OUTWARD"

    def __str__(self) -> str:
        return str(self.value)
