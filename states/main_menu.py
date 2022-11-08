"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

from states.menu import Menu
import states.settings as settings
import color
from UI.button import Button

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()