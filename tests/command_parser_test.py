from unittest import TestCase

import app.commands as commands
from app.command_parser import CommandParser, InvalidFormatException


class CommandParserTest(TestCase):
    __command_parser = None

    def setUp(self) -> None:
        self.__command_parser = CommandParser()
        return super().setUp()

    def test_parse_command_invalid_format(self) -> None:
        """Test the parse command to raise an exception when the format was wrong."""
        with self.assertRaises(InvalidFormatException):
            self.__command_parser.parse_command("+-+")

    def test_parse_command_invalid_command(self) -> None:
        """Test the parse command to raise an exception when invalid command was parsed."""
        with self.assertRaises(commands.InvalidCommandException):
            self.__command_parser.parse_command("HELLO")

    def test_parse_command_invalid_parameter_format(self) -> None:
        """Test the parse command to raise an exception when invalid PLACE format is detected."""
        with self.assertRaises(commands.InvalidParameterFormatException):
            self.__command_parser.parse_command("PLACE hello,why,what")

    def test_parse_command_place_valid(self) -> None:
        """Test the parse command to return place command commander."""
        command = self.__command_parser.parse_command("PLACE 1,2,NORTH")

        self.assertIsInstance(command, commands.PlaceCommand)

    def test_parse_command_move(self) -> None:
        """Test the parse command to return move command commander."""
        command = self.__command_parser.parse_command("MOVE")

        self.assertIsInstance(command, commands.MoveCommand)

    def test_parse_command_move_with_parameter_valid(self) -> None:
        """Test the parse command to return move command commander even if parameter is set."""
        command = self.__command_parser.parse_command("MOVE 1")

        self.assertIsInstance(command, commands.MoveCommand)

    def test_parse_command_right(self) -> None:
        """Test the parse command to return right command commander."""
        command = self.__command_parser.parse_command("RIGHT")

        self.assertIsInstance(command, commands.RightCommand)

    def test_parse_command_right_with_parameter_valid(self) -> None:
        """Test the parse command to return right command commander even if parameter is set."""
        command = self.__command_parser.parse_command("RIGHT 1")

        self.assertIsInstance(command, commands.RightCommand)

    def test_parse_command_left(self) -> None:
        """Test the parse command to return left command commander."""
        command = self.__command_parser.parse_command("LEFT")

        self.assertIsInstance(command, commands.LeftCommand)

    def test_parse_command_left_with_parameter_valid(self) -> None:
        """Test the parse command to return left command commander even if parameter is set."""
        command = self.__command_parser.parse_command("LEFT 1")

        self.assertIsInstance(command, commands.LeftCommand)

    def test_parse_command_report_with_parameter_valid(self) -> None:
        """Test the parse command to return report command commander even if parameter is set."""
        command = self.__command_parser.parse_command("REPORT 1")

        self.assertIsInstance(command, commands.ReportCommand)

    def test_parse_command_report(self) -> None:
        """Test the parse command to return report command commander."""
        command = self.__command_parser.parse_command("REPORT")

        self.assertIsInstance(command, commands.ReportCommand)