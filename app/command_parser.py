import re
import app.commands as commands

from app.location import Location
from app.types.facing_enum import Facing

class InvalidFormatException(Exception):
    pass

class CommandParser:

    supported_command = ['PLACE', 'MOVE', 'LEFT', 'RIGHT', 'REPORT']

    def parse_command(self, command: str) -> commands.Command:
        """Parsed the string command pass and return the appropriate commander."""
        parsed = re.match(r'^(\w+)(\s?)(.*)$', command)

        if not parsed:
            raise InvalidFormatException("Invalid command format found.")

        parsed_command = parsed.group(1)

        if parsed_command not in self.supported_command:
            raise commands.InvalidCommandException("Invalid command found.")
        
        if parsed_command == 'PLACE':
            parsed_parameters = parsed.group(3)
            parameters = parsed_parameters.split(",")

            if not commands.PlaceCommand.valid_parameters(parameters):
                raise commands.InvalidParameterFormatException("Invalid format found for PLACE command.")

            location = Location(int(parameters[0]),int(parameters[1]))
            facing = Facing.from_str(parameters[2])

            return commands.PlaceCommand(location, facing)
        
        if parsed_command == 'MOVE':
            return commands.MoveCommand()

        if parsed_command == 'LEFT':
            return commands.LeftCommand()

        if parsed_command == 'RIGHT':
            return commands.RightCommand()

        if parsed_command == 'REPORT':
            return commands.ReportCommand()