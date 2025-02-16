"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import happinessbar
from home import baseBG, popup, todo
from closet import closetBG, buttons
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (136, 200, 255)
DARK_BLUE = (88, 177, 255)
BROWN_FLR = (92, 64, 51)
BROWN_CLT = (72, 52, 43)
LIGHT_BROWN_CLT = (119, 82, 64)
CREAM = (255, 253, 208)

mode = 0

# Variables
popup_visible = False
accessory = 0
happy = True

#FOR CLOCK
next_step_time = 0
time_interval = 1
start_ticks = pygame.time.get_ticks()  

pygame.init()

# Set the width and height of the screen [width, height]
size = (480, 640)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pet Tropica")

happiness_bar = happinessbar.HappinessBar(30,30,200,20,100)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            popup_visible = False  # Hide the popup when any key is pressed
 
    # --- Game logic should go here
    

    # -- CLOCK --
    current_time = (pygame.time.get_ticks()-start_ticks)/6000
    if current_time > next_step_time:
        next_step_time += time_interval
        happiness_bar.decrease_health(20)
        print(current_time)
    



    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHT_BLUE)

    # --- Drawing code should go here
    baseBG(screen)

    #draw happiness bar
    happiness_bar.draw(screen)

    popup(screen, popup_visible, accessory)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
