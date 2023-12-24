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
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_start(self):
        self.color = ORANGE

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
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        # we check up, left, down, right to see if they are barriers
        # if they are not barriers, if not then we add them to a list of neighbors
        self.neighbors = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # going DOWN
            self.neighboars.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # going UP
            self.neighboars.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # going RIGHT
            self.neighboars.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # going LEFT
            self.neighboars.append(grid[self.row][self.col - 1])

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

def algorithm(draw, grid, start, end): # our algorithm function
    pass

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

# defining the fuction to draw the lines on the grid
def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)

    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()

# defining a function that determines the position of the mouse to the correlating node
def get_clicked_pos(pos, rows, width):
    gap = width // rows # gap is the width of each node on the grid
    y, x = pos

    row = y // gap
    col = x //gap
    return row, col

def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    started = False

    while run:
        draw(win, grid, ROWS, width)
        print("test")
        for event in pygame.event.get(): # looping through each event and checking them
            if event.type == pygame.QUIT: # is we click the x button on the window
                run = False

            # this if statement prevents any interference while the algorithm is running
            if started:
                continue

            if pygame.mouse.get_pressed()[0]: # if mouse was left clicked
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width) # the function we created
                node = grid[row][col] # our indeed spot in the grid
                if not start and node != end:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None

                if node == end:
                    end = Node

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not started:
                    # here we start running the algorithm
                    for row in grid:
                        for node in row:
                            node.update_neighbors()

                    algorithm(lambda: draw(win, grid, ROWS, width), grid, start, end)
        
    pygame.quit()

main(WIN, WIDTH)