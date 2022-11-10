from .location import Location
from .table import Table
from app.types.facing_enum import Facing
from typing import Optional

class RobotNotPlacedException(Exception):
    pass

def check_robot_placed(func) -> None:
    """A decorator function to make sure that the robot is already placed."""
    def wrapper(*args):
        location = args[0].get_location()
        facing = args[0].get_facing()

        if not location or not facing:
            raise RobotNotPlacedException("The robot is not yet placed.")

        return func(*args)
        
    return wrapper

class Robot:
    """
    This class is the robot that moves on the observable table surface.
    """
    __table = None
    __location = None
    __facing = None

    def __init__(self, table: Table, location: Optional[Location] = None, facing: Optional[Facing] = None) -> None:
        self.__location = location
        self.__facing = facing
        self.__table = table

    def get_location(self) -> Location:
        """Get the current location of the robot."""
        return self.__location

    def set_location(self, location: Location) -> None:
        """Set the new location of the robot."""
        if not self.__table.check_valid_location(location):
            raise Exception("Invalid location set.")
            
        self.__location = location

    def get_facing(self) -> Facing:
        """Get the facing orientation of the robot."""
        return self.__facing

    def set_facing(self, facing: Facing) -> None:
        """Set the facing orientation of the robot."""
        self.__facing = facing

    def place(self, location: Location, facing: Facing) -> None:
        """
        Place the robot in the table with the given location and facing orientation.
        It will invalidate all the out-of-bound location and unsupported facing orientation.
        """      
        if self.__table.check_valid_location(location):
            self.__location = location
            self.__facing = facing

    @check_robot_placed
    def move(self) -> None:
        """
        Move the robot 1 step to the front based on their location and orientation. It will
        prevent the robot to move out-of-bounds.
        """
        next_location = self.__get_simulated_next_location()
        if self.__table.check_valid_location(next_location):
            self.__location = next_location

    @check_robot_placed
    def turn_left(self) -> None:
        """Turn the robot's orientation 1 step to the left."""
        if self.__facing == Facing.NORTH:
            self.__facing = Facing.WEST
        elif self.__facing == Facing.EAST:
            self.__facing = Facing.NORTH
        elif self.__facing == Facing.SOUTH:
            self.__facing = Facing.EAST
        elif self.__facing == Facing.WEST:
            self.__facing = Facing.SOUTH
    
    @check_robot_placed
    def turn_right(self) -> None:
        """Turn the robot's orientation 1 step to the right."""
        if self.__facing == Facing.NORTH:
            self.__facing = Facing.EAST
        elif self.__facing == Facing.EAST:
            self.__facing = Facing.SOUTH
        elif self.__facing == Facing.SOUTH:
            self.__facing = Facing.WEST
        elif self.__facing == Facing.WEST:
            self.__facing = Facing.NORTH

    @check_robot_placed
    def report(self) -> str:
        """Report the robot's state."""
        print(f'Output: {self.__location.get_x_location()},{self.__location.get_y_location()},{self.__facing.value}')

    def __get_simulated_next_location(self) -> Location:
        """Get the simulated next location of the robot based on its current location and facing orientation."""
        x_location = self.__location.get_x_location()
        y_location = self.__location.get_y_location()

        if self.__facing == Facing.NORTH:
            return Location(x_location, y_location + 1)

        if self.__facing == Facing.EAST:
            return Location(x_location + 1, y_location)

        if self.__facing == Facing.SOUTH:
            return Location(x_location, y_location - 1)

        if self.__facing == Facing.WEST:
            return Location(x_location - 1, y_location)