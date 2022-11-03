"""
    app.py
    This file handles entry of the application. It holds the game loop and applies the fps from settings.py.
    Control is given to current_state (from settings.py).
"""

import os
import pygame
# when importing static values that other files may change, you cant use 'from' keyword
import states.settings as settings

# always center the game window
os.environ['SDL_VIDEO_CENTERED'] = '1'


class App:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(settings.window_caption)
        self.clock = pygame.time.Clock()

    def process_input(self) -> None:
        # close program when user clicks x
        events = pygame.event.get()
        for event in events:
            # if the user clicks the x button
            if event.type == pygame.QUIT:
                settings.running = False

        # process input from respective application states
        settings.current_state.process_input()

    def update(self) -> None:
        settings.current_state.update()

    def render(self) -> None:
        settings.window.fill((0, 0, 0))
        settings.current_state.render()
        pygame.display.update()

    def run(self) -> None:
        while settings.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(settings.fps)

app = App()
app.run()
pygame.quit()