from unittest import TestCase
from unittest.mock import MagicMock

from app.robot import Robot, RobotNotPlacedException
from app.location import Location
from app.types.facing_enum import Facing

class RobotTest(TestCase):
    __robot = None
    __mock_table = None

    def setUp(self) -> None:
        self.__mock_table = MagicMock()
        self.__robot = Robot(self.__mock_table)
        return super().setUp()

    def test_place_valid(self) -> None:
        """Test the robot to be placed if the location and facing orientation is valid."""
        self.__mock_table.check_valid_location.return_value = True
        location = Location(0,0)

        self.__robot.place(location, Facing.NORTH)

        self.assertEquals(location, self.__robot.get_location())
        self.assertEquals(Facing.NORTH, self.__robot.get_facing())

    def test_place_invalid_location(self) -> None:
        """Test the robot to not be placed when the location or facing orientation is invalid."""
        self.__mock_table.check_valid_location.return_value = False
        location = Location(3,3)
        self.__robot.place(location, Facing.NORTH)

        self.assertIsNone(self.__robot.get_location())
        self.assertIsNone(self.__robot.get_facing())

    def test_turn_left(self) -> None:
        """Test the robot to turn the facing orientation 1 step to the left."""
        location = Location(3,3)
        self.__robot.place(location, Facing.NORTH)

        self.__robot.turn_left()

        self.assertEquals(self.__robot.get_facing().value, Facing.WEST.value)

    def test_turn_right(self) -> None:
        """Test the robot to turn the facing orientation 1 step to the right."""
        location = Location(3,3)
        self.__robot.place(location, Facing.NORTH)
        
        self.__robot.turn_right()
        
        self.assertEquals(self.__robot.get_facing().value, Facing.EAST.value)

    def test_move_valid(self) -> None:
        """Test the robot move 1 step ahead based from its current location and facing orientation."""
        self.__mock_table.check_valid_location.return_value = True
        location = Location(3,3)
        self.__robot.place(location, Facing.NORTH)

        self.__robot.move()

        new_location = Location(3,4)
        self.__assert_location_equal(self.__robot.get_location(), new_location)

    def test_move_invalid(self) -> None:
        """Test the robot to not move when the next location is invalid."""
        location = Location(3,3)
        self.__robot.place(location, Facing.NORTH)
        self.__mock_table.check_valid_location.return_value = False

        self.__robot.move()

        expected_location = Location(3,3)
        self.__assert_location_equal(self.__robot.get_location(), expected_location)

    def test_move_not_place_robot_error(self) -> None:
        """Test the robot move to raise an exception if the robot is not yet placed."""
        with self.assertRaises(RobotNotPlacedException):
            self.__robot.move()

    def test_turn_right_not_place_robot_error(self) -> None:
        """Test the robot turn right to raise an exception if the robot is not yet placed."""
        with self.assertRaises(RobotNotPlacedException):
            self.__robot.turn_right()

    def test_turn_left_not_place_robot_error(self) -> None:
        """Test the robot turn left to raise an exception if the robot is not yet placed."""
        with self.assertRaises(RobotNotPlacedException):
            self.__robot.turn_left()

    def test_report_not_place_robot_error(self) -> None:
        """Test the robot report to raise an exception if the robot is not yet placed."""
        with self.assertRaises(RobotNotPlacedException):
            self.__robot.report()

    def __assert_location_equal(self, location1: Location, location2: Location) -> None:
        self.assertEqual(location1.get_x_location(), location2.get_x_location())
        self.assertEqual(location1.get_y_location(), location2.get_y_location())
        