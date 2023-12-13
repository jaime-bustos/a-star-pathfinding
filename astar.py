import pygame #pygame is used for the visualization of astar
import math
from queue import PriorityQueue #used for the astar algorithm

#defining the window as a square of 800 x 800
WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
#setting the caption for the display
pygame.display.set_caption("A* path finding algorithm")

#defining the color codes to use for visualization
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

#building the visualization tool
#each node is each square in the grid
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE #we start with all white nodes
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col
