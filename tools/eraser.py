from utils.constants import *
import pygame

class Eraser:
    def draw(self, row, col, canvas):
        canvas.set_pixel(row, col, canvas.default_color)
