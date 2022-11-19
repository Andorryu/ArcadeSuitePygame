
import pygame
from states.state import State
from states.main_menu import MainMenu
from states.settings import Settings
from vector.vector import Vector

# CALLBACK FUNCTIONS
# callback functions to be called when buttons are submitted
def change_state(new_state: State) -> None:
    global current_state
    current_state = new_state
def exit_program() -> None:
    global running
    running = False
# END CALLBACK FUNCTIONS

# adapts (translates) to pygame interpretable values
# call these whenever the framework interacts with pygame
def ad(vector: Vector) -> Vector:
    return vector * resolution // space
def adx(x_val: int) -> int:
    return x_val * resolution.x // space.x
def ady(y_val: int) -> int:
    return y_val * resolution.y // space.y
    
# init app-wide settings
# SCALE: scale of 80 makes 1280 x 720, 120 makes 1920 x 1080, 150 makes 2400 x 1350
scale = 120
space = Vector(16 * scale, 9 * scale)
resolution = Vector(1280, 720)
window = pygame.display.set_mode(resolution.as_tuple())
icon = pygame.image.load("./img/joystick_icon.png")
fps = 60 # apply fps (done in app.py): self.clock.tick(fps)
window_caption = "Arcade Suite" # applied with: pygame.display.set_caption()
running = True # keeps game loop running when True, change to False to stop the game

# current_state should be at the bottom of this file
current_state: State = Settings() # change this whenever the state is changed
