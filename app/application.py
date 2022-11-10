from io import TextIOWrapper

from app.simulator import Simulator
from app.table import Table

class Application:
    __simulator = None
    __table = None

    def __init__(self):
        self.__table = Table(5,5)
        self.__simulator = Simulator(self.__table)

    def start_using_command_line(self) -> None:
        """Start the toy robot application using input from command line"""
        while True:
            command = input()
            self.__simulator.process(command)

    def start_using_file(self, filename: str) -> None:
        """Start the toy robot application using command from file"""
        with open(filename, "r") as file:
            commands = self.__get_normalized_commands_from_file(file)

            for command in commands:
                self.__simulator.process(command)


    def __get_normalized_commands_from_file(self, file: TextIOWrapper):
        return [command.strip() for command in file.readlines()]
