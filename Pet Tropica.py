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
BROWN_CLT = (72, 52, 43)
LIGHT_BROWN_CLT = (119, 82, 64)
CREAM = (255, 253, 208)

# Variables
popup_visible = False

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
    cat = pygame.image.load("Images/basecat.png")
    resized_cat = pygame.transform.scale(cat, (300, 250))
    screen.blit(resized_cat, (105, 150))

    #BUTTON
    font = pygame.font.Font(None, 36)
    #accept_rect = pygame.Rect(200, 150, 200, 60)  # (x, y, width, height)
    #button_text = font.render("Accept", True, BLACK)
    #pygame.draw.rect(screen, LIGHT_BLUE, accept_rect, border_radius=30)  # Increase border_radius for rounder corners

    # Draw text inside the button (centered)
    #text_rect = button_text.get_rect(center=accept_rect.center)
    #screen.blit(button_text, text_rect)

    #POP UP WINDOW
    if popup_visible:
        popup_font = pygame.font.Font(None, 50)
        popup_rect = pygame.Rect(100, 70, 300, 500)
        pygame.draw.rect(screen, CREAM, popup_rect, border_radius=30)
        popup_text = popup_font.render("New Accessory", True, BLACK)
        popuptext_rect = popup_text.get_rect(midtop=(popup_rect.centerx, 90))
        screen.blit(popup_text, popuptext_rect)

def closetBG():
   #Define Room
   pygame.draw.polygon(screen, DARK_BLUE, [[0, 0],[480, 0],[380, 80],[100, 80]])
   pygame.draw.polygon(screen, BROWN_FLR,[[0, 400],[480, 400],[380, 280],[100, 280]])

   #Room Outline
   pygame.draw.polygon(screen, BLACK,[[0, 0],[100, 80],[100, 280],[0, 400]], 3)
   pygame.draw.polygon(screen, BLACK,[[480, 0],[380, 80],[380, 280],[480, 400]], 3)
   pygame.draw.polygon(screen, BLACK, [[0, 0],[480, 0],[380, 80],[100, 80]], 3)
   pygame.draw.polygon(screen, BLACK,[[0, 400],[480, 400],[380, 280],[100, 280]], 3)

   #Closet Left Side
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[10, 400],[40, 420],[40, 170],[10, 150]])
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[40, 420],[140, 320],[140, 90],[40, 170]])
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[140, 90],[40, 170],[10, 150],[110, 70]])

   #Closet Left Outline
   pygame.draw.polygon(screen, BROWN_CLT,[[10, 400],[40, 420],[40, 170],[10, 150]], 4)
   pygame.draw.polygon(screen, BROWN_CLT,[[40, 420],[140, 320],[140, 90],[40, 170]], 4)
   pygame.draw.polygon(screen, BROWN_CLT,[[140, 90],[40, 170],[10, 150],[110, 70]], 4)

   #Closet Right Side
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[470, 400],[440, 420],[440, 170],[470, 150]])
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[440, 420],[340, 320],[340, 90],[440, 170]])
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[340, 90],[440, 170],[470, 150],[370, 70]])


   #Closet Right Outline
   pygame.draw.polygon(screen, BROWN_CLT,[[470, 400],[440, 420],[440, 170],[470, 150]], 4)
   pygame.draw.polygon(screen, BROWN_CLT,[[440, 420],[340, 320],[340, 90],[440, 170]], 4)
   pygame.draw.polygon(screen, BROWN_CLT,[[340, 90],[440, 170],[470, 150],[370, 70]], 4)

   #Closet Middle
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[340, 90],[370, 70],[110, 70],[140, 90]])
   pygame.draw.polygon(screen, LIGHT_BROWN_CLT,[[140, 90],[340, 90],[340, 320],[140, 320]])
   
   #Closet Middle Outline
   pygame.draw.polygon(screen, BROWN_CLT,[[340, 90],[370, 70],[110, 70],[140, 90],[140, 320]], 4)
   pygame.draw.polygon(screen, BROWN_CLT,[[140, 90],[340, 90],[140, 320],[340, 320]], 4)

   #Info Slot
   pygame.draw.rect(screen, WHITE, [0, 400, 480, 240])

   #CAT
   cat = pygame.image.load("Images/basecat.png")
   resized_cat = pygame.transform.scale(cat, (300, 250))
   screen.blit(resized_cat, (105, 150))

   #BUTTON
   #font = pygame.font.Font(None, 36)
   #accept_rect = pygame.Rect(200, 150, 200, 60)  # (x, y, width, height)
   #button_text = font.render("Accept", True, BLACK)
   #pygame.draw.rect(screen, LIGHT_BLUE, accept_rect, border_radius=30)  # Increase border_radius for rounder corners

   # Draw text inside the button (centered)
   #text_rect = button_text.get_rect(center=accept_rect.center)
   #screen.blit(button_text, text_rect)

# Set the width and height of the screen [width, height]
size = (480, 640)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Pet Tropica")

happiness_bar = happinessbar.HappinessBar(30,30,200,20,100)

todobutton = dropdown.Dropdown(20,440,120,30,options) 
todobutton2 = dropdown.Dropdown(20,500,120,30,options) 
todobutton3 = dropdown.Dropdown(20,560,120,30,options) 

level = dropdown.Dropdown(170,440,140,30,modes) 
level2 = dropdown.Dropdown(170,500,140,30,modes) 
level3 = dropdown.Dropdown(170,560,140,30,modes) 




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
    baseBG()

    #draw happiness bar
    happiness_bar.draw(screen)
    #TO DO buttons
    todobutton2.draw(screen)
    todobutton3.draw(screen)
    todobutton.draw(screen)
    #mode button
    level.draw(screen)
    level2.draw(screen)
    level3.draw(screen)
    """
    screen.blit(text1, text1_position)
    screen.blit(text2, text2_position)
    screen.blit(text3, text3_position)"""

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
