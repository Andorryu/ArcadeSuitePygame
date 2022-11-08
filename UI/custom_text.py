"""
    custom_text.py
    gives a default text configuration and handles loading the font
"""

import pygame
from UI.UI_element import UIElement

class CustomText:
    def __init__(self, text: str, pos:tuple[int, int], color: tuple[int, int, int], 
    font_size: int, font_family_path: str=None) -> None:

        pygame.font.init()
        self.font: pygame.font.Font = pygame.font.Font(font_family_path, font_size)
        self.surf: pygame.Surface = self.font.render(text, color=color, antialias=True)
        self.rect: pygame.Rect = self.surf.get_rect(center=pos)
