# Name: Sujai Shanmugam , 231ADB016.


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


def explore_maze(maze, row, col, coins):
    """
    Iterative function to explore the maze and collect coins (0 to 9).
    Returns the total coins collected on the way out of the maze.
    """
    stack = [(row, col, coins)]  # Initialize a stack with the starting positions and coins collected
    total_coins = 0  # Initialize the variable to track the total coins collected

    while stack:  # Continue the loop as long as there are positions in the stack which is Initialized above (line 49)
        row, col, coins = stack.pop()  # Get the current position and coins collected from the stack

        if not is_valid_move(maze, row, col):  # Firstly Check if the current move is valid
            continue  # If not valid, skip to the next iteration

        cell = maze[row][col]  # Get the cell value at the current position

        if cell == 'G':  # Check If the cell is the goal
            total_coins += int(coins)  # Add the coins collected to the total as integer
            continue  # Skip to the next iteration

        if cell.isdigit():  # If the cell contains a digit (coin)
            coins = coins + cell  # Add the digit to the coins collected

        maze[row][col] = 'X'  # Mark the current cell as visited by replacing it with 'X'

        # Adding neighboring cells to the stack to check for all possible paths
        stack.append((row - 1, col, coins))  # Add the position above to the stack (up)
        stack.append((row + 1, col, coins))  # Add the position below to the stack (down)
        stack.append((row, col - 1, coins))  # Add the position to the left to the stack (left)
        stack.append((row, col + 1, coins))  # Add the position to the right to the stack (right)
        # not moving diagonally!

    return total_coins  # Return the total coins collected finally.


def solve_maze(file_path):
    """
    Solve the maze and return coins collected on the way out of the maze.
    """
    maze = read_maze(file_path) # read the maze
    start_row, start_col = find_start(maze) # find the index of row and column and store in variable start_row & start_col.
    coins = explore_maze(maze, start_row, start_col, '0')
    return coins # return the collected coins.


def main():

    print("\nFINAL - PROJECT MAZE")
    print("Sujai Shanmugam , 231ADB016\n")


    file_path = "maze_11x11.txt"  # Name of the file , Initialized in file_path

    coins = solve_maze(file_path) # get coins by calling solve_maze by passing file_path
    print("Coins collected on the path:", coins) # print coins in the output

    # Calculate the sum of digits in coins_collected
    total = 0
    for num in str(coins):
        total += int(num)
    print("Sum of collected coins:", total)

    print("\nThank you!") # Just for thanks :)

if __name__ == '__main__':
    main()
