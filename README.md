🚀 Moon Rover Navigation Simulator
This project simulates the navigation of robotic rovers deployed by ISRO on a rectangular plateau on the Moon. Each rover receives a sequence of commands to turn left, turn right, or move forward on a grid-based plateau.
The program processes rover instructions sequentially and outputs the final position and direction of each rover after executing all commands.

📌 Commands
The rover understands the following commands:
L → Turn left (90°)
R → Turn right (90°)
M → Move forward one grid point in the current direction
Directions supported:
N → North
E → East
S → South
W → West

📥 Input Format
The first line contains the upper-right coordinates of the plateau.
Each rover has two lines of input:
First line → Initial position (x y direction)
Second line → Command string containing L, R, M.

📥 Sample Input

5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

📤 Expected Output

1 3 N
5 1 E

⚙️ How the Program Works
The plateau grid is defined using the maximum coordinates.
Each rover starts at a given position and orientation.
The command string is processed step-by-step.
The rover updates its direction or moves forward accordingly.
The rover is restricted to remain within the plateau boundaries.
After executing all commands, the final position is printed.
