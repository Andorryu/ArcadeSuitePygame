"""
    settings.py
    This module contains the settings menu state which allows control of some global settings
"""
from states.menu import Menu

class Settings(Menu):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()