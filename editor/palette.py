from utils.constants import *
import pygame

class Palette:
    def __init__(self, x, y, colors):
        self.colors = colors
        self.selected_color = colors[0]
        self.x = x
        self.y = y
        self.color_size = 40
        self.cols = 6

    def get_color_clicked(self, pos):
        for i, color in enumerate(self.colors):
            rows = i / self.cols 
            cols = i % self.cols

            x = self.x + cols * (self.color_size + 5)
            y = self.y + rows * (self.color_size + 5)

            dx = pos[0] - x
            dy = pos[1] - y

            if dx**2 + dy**2 <= (self.color_size // 2) ** 2:
                return color 
        return self.selected_color 

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected_color = self.get_color_clicked(event.pos)

    def draw(self, screen):
        for i, color in enumerate(self.colors):
            rows = i // self.cols 
            cols = i % self.cols
            x = self.x + cols * (self.color_size + 5)
            y = self.y + rows * (self.color_size + 5)
            
            pygame.draw.circle(screen, color, (x, y), self.color_size // 2, 20)
