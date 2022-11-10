from unittest import TestCase

from app.table import Table
from app.location import Location

class TableTest(TestCase):
    __table = None

    def setUp(self) -> None:
        self.__table = Table(5,5)
        return super().setUp()

    def test_check_valid_location_is_valid(self) -> None:
        """Test the check valid location to return True if the location is within the boundary of the table."""
        location = Location(0,0)
        is_valid = self.__table.check_valid_location(location)

        self.assertTrue(is_valid)

    def test_check_valid_location_out_of_bounds(self) -> None:
        """Test the check valid location to return False if the location is not within the boundary of the table."""
        location = Location(10, 10)
        is_valid = self.__table.check_valid_location(location)

        self.assertFalse(is_valid)

    def test_check_valid_location_negative(self) -> None:
        """Test the check valid location to return False if the location is outside the positive boundary of the table."""
        location = Location(-1, -1)
        is_valid = self.__table.check_valid_location(location)

        self.assertFalse(is_valid)
