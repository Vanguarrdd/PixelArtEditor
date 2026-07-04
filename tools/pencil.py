from utils.constants import *
import pygame

class Pencil:
    def draw(self, row, col, canvas, color):
        canvas.set_pixel(row, col, color)



