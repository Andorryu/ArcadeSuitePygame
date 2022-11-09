
import pygame
from states.state import State
from states.main_menu import MainMenu

# callback functions to be called when buttons are submitted
def change_state(new_state: State):
    global current_state
    current_state = new_state
    
# init app-wide settings
width = 1280
height = 720
window = pygame.display.set_mode((width, height))
icon = pygame.image.load("./img/joystick_icon.png")
fps = 60 # apply fps (done in app.py): self.clock.tick(fps)
current_state: State = MainMenu() # change this whenever the state is changed
window_caption = "Arcade Suite" # applied with: pygame.display.set_caption()
running = True # keeps game loop running when True, change to False to stop the game
