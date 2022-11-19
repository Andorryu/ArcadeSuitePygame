"""
    custom_text.py
    gives a default text configuration and handles loading the font
"""

import pygame
import global_settings as settings
from UI.UI_element import UIElement
from vector.vector import Vector

class CustomText:
    def __init__(self, text: str, pos: Vector, color: tuple[int, int, int], 
    font_size: int, font_family_path: str=None) -> None:

        pygame.font.init()
        self.font: pygame.font.Font = pygame.font.Font(font_family_path, settings.ady(font_size))
        self.surf: pygame.Surface = self.font.render(text, True, color)
        self.rect: pygame.Rect = self.surf.get_rect(center=settings.ad(pos).as_tuple())
        self.rect_size_vector = Vector.from_tuple(self.rect.size)
        self.text = text
        self.pos = pos
        self.color = color
    
    def render(self, color=None) -> None:
        if color == None:
            color = self.color
        # only update color if it needs to be updated
        if self.color != color:
            self.surf = self.font.render(self.text, True, color)
            self.color = color
        settings.window.blit(self.surf, self.rect)
