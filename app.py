"""
    app.py
    This file handles entry of the application.
"""

import os
import pygame

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

        events = pygame.event.get()
        for event in events:
            # if the user clicks the x button
            if event.type == pygame.QUIT:
                self.running = False

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass

    def run(self) -> None:
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(60)

app = App()
app.run()
pygame.quit()