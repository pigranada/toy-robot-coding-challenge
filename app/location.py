from __future__ import annotations
from .types.facing_enum import Facing

class Location:
    __x_location = None
    __y_location = None

    def __init__(self, x_location: int, y_location: int) -> None:
        self.__x_location = x_location
        self.__y_location = y_location

    def get_x_location(self) -> int:
        """
        Get the x location.
        """
        return self.__x_location

    def get_y_location(self) -> int:
        """
        Get the y location.
        """
        return self.__y_location

    def get_simulated_next_location(self, facing: Facing) -> Location:
        x = self.__x_location
        y = self.__y_location

        if facing == Facing.NORTH:
            y += 1

        if facing == Facing.EAST:
            x += 1

        if facing == Facing.SOUTH:
            y -= 1

        if facing == Facing.WEST:
            x -= 1

        return Location(x,y)