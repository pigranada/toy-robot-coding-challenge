from .location import Location

class Table:
    """
    Table class represent the lenght x width table where the robot can move.
    """
    __length = None
    __width = None

    def __init__(self, length: int = 5, width: int = 5) -> None:
        self.__length = length
        self.__width = width

    def check_valid_location(self, location: Location) -> bool:
        """ This check if the location is within the boundry of the table """
        x_coordinate = location.get_x_location()
        y_coordinate = location.get_y_location()
        return x_coordinate >= 0 and x_coordinate <= self.__length and y_coordinate >= 0 and y_coordinate <= self.__width