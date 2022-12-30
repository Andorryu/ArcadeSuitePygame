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
from UI.switch import Switch

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
            if isinstance(element, Switch):
                self.handle_switch(element)
            elif isinstance(element, Button):
                self.handle_button(element)

    def handle_button(self, button: Button):
                # selection
                self.handle_sel(button)
                # submission
                self.handle_sub(button)

    def handle_switch(self, switch: Switch):
        # first handle whether the individual buttons' are selected
        for button in switch.buttons:
            self.handle_sel(button)
        # then handle switch selection
        switch.selected = False
        for button in switch.buttons:
            if button.selected:
                switch.selected = True
        # if clicking switch
        if switch.selected and self.mouse_down:
            switch.unsubmit() # unsubmit all buttons in switch
        # then do individual button submissions
        for button in switch.buttons:
            if not button.submitted:
                self.handle_sub(button)
    
    def handle_sel(self, button: Button):
        if button.rect.collidepoint(self.mouse_pos):
            button.selected = True
        else:
            button.selected = False

    def handle_sub(self, button: Button):
        if button.selected and self.mouse_down:
            button.submitted = True
            print("Button submitted!")
            button.call_back()
