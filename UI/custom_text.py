"""
    custom_text.py
    gives a default text configuration and handles loading the font
"""

import pygame
import states.settings as settings
from UI.UI_element import UIElement

class CustomText:
    def __init__(self, text: str, pos:tuple[int, int], color: tuple[int, int, int], 
    font_size: int, font_family_path: str=None) -> None:

        pygame.font.init()
        self.font: pygame.font.Font = pygame.font.Font(font_family_path, font_size)
        self.surf: pygame.Surface = self.font.render(text, True, color)
        self.rect: pygame.Rect = self.surf.get_rect(center=pos)
        self.text = text
        self.pos = pos
        self.color = color
    
    def render(self) -> None:
        self.surf = self.font.render(self.text, True, self.color)
        settings.window.blit(self.surf, self.rect)
