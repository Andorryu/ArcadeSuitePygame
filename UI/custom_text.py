"""
    custom_text.py
    gives a default text configuration and handles loading the font
"""

import pygame
import color
import global_settings as settings
from UI.UI_element import UIElement
from vector.vector import Vector

class CustomText:
    def __init__(self, text: str="text", pos: Vector=settings.space // 2, placement_mode: str="center", color: tuple[int, int, int]=color.WHITE, 
    font_size: int=80, font_family_path: str=None) -> None:

        pygame.font.init()
        self.font: pygame.font.Font = pygame.font.Font(font_family_path, settings.ady(font_size))
        self.surf: pygame.Surface = self.font.render(text, True, color)
        if placement_mode == "center":
            self.rect: pygame.Rect = self.surf.get_rect(center=settings.ad(pos).as_tuple())
        elif placement_mode == "topleft":
            self.rect: pygame.Rect = self.surf.get_rect(topleft=settings.ad(pos).as_tuple())

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
