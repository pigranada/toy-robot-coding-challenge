from abc import ABCMeta, abstractmethod
from typing import List
from .location import Location
from .robot import Robot
from .types.facing_enum import Facing

class InvalidCommandException(Exception):
    pass

class InvalidParameterFormatException(Exception):
    pass

class Command(metaclass=ABCMeta):

    @abstractmethod
    def invoke(self, robot: Robot):
        pass

class MoveCommand(Command):

    def invoke(self, robot: Robot) -> None:
        robot.move()

class PlaceCommand(Command):

    __location = None
    __facing = None

    def __init__(self, location: Location, facing: Facing) -> bool:
        self.__location = location
        self.__facing = facing

    def invoke(self, robot: Robot):
        robot.set_location(self.__location)
        robot.set_facing(self.__facing)

    @staticmethod
    def valid_parameters(parameters: List[str]) -> bool:
        return (
            parameters[0].isdigit() and
            parameters[1].isdigit() and
            parameters[2] in [facing.value for facing in Facing]
        )

class LeftCommand(Command):

    def invoke(self, robot: Robot):
        robot.turn_left()

class RightCommand(Command):

    def invoke(self, robot: Robot):
        robot.turn_right()

class ReportCommand(Command):
    
    def invoke(self, robot: Robot):
        robot.report()