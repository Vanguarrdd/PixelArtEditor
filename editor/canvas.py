from utils.constants import * 
import pygame

class Canvas:
    def __init__(self, rows: int, cols: int, pixel_size: int, canvas_x: float, canvas_y: float):
        self.rows = rows
        self.cols = cols 

        self.pixel_size = pixel_size
        self.canvas_x = canvas_x
        self.canvas_y = canvas_y

        self.cell_size = CELL_SIZE

        self.default_color = (255, 255, 255)

        self.grid = [
            [self.default_color for _ in range(cols)]
            for _ in range(rows)
        ]
    
    # mouse pos to grid pos
    def mouse_to_grid(self, mouse_x: int, mouse_y: int):
        col = (mouse_x - mouse_y) // self.cell_size
        row = (mouse_y - mouse_x) // self.cell_size

        if 0 <= row < self.rows and 0 <= col < self.cols:
            return int(row), int(col)
        return None

    def get_pixel(self, row: int, col: int):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def set_pixel(self, row: int, col: int, color):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = color

    def draw_pixel_square(self, screen: pygame.Surface, row: int, col: int, color):
        x = self.canvas_x + col * self.cell_size
        y = self.canvas_y + row * self.cell_size

        pygame.draw.rect(screen, color, (x, y, self.pixel_size, self.pixel_size))

    def draw_canvas(self, screen: pygame.Surface):
        for row in range(self.rows):
            for col in range(self.cols):
                color = self.grid[row][col]
                self.draw_pixel_square(screen, row, col, color)



