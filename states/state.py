"""
    state.py
    The class State is an interface for every possible state. Possible states include (but are
    not limited to) MainMenu, Pong, PacMan, Options.
"""

class State:
    def __init__(self) -> None:
        pass
    
    def process_input(self, events) -> None:
        pass

    def update(self) -> None:
        pass

    def render(self) -> None:
        pass
