
import pygame
from vector.vector import Vector

# ADAPTION FUNCTIONS
# call these whenever the framework interacts with pygame
def ad(vector: Vector) -> Vector:
    return vector * resolution // space
def adx(x_val: int) -> int:
    return x_val * resolution.x // space.x
def ady(y_val: int) -> int:
    return y_val * resolution.y // space.y
# END ADAPTION FUNCTIONS
    
# APP-WIDE SETTINGS
# resolution scales (for _16BY9)
_1280X720 = 80
_1920X1080 = 120
_2400X1350 = 150

# screen ratios
_16BY9 = Vector(16, 9)

space_scale = _2400X1350
res_scale = _1280X720

# space and resolution should have the same ratio
space = _16BY9 * space_scale
resolution = _16BY9 * res_scale
window = pygame.display.set_mode(resolution.as_tuple())
icon = pygame.image.load("./img/joystick_icon.png")
fps = 60 # apply fps (done in app.py): self.clock.tick(fps)
window_caption = "Arcade Suite" # applied with: pygame.display.set_caption()
running = True # keeps game loop running when True, change to False to stop the game
# END APP-WIDE SETTINGS

# State Stuff

from states.state import State
from states.main_menu import MainMenu
from states.settings import Settings

# CALLBACK FUNCTIONS
# called when buttons are submitted
def change_state(new_state: State) -> None:
    global current_state
    current_state = new_state
def exit_program() -> None:
    global running
    running = False
# END CALLBACK FUNCTIONS

# current_state should be at the bottom of this file
current_state: State = MainMenu() # change this whenever the state is changed
