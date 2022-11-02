"""
    settings.py
    This file stores application-wide settings such as fps, window, and current_state as static variables
    and the settings menu state which allows control of some settings
"""
import pygame
from menu import Menu
from main_menu import MainMenu

# init app-wide settings
window = pygame.display.set_mode((1280, 720))
fps = 60
current_state = MainMenu()

class Settings(Menu):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()