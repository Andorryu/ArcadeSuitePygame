"""
    custom_font.py

    This class can be used in two ways:

    First, you can call the constructor to create a pygame font, (without placing the text on the screen) Then
    you can call the place_text method on your font to place it on the screen. An error is raised if you try to
    render the font without placing it on the screen first
    
    Second you can call the as_text class method to create the font and place the text on the screen in one fell
    swoop.

    The reason for separating this functionality is so that the size of the font (width and height in pixels)
    can be calculated from the font (with self.get_size_vector()) before placing it on the screen
"""

import pygame
import color
import global_settings as settings
from UI.UI_element import UIElement
from vector.vector import Vector

class CustomFont:

    # create custom font without placing it on the screen
    # use self.get_size_vector() to return a vector containing the size of the font before rendering it
    def __init__(self,
        text: str="text",
        color: tuple[int, int, int]=color.WHITE,
        font_size: int=80,
        font_family_path: str=None
    ) -> None:

        pygame.font.init()
        self.pygame_font: pygame.font.Font = pygame.font.Font(font_family_path, settings.ady(font_size))
        self.surf: pygame.Surface = self.pygame_font.render(text, True, color)
        self.text = text
        self.color = color

    # create font and place text for it in one go
    @classmethod
    def as_text(cls,
        text: str="text",
        color: tuple[int, int, int]=color.WHITE,
        font_size: int=80,
        font_family_path: str=None,
        pos: Vector=settings.space // 2,
        placement_mode="center"
    ):
        custom_font = cls(text, color, font_size, font_family_path)
        custom_font.place_text(pos, placement_mode)
        return custom_font

    # place the previously created font as text on the screen
    def place_text(self,
        pos: Vector=settings.space // 2,
        placement_mode="center"
    ) -> None:
        # create self.rect that has desired position so that text can be placed on screen
        if placement_mode == "center":
            self.rect = self.surf.get_rect(center=settings.ad(pos).as_tuple())
        elif placement_mode == "topleft":
            self.rect = self.surf.get_rect(topleft=settings.ad(pos).as_tuple())
        else:
            print("INVALID PLACEMENT MODE FOR CUSTOM_FONT")

    def get_size_vector(self) -> Vector:
        return settings.unad(Vector(self.surf.get_rect().width, self.surf.get_rect().height))

    # render is called in game loop
    def render(self, color=None) -> None:
        # use same color if none is specified
        if color == None:
            color = self.color
        # only update color if it needs to be updated
        if self.color != color:
            self.surf = self.pygame_font.render(self.text, True, color)
            self.color = color
        # error handling - failed to place text
        try:
            settings.window.blit(self.surf, self.rect)
        except:
            print("CustomFont.render() failed, use place_text() method to place your text on the screen first.")
