"""
    button.py
    This class holds data related to button functionality and how they should be displayed
"""

from collections.abc import Callable
import pygame
import color
from UI.custom_text import CustomText
from UI.UI_element import UIElement
import global_settings as settings
from vector.vector import Vector

"""
    DESC:
        Button consists of a rectangle background with text centered inside. The 
        primary and secondary colors are swapped when the button is selected.
    PARAMS:
        * text - string of text centered in button.
        * pos - double of ints, refers to the center of the button.
        * font_size - size of the text in the button.
        * primary_color - triple of ints (R, G, B), describes the text color when 
        the button is not selected and the background color when the button is selected.
        * secondary_color - triple of ints (R, G, B), describes the background color 
        when the button is not selected and the text color when the button is selected.
"""
class Button(UIElement):
    def __init__(self, text: str="Button", pos: Vector=(settings.space // 2), placement_mode: str="center",
    primary_color: tuple[int, int, int]=color.BLACK, secondary_color: tuple[int, int, int]=color.WHITE, font_size: int=80, 
    padding: Vector=Vector(40, 40), callback: Callable[[None], None]=lambda: None, active=True, selected=False, submitted=False) -> None:

        # set up button in its initial state
        self.text = CustomText(
            text = text,
            pos = pos + padding if placement_mode == "topleft" else pos,
            placement_mode = placement_mode,
            color = primary_color,
            font_size = font_size
        )
        self.area = pygame.Surface((settings.ad(padding)*2 + self.text.rect_size_vector).as_tuple())
        if placement_mode == "center":
            self.area_rect = self.area.get_rect(center=settings.ad(pos).as_tuple())
        elif placement_mode == "topleft":
            self.area_rect = self.area.get_rect(topleft=settings.ad(pos).as_tuple())
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.call_back = callback
        self.active = active
        self.selected = selected
        self.submitted = submitted

    # button states are updated in UILayer since they depend on the states of other buttons

    def render(self) -> None:
        bg_color = self.primary_color if self.selected else self.secondary_color
        text_color = self.secondary_color if self.selected else self.primary_color
        # first, draw background rect
        settings.window.fill(bg_color, self.area_rect)
        # then, draw text
        self.text.render(text_color)
