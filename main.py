from utils.constants import * 
from editor.canvas import Canvas
from editor.palette import Palette
from editor.editor import Editor
import pygame

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.running = True
        self.dt = 0
        self.clock = pygame.time.Clock()
        
        self.editor = Editor()
        # self.canvas = Canvas(ROWS, COLS, PIXEL_SIZE, CANVAS_X, CANVAS_Y)
        # self.palette = Palette(SCREEN_WIDTH // 2 - (6 * (40 + 2)) // 2, 50,COLORS)
 
    def run(self) -> None:

        while self.running:
            self.dt = self.clock.tick(FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(BG_COLOR)

            self.editor.handle_events(events)
            self.editor.draw(self.screen)
            # self.canvas.draw_canvas(self.screen)
            # self.palette.draw(self.screen)
            pygame.display.flip()

        pygame.quit()
     


if __name__ == "__main__":
    main = Main()
    main.run()
