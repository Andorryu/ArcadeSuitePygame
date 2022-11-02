"""
    state_machine.py
    This class's purpose is to know what state the application is in and
    to handle the game loop actions based on the state of the application.
    Since state is static, any script can alter it.
"""

from enum import Enum, unique, auto

@unique
class State(Enum):
    MAINMENU = auto()
    PONG = auto()


class StateMachine:
    
    state = State.PONG
    
    def __init__(self) -> None:
        pass

    def process_input(self) -> None:
        pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass
