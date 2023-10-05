# Mars Rover Simulation

## Table of Contents
1. [Description](#description)
2. [Getting Started](#getting-started)
3. [Usage](#usage)
4. [Class Diagram](#class-diagram)

<a name="description"></a>
## Description
This is a simple simulation of a Mars Rover that can navigate a grid-based terrain using object-oriented programming (OOP) principles and design patterns. The Rover is designed to avoid obstacles and stay within the grid's boundaries.

<a name="getting-started"></a>
## Getting Started
To get started with the simulation, you need a Python environment.

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your_username/mars_rover_simulation.git
```

2. Navigate to the cloned directory:
```bash
cd mars_rover_simulation
```

<a name="usage"></a>
## Usage
```bash
python mars_rover.py
```

Upon running the script, the Rover will start at a predefined point and will execute a series of commands. The Rover's journey will be printed on the console.

<a name="class-diagram"></a>
## Class Diagram

```
              +-----------+
              | Navigator |
              +-----------+
                    ^
                    |
    +-----------+   |   +----------+
    | Command   |---+---| MarsRover|
    +-----------+       +----------+
```

### Classes:

1. **MarsRover**: The main rover object responsible for maintaining the state of the rover (position, direction).

2. **Navigator**: Interface class that has methods `turn_left`, `turn_right`, and `move_forward`.

3. **Command**: An interpreter pattern class to navigate the Rover based on string-based commands like "L", "R", and "M" for left, right, and move respectively.


---

Please note: The simulation avoids using if-else constructs in favor of polymorphism and design patterns. The Command design pattern allows us to add more commands in the future with ease. The Navigator interface lets us add more navigation mechanisms in the future without changing the existing code.

---

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

---

This README is a basic guide to the Mars Rover Simulation. The provided class structure and design patterns ensure the project's scalability and maintainability.
