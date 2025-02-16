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
import dropdown
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (136, 200, 255)
DARK_BLUE = (88, 177, 255)
BROWN_FLR = (92, 64, 51)

# Variables

#FOR CLOCK
next_step_time = 0
time_interval = 1
start_ticks = pygame.time.get_ticks()

#FOR DROPDOWN
options = ["thing1","thing2","thing3","thing4","thing5","thing6","thing7","thing8","thing9","thing10"]
modes = ["easy","medium","hard"]    




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

    #CAT
    cat = pygame.image.load("basecat.png")
    resized_cat = pygame.transform.scale(cat, (300, 250))
    screen.blit(resized_cat, (105, 150))


 
# Set the width and height of the screen [width, height]
size = (480, 640)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pet Tropica")

happiness_bar = happinessbar.HappinessBar(30,30,200,20,100)
todobutton = dropdown.Dropdown(30,220,100,50,options) 
todobutton2 = dropdown.Dropdown(30,260,100,50,options) 
todobutton3 = dropdown.Dropdown(30,2,100,50,options) 

 #for font
font = pygame.font.SysFont('georgia', 18)
text1 = font.render("To Do", True, (0,0,0))
text2 = font.render("Level", True, (0,0,0))
text3 = font.render("Update", True, (0,0,0))


text1_position = (50,410)
text2_position = (220,410)
text3_position= (380,410)

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
    baseBG()

    #draw happiness bar
    happiness_bar.draw(screen)
    todobutton2.draw(screen)
    todobutton3.draw(screen)
    todobutton.draw(screen)

    screen.blit(text1, text1_position)
    screen.blit(text2, text2_position)
    screen.blit(text3, text3_position)

    

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

 
# Close the window and quit.