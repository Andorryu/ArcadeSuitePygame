
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
        callbacks: list[Callable[[Button], None]]=[lambda: None, lambda: None, lambda: None],
        pos: Vector=(settings.space // 2),
        placement_mode: str="center"
    ) -> None:

        super().__init__()
        self.selected = False

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
            if font.get_size_vector().x > longest_font.get_size_vector().x:
                longest_font = font
        switch_width = padding.x*2 + longest_font.get_size_vector().x

        # Step 3: create list of buttons where the padding is based on the longest text
        self.buttons: list[Button] = []
        pos_i = pos.copy()
        for font in fonts:
            # calculate the padding for each button so that the total width is equal to switch_width
            btn_padding = padding.copy()
            btn_padding.x = switch_width - font.get_size_vector().x
            print(f"switch width = {switch_width}, padding = {btn_padding.x}, font width = {font.get_size_vector().x}")
            self.buttons.append(Button(
                text = font,
                pos = pos_i,
                placement_mode = placement_mode,
                primary_color = primary_color,
                secondary_color = secondary_color,
                font_size = font_size,
                padding = btn_padding,
                callback = callbacks[0] # first callback in list
            ))
            callbacks.append(callbacks.pop(0)) # move first callback to end of list
            pos_i.y += padding.y*2 + font.get_size_vector().y # increment pos

        for btn in self.buttons:
            print(settings.unadx(btn.rect.width))

    def render(self) -> None:
        super().render()
        for button in self.buttons:
            button.render()

    def unsubmit(self) -> None: 
        for button in self.buttons:
            button.submitted = False
