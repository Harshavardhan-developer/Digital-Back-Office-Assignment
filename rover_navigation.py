# Function to change rover direction based on L or R command
def turn(direction, cmd):
    directions = ['N', 'E', 'S', 'W']
    idx = directions.index(direction)

    if cmd == 'L':
        idx = (idx - 1) % 4
    elif cmd == 'R':
        idx = (idx + 1) % 4

    return directions[idx]


# Function to move the rover one step forward
def move(x, y, direction):
    if direction == 'N':
        y += 1
    elif direction == 'S':
        y -= 1
    elif direction == 'E':
        x += 1
    elif direction == 'W':
        x -= 1

    return x, y


# Read plateau size
max_x, max_y = map(int, input().split())

# Process rovers sequentially
while True:
    try:
        # Read rover position
        x, y, direction = input().split()
        x, y = int(x), int(y)

        # Read command string
        commands = input().strip()

        # Execute commands
        for cmd in commands:
            if cmd in ('L', 'R'):
                direction = turn(direction, cmd)
            elif cmd == 'M':
                nx, ny = move(x, y, direction)

                # Keep rover inside plateau
                if 0 <= nx <= max_x and 0 <= ny <= max_y:
                    x, y = nx, ny

        # Print final rover position
        print(x, y, direction)

    except EOFError:
        break


