"""
    menu.py
    Menu is a state that handles menu related actions. Menu inherits from State.
"""

import pygame
from states.state import State

class Menu(State):
    def __init__(self) -> None:
        super().__init__()
        pygame.init()
        # create default font and title
        self.title_font = pygame.font.Font(None, 50) # 'None' uses the default pygame font: freesansbold

    def process_input(self) -> None:
        super().process_input()
        
