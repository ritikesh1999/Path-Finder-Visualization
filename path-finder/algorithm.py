import pygame
import math
from queue import PriorityQueue

from box import BOX
from drawutil import DrawUtil

class Algorithm:

    def __init__(self, WINDOW, grid, rows, width, start, end):
        self.WINDOW = WINDOW
        self.grid = grid
        self.rows = rows
        self.width = width
        self.start = start
        self.end = end
        

    def heurestic(self, point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return abs(x1 - x2) + abs(y1 - y2)

    def reconstruct_path(self, came_from, current, drawutil):
        while current in came_from:
            current = came_from[current]
            current.make_path()
            drawutil.draw_screen()


    def start_algo(self, start, end):

        drawutil = DrawUtil(self.WINDOW, self.grid, self.rows, self.width)

        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        came_from = {}

        g_score = {box: float("inf") for row in self.grid for box in row}
        g_score[start] = 0
        
        f_score = {box: float("inf") for row in self.grid for box in row}
        f_score[start] = self.heurestic(start.get_pos(), end.get_pos())

        open_set_hash = {start}

        while not open_set.empty():

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reconstruct_path(came_from, end, drawutil)
                end.make_end()
                start.make_start()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                   
                    g_score[neighbor] = temp_g_score
                    f_score[neighbor] = temp_g_score + self.heurestic(neighbor.get_pos(), end.get_pos())

                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()
            
            drawutil.draw_screen()

            if current != start:
                current.make_close()

        return False