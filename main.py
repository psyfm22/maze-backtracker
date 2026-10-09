maze = [
    "#####################",
    "#S....#.......#.....#",
    "#####.#.#####.#.###.#",
    "#.....#.....#.#...#.#",
    "#.#########.#.###.#.#",
    "#.#.......#.#.....#.#",
    "#.#.#####.#.#######.#",
    "#...#...#.#.........#",
    "###.#.#.#.#########.#",
    "#...#.#.#.....#.....#",
    "#.###.#.#####.#.###.#",
    "#.....#.....#...#...#",
    "#.#########.#####.###",
    "#.........#.........#",
    "#########.#.#########",
    "#.........#.........#",
    "#.###########.#####.#",
    "#.............#....E#",
    "#####################"
]

# Find the start and end positions
start = None
end = None
for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == "S":
            start = (row, col)
        if maze[row][col] == "E":
            end = (row, col)

# Positions the robot can move to
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

stack = [start]
visited = {start}

while stack:
    if stack[-1] == end:
        print("Found Ending")
        break

    nextFound = False
    #Find next unvisited cell
    for direction in directions:
        current = stack[-1]

        temp = (
            current[0] + direction[0],
            current[1] + direction[1]
        )

        # Check that the position is inside the maze
        if 0 <= temp[0] < len(maze):
            if 0 <= temp[1] < len(maze[temp[0]]):

                # Check that the cell is open and unvisited
                if maze[temp[0]][temp[1]] in ".E" and temp not in visited:
                    stack.append(temp)
                    visited.add(temp)
                    nextFound = True
                    break


    # Backtrack if no valid move was found
    if not nextFound:
        if len(stack) == 1:
            print("No route to the exit")
            break

        stack.pop()