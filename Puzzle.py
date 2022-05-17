# ---------------------------------------------------------------------------------
# Author: Allison Little
# Version: 1.0.0
# Graph Traversal Puzzle
#   Presents a path from source to destination given a puzzle board as a 2D array
# ---------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------
# Import min heap
# ---------------------------------------------------------------------------------
import heapq


# ---------------------------------------------------------------------------------
# Function returns minimum path from source to destination in puzzle board.
# ---------------------------------------------------------------------------------
def solve_puzzle(board, source, destination):
    MST = graph_traversal(board, source, destination)
    path = [destination]
    while destination != source:
        destination, distance = MST[destination]
        path.append(destination)
    path.reverse()

    return path


# ---------------------------------------------------------------------------------
# Function utilizes Prim's algorithm graph traversal and returns tree containing
#   the shortest path from the source to the destination.
# ---------------------------------------------------------------------------------
def graph_traversal(board, source, destination):
    visited = []
    distances = initialize_distances(board)
    MST = {}

    # Initialize source node
    distances[source] = 0
    priority_queue = [(0, source, source)]

    while destination not in visited:
        node_distance, node, previous_node = heapq.heappop(priority_queue)
        if node_distance > distances[node]:
            continue
        visited.append(node)
        if node != previous_node:
            MST[node] = (previous_node, node_distance)
        neighbors = node_neighbors(board, node)
        for neighbor in neighbors:
            if node_distance + 1 < distances[neighbor]:
                distances[neighbor] = node_distance + 1
                heapq.heappush(priority_queue, (node_distance + 1, neighbor, node))

    return MST


# ---------------------------------------------------------------------------------
# Function returns a distance dictionary initialized to inf for all indices of board.
# ---------------------------------------------------------------------------------
def initialize_distances(board):
    distances = {}
    for row in range(len(board)):
        for column in range(len(board[0])):
            distances[(row, column)] = float('infinity')

    return distances


# ---------------------------------------------------------------------------------
# Function returns a list of all possible neighbors of an origin node.
# ---------------------------------------------------------------------------------
def node_neighbors(board, origin):
    neighbors = []
    neighbor_options = [
        (origin[0], origin[1] + 1),
        (origin[0], origin[1] - 1),
        (origin[0] + 1, origin[1]),
        (origin[0] - 1, origin[1])
    ]
    for option in neighbor_options:
        if check_valid_node(board, option):
            neighbors.append(option)

    return neighbors


# ---------------------------------------------------------------------------------
# Function returns False if node is not a valid not in puzzle, True otherwise.
# ---------------------------------------------------------------------------------
def check_valid_node(board, node):
    if node[0] < 0 or node[1] < 0:
        return False
    if node[0] >= len(board) or node[1] >= len(board[0]):
        return False
    return open_path(board, node)


# ---------------------------------------------------------------------------------
# Function returns False if node in board is impassable ('#'), True otherwise.
# ---------------------------------------------------------------------------------
def open_path(board, node):
    if board[node[0]][node[1]] == '#':
        return False
    return True


# Puzzle = [
#  ['-', '-', '-', '-', '-'],
#  ['-', '-', '#', '-', '-'],
#  ['-', '-', '-', '-', '-'],
#  ['#', '-', '#', '#', '-'],
#  ['-', '#', '-', '-', '-']
# ]
# print(solve_puzzle(Puzzle, (0, 2), (2, 2)))