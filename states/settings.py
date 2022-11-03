"""
    settings.py
    This file stores application-wide settings such as fps, window, and current_state as static variables
    and the settings menu state which allows control of some settings
"""
import pygame
from states.menu import Menu
from states.main_menu import MainMenu

# init app-wide settings
window = pygame.display.set_mode((1280, 720))
fps = 60 # apply fps (done in app.py): self.clock.tick(fps)
current_state = MainMenu() # change this whenever the state is changed
window_caption = "Arcade Suite" # applied with: pygame.display.set_caption()
running = True # keeps game loop running when True, change to False to stop the game

class Settings(Menu):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()