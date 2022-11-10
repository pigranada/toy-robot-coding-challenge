# Toy Robot Coding Challenge

## Summary

Welcome to the Toy Robot Coding!

The toy robot coding is an application that simulates a robot moving on a table surface. The application have set of commands that controls the movement of the robot.

## How to start the application.

There is no prior installation needed to run the application as all the libraries used was built-in to Python 3. 

The application can be used in 2 ways:

1. Command line (Default)

    `$ python3 main.py`

2. File read

    `$ python3 main.py [-f | --file] FILENAME`

For more help, simply run `python3 main.py -h`

## How to use the application

### Command List

Here are the list of commands that will let the robot to do a certain actions.

1. `PLACE`

`PLACE` is the first command that needs to be issued in the application. This sets the initial location and facing orientation of the robot on the table surface.

Usage: `PLACE <x location>,<y location>,<facing orientation>`

Where:
- x location - the x coordinate on the table surface (0 - 5)
- y location - the y coordinate on the table surface (0 - 5)
- facing orientation - the position where the robot is facing.
    - NORTH
    - EAST
    - SOUTH
    - WEST

Example:

```
PLACE 1,1,NORTH
```

Explanation: The robot was placed to the (1,1) location of the table and the robot will be facing north.

2. `MOVE`

> NOTE: `MOVE` will not work if the robot is not yet placed on the table. Place the robot first by using `PLACE` before using this command.

`MOVE` is the command that will move the robot 1 step forward to where it is currently facing. It will avoid moving the robot outside the boundary of the table.

Usage: `MOVE`

Example:

 ```
 PLACE 1,1,NORTH
 MOVE
 ```

Explanation: The robot is placed to (1,1) location and it is facing north, then the robot will move 1 step forward towards north. The robot will move to (1,2) location of the table.

3. `LEFT`

> NOTE: `LEFT` will not work if the robot is not yet placed on the table. Place the robot first by using `PLACE` before using this command.

`LEFT` is the command that will turn the robot's facing orientation 1 step to the left.

Usage: `LEFT`

Example:

```
PLACE 1,1,NORTH
LEFT
```

Explanation: The robot was initially facing north and it is now facing toward west after turning it to the left.


4. `RIGHT`

> NOTE: `RIGHT` will not work if the robot is not yet placed on the table. Place the robot first by using `PLACE` before using this command.

`RIGHT` is the command that will turn the robot's facing orientation 1 step to the right.

Usage: `RIGHT`

Example:

```
PLACE 1,1,NORTH
RIGHT
```

Explanation: The robot was initially facing north and it is now facing toward east after turning it to the right.

5. `REPORT`

> NOTE: `REPORT` will not work if the robot is not yet placed on the table. Place the robot first by using `PLACE` before using this command.

`REPORT` is the command that will print the current location and facing orientation of the robot.

Usage: `REPORT`

Example:

```
PLACE 1,1,NORTH
REPORT
Output: 1,1,NORTH
```

Explanation: The robot was initially placed to (1,1) location of the table and it is facing north.

## Run unit test

The toy robot is using [pytest](https://docs.pytest.org) test framework for the unit testing of the toy robot.

1. (Optional) Install the `pytest` if it is not yet available.

    `$ pip install pytest`

    or

    `$ pip install -r requirements.txt`

2. Simply run the `pytests` command in the root folder.

    `pytest`
