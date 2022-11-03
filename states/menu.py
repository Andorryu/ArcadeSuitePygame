"""
    menu.py
    Menu is a state that handles menu related actions. Menu inherits from State.
"""

import pygame
import states.settings as settings
import color
from states.state import State
from UI.button import Button

class Menu(State):
    def __init__(self) -> None:
        super().__init__()
        pygame.font.init()
        # create default font and title
        self.title_font = pygame.font.Font(None, 80) # 'None' uses the default pygame font: freesansbold
        self.mouse_click = False
        self.mouse_pos: tuple[int, int] = None
        # populate this with all Buttons in your menu
        # the order of button_collection determines the submitting priority
        self.button_collection: list[Button] = None

    def process_input(self) -> None:
        super().process_input()
        self.mouse_click = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.BUTTON_LEFT == 1: # if player clicks with the left click
                self.mouse_click = True
        self.mouse_pos = pygame.mouse.get_pos()
        
    def update(self) -> None:
        super().update()

        # HANDLE BUTTONS
        self.selected = False
        # determine button.selected
        for button in self.button_collection:
            if button.rect.collidepoint(self.mouse_pos):
                self.selected = True
        # set color if selected
        for button in self.button_collection:
            if button.selected:
                button.set_background_color(color.WHITE)
                button.set_font_color(color.BLACK)
            else:
                button.set_background_color(color.BLACK)
                button.set_font_color(color.WHITE)
        # if user clicks, perform submit
        if self.mouse_click:
            # for every button in this menu
            for button in self.button_collection:
                # if button is selected
                if button.selected:
                    # perform its submit function
                    button.submit_handler()
        # END HANDLE BUTTONS

    def display(self) -> None:
        # for each button
        for button in self.button_collection:
            # draw clickable rect
            settings.window.fill(button.background_color, button.rect)
            settings.window.blit(button.text, button.text_rect)
