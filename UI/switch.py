
from collections.abc import Callable
from UI.UI_element import UIElement
from UI.custom_font import CustomFont
from UI.button import Button
from vector.vector import Vector
import global_settings as settings
import color

class Switch(UIElement):
    def __init__(self,
        texts: list[str]=["Button 1", "Button 2", "Button 3"],
        primary_color: tuple[int, int, int]=color.BLACK,
        secondary_color: tuple[int, int, int]=color.WHITE,
        font_size: int=80,
        font_family_path: str=None,
        padding: Vector=Vector(40, 40),
        callbacks: list[Callable[[None], None]]=[lambda: None, lambda: None, lambda: None],
        pos: Vector=(settings.space // 2),
        placement_mode: str="center",
    ) -> None:

        super().__init__()

        # Step 1: create fonts
        fonts: list[CustomFont] = []
        for btn_txt in texts:
            fonts.append(CustomFont(
                text = btn_txt,
                color = primary_color,
                font_size = font_size,
                font_family_path = font_family_path
            ))
        
        # Step 2: find longest text and get width value
        longest_font = CustomFont(text = "") # create font with empty string
        for font in fonts:
            if len(font.text) > len(longest_font.text):
                longest_font = font
        longest_text_width = longest_font.get_size_vector().x
        switch_width = padding*2 + longest_text_width

        # Step 3: create list of buttons where the padding is based on the longest text
        self.buttons: list[Button] = []
        pos_i = pos.copy()
        for btn_font in fonts:
            # calculate the padding for each button so that the total width is equal to switch_width
            btn_padding = padding
            btn_padding.x = switch_width - btn_font.get_size_vector().x
            self.buttons.append(Button(
                text = btn_font,
                pos = pos_i,
                placement_mode = placement_mode
            ))
            pos_i.y += padding.y*2 + btn_font.get_size_vector().y # increment pos

    def render(self) -> None:
        super().render()
        for button in self.buttons:
            button.render()
