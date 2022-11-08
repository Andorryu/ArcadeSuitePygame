"""
    main_menu.py
    MainMenu is a leaf state that does things that you would expect from a main menu. This
    state is the application's entry state. MainMenu inherits from menu which inherits from state.
"""

from states.menu import Menu
import states.settings as settings
import color
from UI.UI_layer import UILayer
from UI.button import Button
from UI.custom_text import CustomText

class MainMenu(Menu):
    def __init__(self) -> None:
        super().__init__()
        self.UI_layer = UILayer([
            Button(
                "fuck me!!!!",
                (settings.width/2, settings.height/2),
                color.BLACK,
                color.WHITE,
                24,
                (50, 20)
            )
        ])

    def update(self) -> None:
        super().update()

    def render(self) -> None:
        super().render()
        self.UI_layer.render()
        