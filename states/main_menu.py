"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

import pygame
from states.menu import Menu
import states.settings as settings

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.title = self.title_font.render("Arcade Suite!", True, (255, 255, 255))

    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()
        settings.window.blit(self.title, self.title.get_rect())