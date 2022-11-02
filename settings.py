"""
    settings.py
    This file stores application-wide settings such as fps, window, and current_state as static variables
"""
import pygame
from state_machine.states.main_menu import MainMenu

# init app-wide settings
window = pygame.display.set_mode((1280, 720))
fps = 60
current_state = MainMenu()