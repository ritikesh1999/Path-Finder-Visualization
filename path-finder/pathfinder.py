import pygame
import math
from queue import PriorityQueue

from box import BOX
from algorithm import Algorithm
from drawutil import DrawUtil


WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path finding Algorithm")


class Path:

    def __init__(self, rows, width, grid = []):
        self.rows = rows
        self.width = width
        self.grid = grid

    def get_clicked_pos(self, pos):
        gap = self.width // self.rows
        y, x = pos

        row = y // gap
        col = x // gap

        return row, col

    def make_grid(self):
        self.grid = []
        gap = self.width // self.rows   # Size of one cell

        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                box = BOX(i, j, gap, self.rows)
                self.grid[i].append(box)
        

    def start(self, start, end):
        print("Waiting for inputs")

        self.make_grid()

        run = True
        
        drawutil = DrawUtil(WINDOW, self.grid, self.rows, self.width)

        algorithm = Algorithm(WINDOW, self.grid, self.rows, self.width, start, end)

        while run:
            drawutil.draw_screen()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if pygame.mouse.get_pressed()[0]:   # Left click
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_clicked_pos(pos)
                    box = self.grid[row][col]
                    if not start:
                        start = box
                        start.make_start()

                    elif not end and box != start:
                        end = box
                        end.make_end()

                    elif box != end and box != start:
                        box.make_barrier()
                
                elif pygame.mouse.get_pressed()[2]: # Right click
                    pos = pygame.mouse.get_pos()
                    row, col = self.get_clicked_pos(pos)
                    box = self.grid[row][col]
                    box.reset()
                    if box == start:
                        start = None
                    elif box == end:
                        end = None
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and start and end:
                        
                        for row in self.grid:
                            for box in row:
                                box.update_neighbors(self.grid)

                        algorithm.start_algo(start, end)

                    if event.key == pygame.K_c:     # Press C to clear grid
                        self.start(None, None)


def main(WIDTH):
    ROWS = 50

    path = Path(ROWS, WIDTH)
    path.start(None, None)

    pygame.quit()

if __name__ == "__main__":
    main(WIDTH)