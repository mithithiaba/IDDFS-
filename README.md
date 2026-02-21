# IDDFS-
Title:
Implementation of Iterative Deepening Depth-First Search (IDDFS) for Maze Path Finding

NAME : Thiaba Rahman Methi 
ID : 232002042

Course Title: Artificial Intelligence Lab 
Course Code: CSE-316   Section:232_D7

Problem:

You are given a 2D grid representing a maze, where each cell is either an empty space (0) or a wall (1). Your task is to implement a Python program that uses Iterative Deepening Depth-First Search (IDDFS) to determine whether a valid path exists from a given start cell to a specified target cell. You may move up, down, left, or right to adjacent empty cells, but you cannot pass through walls, and each cell may be visited only once during a single path exploration.

Solution:

I have used Iterative Deepening Depth-First Search (IDDFS), which combines Depth-First Search (DFS) and Breadth-First Search (BFS) advantages. The algorithm repeatedly performs depth-limited DFS, starting from depth 0 and increasing depth step by step until the goal is found or the maximum possible depth is reached.

Steps:

Start from the initial node.
Perform Depth-Limited Search (DLS) for the current depth.
If the goal is found, return the path.
If not, increase the depth and repeat.
If the maximum depth is reached without finding the goal, report that the path is not found.

Example Cases:

Case #1
Input:

4 4
1 0 1 0
1 1 1 0
0 0 1 1
1 1 0 1
Start: 0 0
Target: 2 3

Output:

Path found at depth 5 using IDDFS
Traversal Order: [(0,0), (1,0), (1,1), (1,2), (2,2), (2,3)]

Case #2
Input:

3 3
0 1 0
0 1 0
0 1 0
Start: 0 0
Target: 2 2

Output:

Path not found at max depth 6 using IDDFS 

