# Name: Sujai Shanmugam, 231ADB016.

from collections import deque as dq  # For BFS queue

def read_maze(file_path):
    """
    Read the maze from a text file and return it as a 2D list.
    Each character represents a cell in the maze.
    S: It is the Starting point
    G: It is the Goal
    X: It is the Wall
    0-9: These are the Coins in the range between from zero to nine
    """
    maze = [] # list for characters
    with open(file_path, 'r') as file: # for only reading the file
        for line in file: # loop over the file
            maze.append(list(line.strip())) # strip newline characters and convert each & every line into list of characters and append in the list 'maze'
    return maze # return 2D maze list, after read the file and add characters into it.


def find_start(maze):
    """
    Find the starting point 'S' in the maze and return its coordinates which is rows and columns.
    """
    for i in range(len(maze)): # for loop over each row
        for j in range(len(maze[i])): # for each column
            if maze[i][j] == 'S': #  check  S found ? then return its row and column so, called coordinates.
                return i, j # index of the row and colum where S found


def is_valid_move(maze, row, col):
    """
    Check if a move to the given row and column is valid.
    If the row and column are within the maze boundaries and the cell is not a wall ('X') then the move is valid.
    """
    if row < 0 or col < 0: # check the index are outside the maze's valid range (negative)
        return False
    elif row >= len(maze) or col >= len(maze[0]): # check the row and column exceeds the maze's size
        return False
    elif maze[row][col] == 'X': # check the current position is a wall ('X')
        return False
    else:
        return True # return true if it is valid move (By passing above lines)!


def bfs_explore_maze(maze, start_row, start_col):
    """
    To find the shortest path from 'S' to 'G' using Breadth first search and collect the coins.
    Returns the number of steps and the total coins collected.
    """
    # 8 directions including diagonals (chatgpt used for to get the all directions)
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Top-left
        (-1, 1),  # Top-right
        (1, -1),  # Bottom-left
        (1, 1)    # Bottom-right
    ]

    rows = len(maze)
    col = len(maze[0])

    visited = []  # emtpy list for to store the visited
    for r in range(rows):  # Loop over each row
        row_visited = []  # Temporary list to hold visited info for each column in current row
        for c in range(col):  # Loop over each column
            row_visited.append(False)  # Initially mark all cells as not visited
        visited.append(row_visited)  # Add this row to the visited list

    queue = dq() # empty queue for BFS traversal
    # Add the starting position to the queue
    queue.append((start_row, start_col, 0, 0))  # the arguments are (current row, current column , number of steps and the total coins collected)

    visited[start_row][start_col] = True # mark as true to indentify that it was visited

    while queue:
        row, col, no_of_steps, coins = queue.pop()
        cell = maze[row][col]

        if cell.isdigit():  # If the cell contains a digit (coin)
            coins = coins + int(cell)  # Add the digit to the coins collected

        if cell == 'G': #check it is goal
            return no_of_steps, coins # return the number of steps adn the coins collected

        for move_row, move_column in moves:  # loop all 8 directions
            new_row = move_row + row  # Initialize the new row
            new_col = move_column + col # Initialize the new column

            if is_valid_move(maze, new_row, new_col) and not visited[new_row][new_col]: # check the new position is valid move
                visited[new_row][new_col] = True # mark the cell as visited
                queue.append((new_row, new_col, no_of_steps + 1, coins)) # add new position to the queue

    return -1, coins  # If the goal 'G' is not reachable from the start, return -1 steps and collected coins so far


def solve_maze(file_path):
    """
    Solve the maze using BFS and return steps and coins collected.
    """
    maze = read_maze(file_path) # read the maze
    start_row, start_col = find_start(maze) # find the index of row and column and store in variable start_row & start_col.
    coins = bfs_explore_maze(maze, start_row, start_col)
    return coins # return the collected coins.

def main():
    print("\nFINAL - PROJECT MAZE")
    print("Sujai Shanmugam , 231ADB016\n")

    file_path = "maze_11x11.txt"  # Name of the file , Initialized in file_path

    steps, coins = solve_maze(file_path)
    print("Number of step taken to reach the goal 'G' : ", steps) # print the no of steps
    print("Coins collected on the path:", coins) # print the coins in the output

    # Calculate the sum of digits in coins_collected
    total = 0
    for num in str(coins):
        total += int(num)
    print("Sum of collected coins:", total)

    print("\nThank you!") # Just for thanks :)


if __name__ == '__main__':
    main()
