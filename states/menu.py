"""
    menu.py
    Menu is a state that handles menu related actions. Menu inherits from State.
"""

from states.state import State

class Menu(State):
    def __init__(self) -> None:
        super().__init__()

    def process_input(self) -> None:
        super().process_input()
