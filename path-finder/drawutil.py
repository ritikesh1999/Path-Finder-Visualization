import pygame
import math
from queue import PriorityQueue

WHITE   = (255, 255, 255)
GREY    = (128, 128, 128)

class DrawUtil:

    def __init__(self, WINDOW, grid, rows, width):
        self.WINDOW = WINDOW
        self.grid = grid
        self.rows = rows
        self.width = width
        

    def draw_grid(self):
        gap = self.width // self.rows
        
        for i in range(self.rows):
            pygame.draw.line(self.WINDOW, GREY, (0, i*gap), (self.width, i*gap))  # Horizontal Lines (x1, y) to (x2, y)
            for j in range(self.rows):
                pygame.draw.line(self.WINDOW, GREY, (j*gap, 0), (j*gap, self.width))  # Vertical Lines (x, y1) to (x, y2)


    # Draws Everything, main draw function
    def draw_screen(self):
        self.WINDOW.fill(WHITE)

        for row in self.grid:
            for box in row:
                box.draw(self.WINDOW)

        self.draw_grid() # Draw Lines
        pygame.display.update()
