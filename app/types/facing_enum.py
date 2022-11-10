from __future__ import annotations
from enum import Enum

FACING_ORDER = ('NORTH', 'EAST', 'SOUTH', 'WEST')
FACING_COUNT = 4

class Facing(Enum):
    """The enum class representing the support facing orientation."""
    NORTH = 'NORTH'
    EAST = 'EAST'
    SOUTH = 'SOUTH'
    WEST = 'WEST'

    
    
    @classmethod
    def from_str(cls, facing: str):
        """Create a FACING object based on the string value."""
        return cls.__members__[facing]

    def turn(self, step: int) -> Facing:
        new_index = FACING_ORDER.index(self.value) + step
        facing_value = FACING_ORDER[new_index % FACING_COUNT]
        return Facing.from_str(facing_value)