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
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (136, 200, 255)
DARK_BLUE = (88, 177, 255)
BROWN_FLR = (92, 64, 51)
 
pygame.init()

def baseBG():
    pygame.draw.rect(screen, DARK_BLUE, [0, 0, 40, 640])
    pygame.draw.rect(screen, DARK_BLUE, [80, 0, 40, 640])
    pygame.draw.rect(screen, DARK_BLUE, [160, 0, 40, 640])
    pygame.draw.rect(screen, DARK_BLUE, [240, 0, 40, 640])
    pygame.draw.rect(screen, DARK_BLUE, [320, 0, 40, 640])
    pygame.draw.rect(screen, DARK_BLUE, [400, 0, 40, 640])

    pygame.draw.line(screen, LIGHT_BLUE, [0, 266],[480, 266], 3)
    pygame.draw.line(screen, DARK_BLUE, [0, 272],[480, 272], 9)
    pygame.draw.line(screen, LIGHT_BLUE, [0, 278],[480, 278], 3)

    pygame.draw.rect(screen, BROWN_FLR, [0, 280, 480, 120])

    #Info Slot
    pygame.draw.rect(screen, WHITE, [0, 400, 480, 240])

 
# Set the width and height of the screen [width, height]
size = (480, 640)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pet Tropica")

happiness_bar = happinessbar.HappinessBar(50,50,300,30,100)
 
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
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(LIGHT_BLUE)


 
    # --- Drawing code should go here
    baseBG()
    happiness_bar.draw(screen)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
