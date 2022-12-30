"""
    button.py
    This class holds data related to button functionality and how they should be displayed
"""

from collections.abc import Callable
from typing import Union
import pygame
import color
from UI.custom_font import CustomFont
from UI.UI_element import UIElement
import global_settings as settings
from vector.vector import Vector

class Button(UIElement):
    def __init__(self,
        text: Union[str, CustomFont]="Button",
        pos: Vector=(settings.space // 2),
        placement_mode: str="center",
        primary_color: tuple[int, int, int]=color.BLACK,
        secondary_color: tuple[int, int, int]=color.WHITE,
        font_size: int=80, 
        padding: Vector=Vector(40, 40),
        callback: Callable[[None], None]=lambda: None,
        active=True, selected=False, submitted=False
    ) -> None:

        # Step 1: Create the font
        if isinstance(text, str):
            self.font = CustomFont(
                text = text,
                color = primary_color,
                font_size = font_size
            )
        else: # allow to pass in a font instead of a string
            self.font = text

        # Step 2: Create background surface and rect (based on font width and height)
        self.surf = pygame.Surface(settings.ad(padding*2 + self.font.get_size_vector()).as_tuple())
        print(f"padding: {padding.x}, font width: {self.font.get_size_vector().x}")
        if placement_mode == "center":
            self.rect = self.surf.get_rect(center=settings.ad(pos).as_tuple())
        elif placement_mode == "topleft":
            self.rect = self.surf.get_rect(topleft=settings.ad(pos).as_tuple())
        else:
            print("INVALID PLACEMENT MODE FOR BUTTON")

        # Step 3: Place the text
        if placement_mode == "center":
            self.pos = pos
        elif placement_mode == "topleft":
            self.pos = pos + padding
        
        self.font.place_text(
            pos = self.pos,
            placement_mode = placement_mode
        )

        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.call_back = callback
        self.active = active
        self.selected = selected
        self.submitted = submitted
    
    # render the button
    def render(self) -> None:
        bg_color = self.primary_color if self.selected or self.submitted else self.secondary_color
        text_color = self.secondary_color if self.selected or self.submitted else self.primary_color
        # first, draw background rect
        settings.window.fill(bg_color, self.rect)
        # then, draw text
        self.font.render(text_color)
