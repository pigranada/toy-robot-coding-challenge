from enum import Enum

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
