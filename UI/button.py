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
    def __init__(self, text: str, pos: tuple[int, int], primary_color: tuple[int, int, int],
    secondary_color: tuple[int, int, int], font_size: int, padding: tuple[int, int], call_back: Callable[[None], None],
    active=True, selected=False, submitted=False) -> None:

        # set up button in its initial state
        self.text = CustomText(text, pos, primary_color, font_size)
        self.area = pygame.Surface((2*padding[0] + self.text.rect.width, 2*padding[1] + self.text.rect.height))
        self.area_rect = self.area.get_rect(center=pos)
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.call_back = call_back
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
