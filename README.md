# graph-traversal-puzzle
Python script that presents a path from source to destination given a puzzle board as a 2D array.
Utilizing Prim's algorithm, this script creates a Minimum Spanning Tree (MST) that includes the source and desitnation nodes.

A puzzle board is passed in the following form. '-' is a passable node in the puzzle while '#' is a blocker or wall.
Puzzle = [
 ['-', '-', '-', '-', '-'],
 ['-', '-', '#', '-', '-'],
 ['-', '-', '-', '-', '-'],
 ['#', '-', '#', '#', '-'],
 ['-', '#', '-', '-', '-']
]

The Python script will return a list of tuples representing the indices that will be passed through in a minimum path between source and destination.
It also returns a string of directions where L = left, R = right, D = down, U = up.

Example using the puzzle shown above:
solve_puzzle(Puzzle, (0, 2), (2, 2))

Returns:
([(0, 2), (0, 1), (1, 1), (2, 1), (2, 2)], 'LDDR')
