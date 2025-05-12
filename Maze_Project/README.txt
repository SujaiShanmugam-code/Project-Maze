Name: Sujai Shanmugam , 231ADB016

Answers: 18, 16, 22

11x11 maze: sum of the coins  :18
31x31 maze: sum of the coins  :16
101x101 maze: sum of the coins  :22

Algorithm used: Breadth First Search (BFS)

Time Complexity: (N & M are rows and columns)
To find start point (worst case): O(N*M)
Searching path: O(N*M)
To calculate sum of the coins collected: O(C)  where  (C - number of coins)
Overall: O(N*M + C) it is same as O(N*M) in Big-O terms.

Space complexity: O(N*M) - worst case for visited matrix and BFS queue

