from .table import Table
from .robot import Robot
from .command_parser import CommandParser

class Simulator:
    """This class represent the simulation of the toy robot in a specified table."""
    __robot = None
    __parser = None

    def __init__(self, table: Table) -> None:
        self.__robot = Robot(table)
        self.__parser = CommandParser()

    def process(self, string_command: str) -> None:
        """This function accepts a input command that will be parsed and passed"""
        command = self.__parser.parse_command(string_command)

        try:
            command.invoke(self.__robot)
        except Exception as exception:
            print(exception)
