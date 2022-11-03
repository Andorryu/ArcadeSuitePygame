"""
    button.py
    This class holds data related to button functionality and how they should be displayed,
    and functions that statically change the button in some way
    button.py and menu.py modules are fairly tightly coupled
"""

import pygame
import color

class Button:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int], text: str, font_size: int, submit_handler,
            primary_color=color.WHITE, secondary_color=color.BLACK, active=True, selected=False
        ) -> None:

        pygame.font.init() # init font module

        self.pos = pos
        self.text = text
        # SUBMIT HANDLER
        self.submit_handler = submit_handler # function to be called when button is submitted
        # END SUBMIT HANDLER

        # OPT PARAMS
        self.active = active
        self.selected = selected
        # COLOR PARAMS
        # these change in Menu
        self.background_color = secondary_color
        self.font_color = primary_color
        # END COLOR PARAMS
        # END OPT PARAMS

        # PYGAME PARAMS
        # create rect that obeys pos and size params
        self.rect = pygame.Rect(left_top_width_height = (
            pos[0] - size[0]/2,
            pos[1] - size[1]/2,
            size[0],
            size[1]
        ))
        # create font
        self.font = pygame.font.Font(None, font_size)
        # create text
        self.text_surface = self.font.render(text, True, self.font_color)
        self.text_rect = self.text_surface.get_rect(
            center=self.pos
        )
        # END PYGAME PARAMS

    def set_font_color(self, color) -> None:
        self.font_color = color
        self.text = self.font.render(self.text, True, self.font_color)
        self.text_rect = self.text_surface.get_rect(
            center=self.pos
        )

    def set_background_color(self, color) -> None:
        self.background_color = color
