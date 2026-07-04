from editor.canvas import Canvas
from utils.constants import *
from editor.palette import Palette
from tools.pencil import Pencil
from tools.eraser import Eraser
from tools.reset import reset
import pygame

class Editor:
    def __init__(self):
        self.canvas = Canvas(ROWS, COLS, PIXEL_SIZE, CANVAS_X, CANVAS_Y)
        self.palette = Palette(SCREEN_WIDTH // 2 - (6 * (40 + 2)) // 2, 50,COLORS)
        self.eraser = Eraser()
        self.pencil = Pencil()
        self.current_tool = self.pencil

    def handle_events(self, events):
        self.palette.handle_events(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.current_tool = self.pencil
                if event.key == pygame.K_e:
                    self.current_tool = self.eraser
                if event.key == pygame.K_r:
                    reset(self.canvas) 

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    self.apply_tool(event.pos)

    def apply_tool(self, pos):
        result = self.canvas.mouse_to_grid(*pos)
        if result:
            row, col = result
            if self.current_tool == self.pencil:
                self.canvas.set_pixel(row, col, self.palette.selected_color)
            if self.current_tool == self.eraser:
                self.canvas.set_pixel(row, col, self.canvas.default_color)
    def draw(self, screen):
        self.canvas.draw_canvas(screen)
        self.palette.draw(screen)
