"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

import pygame
from states.menu import Menu

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.font = pygame.font.Font(None) # 'None' uses the default pygame font: freesansbold

    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()