import pygame # pygame is used for the visualization of astar
import math
from queue import PriorityQueue # used for the astar algorithm

# defining the window as a square of 800 x 800
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
# setting the caption for the display
pygame.display.set_caption("A* path finding algorithm")

# defining the color codes to use for visualization
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# building the visualization tool
# each node is each square in the grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # we must keep track of coordinate positions
        self.x = row * width
        self.y = col * width
        self.color = WHITE # we start with all white nodes
        self.neighbors = [] 
        self.width = width
        self.total_rows = total_rows

    # this method tells us the position of the node on the grid
    def get_pos(self):
        # we are indexing by rows and cols, so a node at (6, 3) is at (row: 6, col: 4)
        return self.row, self.col
    
    # these methods tell us the state of the node as bool values
    def is_closed(self): # the node that is already considered by the algorithm
        return self.color == RED

    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self): # this node will be black
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE
    
    # these methods will change the state of the node
    def reset(self):
        self.color == WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    # a function to actually draw the node barriers
    def draw(self, win):
        pygame.draw.rec(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):
        return False
"""
Now we define the heuristics function
p1 and p2 are points 1 and 2
We will use Manhattan distance to determing the distance b/w these points
"""
def h(p1, p2):
    x1, y1 = p1 # for example, p1 = (2, 3)
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2) #

# now a function to build the grid
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i , j, gap, rows)
            grid[i].append(node)
    return grid
