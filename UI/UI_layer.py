"""
    UI_layer.py
    This class holds multiple UI elements, such as CustomText or Button objects, and 
    defines how they interact with each other. This class also defines how the buttons
    are mapped between each other. The goal is for the button selection to be controlled 
    through either mouse or keyboard input.
"""

import pygame
from enum import Enum, auto
from UI.UI_element import UIElement
from UI.button import Button

# enum to distinguish between keyboard and mouse input
class InputType(Enum):
    KEYBOARD = auto
    MOUSE = auto

class UILayer:
    def __init__(self, UI_elements: list) -> None:
        self.input_mode = InputType.MOUSE
        self.UI_elements = UI_elements
        self.mouse_down = False
        self.mouse_pos = (0, 0)
    
    def process_input(self, events) -> None:
        if self.mouse_down:
            self.mouse_down = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
        self.mouse_pos = pygame.mouse.get_pos()

    def update(self) -> None:
        # input mode is mouse
        if self.input_mode == InputType.MOUSE:
            self.handle_mouse_input_mode()

        # input mode is keyboard
        elif self.input_mode == InputType.KEYBOARD:
            pass

    def render(self) -> None:
        element: UIElement
        for element in self.UI_elements:
            element.render()

    def handle_mouse_input_mode(self) -> None:
        element: UIElement
        for element in self.UI_elements:
            if isinstance(element, Button):
                # selection
                if element.area_rect.collidepoint(self.mouse_pos):
                    element.selected = True
                else:
                    element.selected = False
                # submission
                if element.selected and self.mouse_down:
                    element.call_back()

