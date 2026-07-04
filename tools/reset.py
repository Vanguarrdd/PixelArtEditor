from editor.canvas import Canvas
import pygame

def reset(canvas):
    canvas.grid = [
        [canvas.default_color for _ in range(canvas.cols)]
        for _ in range(canvas.rows)
    ]

