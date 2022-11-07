"""
    button.py
    This class holds data related to button functionality and how they should be displayed
"""

import pygame
import color

class Button:
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
    def __init__(self, text: str, pos: tuple[int, int], font_size: int, primary_color: tuple[int, int, int],
        secondary_color: tuple[int, int, int], padding: tuple[int, int], active=True, selected=False, submitted=False):
        # set up button in its initial state
        pass

    # button states are updated in UILayer since they depend on other buttons

    def render(self):
        pass
