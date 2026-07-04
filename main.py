from utils.constants import * 
from editor.canvas import Canvas
from editor.palette import Palette
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.running = True
        self.dt = 0
        self.clock = pygame.time.Clock()
        
        self.canvas = Canvas(ROWS, COLS, PIXEL_SIZE, CANVAS_X, CANVAS_Y)
        self.palette = Palette(SCREEN_WIDTH // 2 - (6 * (40 + 2)) // 2, 50,COLORS)
 
    def run(self) -> None:
        self.dt = self.clock.tick(FPS)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BG_COLOR)

            self.canvas.draw_canvas(self.screen)
            self.palette.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
     


if __name__ == "__main__":
    main = Main()
    main.run()
