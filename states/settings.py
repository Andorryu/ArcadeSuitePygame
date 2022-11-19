"""
    settings.py
    This module contains the settings menu state which allows control of some global settings
"""
import color
from states.menu import Menu
from UI.UI_layer import UILayer
from UI.button import Button
from UI.custom_text import CustomText
from vector.vector import Vector
import global_settings as settings

class Settings(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.UI_layer = UILayer([
            CustomText(
                text = "Settings",
                pos = (settings.space // 2 - Vector(0, 500)),
                color = color.WHITE,
                font_size = 140
            ),
            Button(
                text = "Back",
                pos = (Vector(100, 100)),
                placement_mode = "topleft",
                font_size = 60,
                callback = lambda: settings.change_state(MainMenu())
            ),
        ])

    def process_input(self, events) -> None:
        super().process_input(events)
        self.UI_layer.process_input(events)
    
    def update(self) -> None:
        super().update()
        self.UI_layer.update()

    def render(self) -> None:
        super().render()
        self.UI_layer.render()

from states.main_menu import MainMenu
