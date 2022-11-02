"""
    app.py
    This file handles entry of the application. It holds the game loop and sets the fps
"""

import os
import pygame
from settings import window, fps
from state_machine.state_machine import StateMachine

# always center the window
os.environ['SDL_VIDEO_CENTERED'] = '1'

class App:
    def __init__(self) -> None:
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.state_handler = StateMachine()

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
        self.state_handler.process_input()

    def update(self) -> None:
        self.state_handler.update()

    def render(self) -> None:
        self.state_handler.render()

    def run(self) -> None:
        while self.running:
            self.process_input()
            self.update()
            self.render()
            self.clock.tick(fps)

app = App()
app.run()
pygame.quit()