import logging
from abc import ABC, abstractmethod

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# # # ----- DIRECTION CLASSES ----- # # #

class Direction(ABC):
    @abstractmethod
    def move_forward(self, x, y):
        pass

    @abstractmethod
    def turn_left(self):
        pass

    @abstractmethod
    def turn_right(self):
        pass

class North(Direction):
    def move_forward(self, x, y):
        return x, y + 1

    def turn_left(self):
        return West()

    def turn_right(self):
        return East()


class East(Direction):
    def move_forward(self, x, y):
        return x + 1, y

    def turn_left(self):
        return North()

    def turn_right(self):
        return South()


class South(Direction):
    def move_forward(self, x, y):
        return x, y - 1

    def turn_left(self):
        return East()

    def turn_right(self):
        return West()


class West(Direction):
    def move_forward(self, x, y):
        return x - 1, y

    def turn_left(self):
        return South()

    def turn_right(self):
        return North()


# # # ----- COMMAND CLASSES ----- # # # 

class Command(ABC):
    @abstractmethod
    def execute(self, rover):
        pass


class MoveForward(Command):
    def execute(self, rover):
        rover.move_forward()


class TurnLeft(Command):
    def execute(self, rover):
        rover.turn_left()


class TurnRight(Command):
    def execute(self, rover):
        rover.turn_right()
        

# # # ----- GRID AND ROVER CLASSES ----- # # #

class Grid:
    def __init__(self, width, height, obstacles=[]):
        self.width = width
        self.height = height
        self.obstacles = obstacles

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles


class Rover:
    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid

    def move_forward(self):
        new_x, new_y = self.direction.move_forward(self.x, self.y)
        if 0 <= new_x < self.grid.width and 0 <= new_y < self.grid.height and not self.grid.has_obstacle(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        self.direction = self.direction.turn_left()

    def turn_right(self):
        self.direction = self.direction.turn_right()

    def report_status(self):
        direction_str = {North: 'North', East: 'East', South: 'South', West: 'West'}[type(self.direction)]
        return f"Rover is at ({self.x}, {self.y}) facing {direction_str}. No Obstacles detected."


# # # ----- USER INTERFACE ---- # # #

def initialize_rover():
    while True:
        try:
            print("\nInitializing the Rover...")
            x, y = map(int, input("Enter starting position (x, y): ").split(','))
            direction = input("Enter starting direction (N, S, E, W): ").upper()

            if direction not in ['N', 'E', 'S', 'W']:
                raise ValueError("Invalid direction entered")

            direction_map = {
                'N': North(),
                'E': East(),
                'S': South(),
                'W': West()
            }

            rover = Rover(x, y, direction_map[direction], grid)
            logging.info(f"Rover initialized at ({x}, {y}) facing {direction}")
            return rover
        except ValueError as e:
            logging.error(e)
            print("Invalid input. Please try again.")


def get_commands():
    command_strs = []
    while True:
        try:
            print("\nAvailable Commands:")
            print("M - Move Forward")
            print("L - Turn Left")
            print("R - Turn Right")
            print("Q - Quit and show final status")

            command = input("Enter command (M, L, R, Q): ").upper()

            if command not in ['M', 'L', 'R', 'Q']:
                raise ValueError("Invalid command entered")

            if command == 'Q':
                break

            command_strs.append(command)
        except ValueError as e:
            logging.error(e)
            print("Invalid command, Please try again.")
    return command_strs


# # # ----- Base ------ # # #

if __name__ == "__main__":
    grid = Grid(10, 10, obstacles=[(2, 2), (3, 5)])

    rover = initialize_rover()
    command_map = {'M': MoveForward, 'L': TurnLeft, 'R': TurnRight}
    command_strs = get_commands()

    for cmd_str in command_strs:
        try:
            command = command_map[cmd_str]
            command().execute(rover)
            logging.info(f"Executed command: {cmd_str}")
        except Exception as e:
            logging.error(f"Error executing command {cmd_str}: {e}")

    print("\n" + rover.report_status())
