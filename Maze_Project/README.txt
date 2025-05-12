# Maze Solver - BFS Approach

**Name:** Sujai Shanmugam  
**ID:** 231ADB016  

## Results
- 11x11 maze: sum of the coins: 18
- 31x31 maze: sum of the coins: 16
- 101x101 maze: sum of the coins: 22

## Algorithm
Breadth First Search (BFS) was used to solve the maze.

## Complexity Analysis
### Time Complexity:
- To find start point (worst case): O(N*M)
- Searching path: O(N*M)
- To calculate sum of the coins collected: O(C) where (C - number of coins)
- Overall: O(N*M + C) it is same as O(N*M) in Big-O terms.

### Space complexity: 
O(N*M) - worst case for visited matrix and BFS queue

## Additional Note
There is a file `dfs_maze.py` that was created by me using depth first search and that was additional file which I created for my self to check that approach.
