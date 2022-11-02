"""
    app.py
    This file handles entry of the application. It holds the game loop and applies the fps from settings.py.
    Control is given to the settings object current_state.
"""

import os
import pygame
from settings import *

# always center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'


class App:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()

    def process_input(self) -> None:
        # uncomment for code that only checks for the most recent event
        # (pygame.event.get() is better)
        #event = pygame.event.poll()

        # close program when user clicks x
        events = pygame.event.get()
        for event in events:
            # if the user clicks the x button
            if event.type == pygame.QUIT:
                self.running = False

        # process input from respective application states
        current_state.process_input()

    def update(self) -> None:
        current_state.process_input()

    def render(self) -> None:
        current_state.process_input()

    def run(self) -> None:
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(fps)

app = App()
app.run()
pygame.quit()