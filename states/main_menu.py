"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

from states.menu import Menu
from states.settings import Settings
import global_settings as settings
import color
from UI.UI_layer import UILayer
from UI.button import Button

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.UI_layer = UILayer([
            Button(
                "Settings",
                (settings.width/2, settings.height/2),
                color.BLACK,
                color.WHITE,
                24,
                (50, 20),
                # callback must not contain arguments, thus it must be a lambda
                lambda: settings.change_state(Settings())
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
        