"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

from states.menu import Menu
import global_settings as settings
import color
from UI.UI_layer import UILayer
from UI.button import Button
from UI.custom_font import CustomFont
from vector.vector import Vector

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.UI_layer = UILayer([
            CustomFont.as_text(
                text = "Welcome!",
                pos = (settings.space // 2 - Vector(0, 500)),
                font_size = 140
            ),
            Button(
                text = "Play!",
                pos = (settings.space // 2 + Vector(0, 0)),
                font_size = 80,
                padding = Vector(200, 50),
                callback = lambda: None
            ),
            Button(
                text = "Settings",
                pos = (settings.space // 2 + Vector(0, 200)),
                padding = Vector(155, 50),
                callback = lambda: settings.change_state(Settings())
            ),
            Button(
                text = "Exit",
                pos = (settings.space // 2 + Vector(0, 400)),
                padding = Vector(214, 50),
                callback = lambda: settings.exit_program()
            )
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
        
from states.settings import Settings
        