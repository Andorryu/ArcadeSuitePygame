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

# enum to distinguish between keyboard and mouse input
class InputType(Enum):
    KEYBOARD = auto
    MOUSE = auto

class UILayer:
    def __init__(self, UI_elements: list) -> None:
        self.input_mode = InputType.MOUSE
        self.UI_elements = UI_elements
        # init mouse info
        # (isMouseButton1Pressed?, x pos, y pos)
        self.mouse_info = (False, 0, 0)
    
    def process_input(self) -> None:
        events = pygame.event.get()
        for event in events:
            if event == pygame.MOUSEBUTTONDOWN:
                pass



    def update(self) -> None:
        if self.input_mode == InputType.MOUSE:
            pass


    def render(self) -> None:
        element: UIElement
        for element in self.UI_elements:
            element.render()
