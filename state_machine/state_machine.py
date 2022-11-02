"""
    state_machine.py
    This class's purpose is to know what state the application is in and
    to handle the game loop actions based on the state of the application.
    Since state is static, any script can alter it.
"""
from states.main_menu import MainMenu

class StateMachine:
    
    # init objects of all states
    currentState = MainMenu

    def __init__(self) -> None:
        pass

    def process_input(self) -> None:
        pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass
