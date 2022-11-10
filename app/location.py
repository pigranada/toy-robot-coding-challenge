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