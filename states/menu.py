"""
    menu.py
    Menu is a state that handles menu related actions. Menu inherits from State.
"""

import pygame
import global_settings as settings
import color
from states.state import State
from UI.button import Button

class Menu(State):
    def __init__(self) -> None:
        super().__init__()

    def process_input(self, events) -> None:
        super().process_input(events)
        
    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()
