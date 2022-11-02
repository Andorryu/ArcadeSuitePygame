"""
    app.py
    This file handles entry of the application. It holds the game loop and applies the fps from settings.py.
    Control is given to current_state (from settings.py).
"""

import os
import pygame
from state_machine.states.settings import current_state, fps, window, window_caption, running

# always center the game window
os.environ['SDL_VIDEO_CENTERED'] = '1'


class App:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(window_caption)
        self.clock = pygame.time.Clock()

    def process_input(self) -> None:
        # close program when user clicks x
        events = pygame.event.get()
        for event in events:
            # if the user clicks the x button
            if event.type == pygame.QUIT:
                self.running = False

        # process input from respective application states
        current_state.process_input()

    def update(self) -> None:
        current_state.update()

    def render(self) -> None:
        current_state.render()

    def run(self) -> None:
        while running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(fps)

app = App()
app.run()
pygame.quit()