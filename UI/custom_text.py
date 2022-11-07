"""
    custom_text.py
    gives a default text configuration and handles loading the font
"""

import pygame

class CustomText:
    def __init__(self, pos:tuple[int, int], text: str, color: tuple[int, int, int], 
    font_size: int, font_family_path: str=None) -> None:

        pygame.font.init()
        self.font = pygame.font.Font(font_family_path, font_size)
        self.text = self.font.render(text, color=color, antialias=True)
        self.rect = self.text.get_rect(center=pos)
