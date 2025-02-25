import pygame
import happinessbar
import dropdown
import modes
import taskComplete
from home import baseBG, popup
from closet import closetBG, hats, cat
import coins
 
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
BUTTON_BDY = (255, 206, 134)
BUTTON = (161, 122, 105)

# Variables
popup_visible = False
accessory = 0
happy = True
a_coins = 0


mouse_clicked = False

# FOR CLOCK
next_step_time = 0
time_interval = 1
start_ticks = pygame.time.get_ticks()

pygame.init()

current_cat = pygame.image.load("Images/basecat.png").convert_alpha()
tired_cat = pygame.image.load("Images/tiredcat.png").convert_alpha()
resized_selectedcat = pygame.transform.scale(current_cat, (150, 120))
resized_tiredcat = pygame.transform.scale(tired_cat,(100,100))

catRect = resized_selectedcat.get_rect()
catRect.topleft = (150,280)

tiredRect = resized_tiredcat.get_rect()
tiredRect.topleft = (90,220)

selected_cat_image = "Images/basecat.png"

# Function to scale images while maintaining aspect ratio
def scale_image(image, max_width, max_height):
    original_width, original_height = image.get_size()
    width_ratio = max_width / original_width
    height_ratio = max_height / original_height
    scale_factor = min(width_ratio, height_ratio)
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    return pygame.transform.scale(image, (new_width, new_height))

def buttons():
    home_rect = pygame.draw.rect(screen, BUTTON_BDY, [360, 600, 45, 30])
    home_image = pygame.image.load("Images/home.png")
    home_image_scaled = scale_image(home_image, 40, 25)
    home_image_pos = (
        home_rect.x + (45 - home_image_scaled.get_width()) // 2,
        home_rect.y + (30 - home_image_scaled.get_height()) // 2
    )
    screen.blit(home_image_scaled, home_image_pos)

    clothes_rect = pygame.draw.rect(screen, BUTTON_BDY, [420, 600, 45, 30])
    clothes_image = pygame.image.load("Images/clothes.png")
    clothes_image_scaled = scale_image(clothes_image, 40, 25)
    clothes_image_pos = (
        clothes_rect.x + (45 - clothes_image_scaled.get_width()) // 2,
        clothes_rect.y + (30 - clothes_image_scaled.get_height()) // 2
    )
    screen.blit(clothes_image_scaled, clothes_image_pos)

    return home_rect, clothes_rect

# Set the width and height of the screen [width, height]
size = (480, 640)
screen = pygame.display.set_mode(size)


pygame.display.set_caption("Pet Tropica")



#Happiness Bar
happiness_bar = happinessbar.HappinessBar(30,30,200,20,100)

#Dropdown Bars + Accept Changes

seen = True 
todobutton = dropdown.Dropdown(20,450,120,30,seen,0)
todobutton2 = dropdown.Dropdown(20,490,120,30,seen,1) 
todobutton3 = dropdown.Dropdown(20,530,120,30,seen,2) 

level = modes.Mode(170,450,140,30,seen,0) 
level2 = modes.Mode(170,490,140,30,seen,1) 
level3 = modes.Mode(170,530,140,30,seen,2) 

accept = taskComplete.Task(320,450,140,30,seen,happiness_bar,0)
accept2 = taskComplete.Task(320,490,140,30,seen,happiness_bar,1)
accept3 = taskComplete.Task(320,530,140,30,seen,happiness_bar,2)




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
screen.fill(LIGHT_BLUE)
baseBG(screen)

while not done:
    # --- Main event loop
    mouse_pos = pygame.mouse.get_pos()
    mouse_clicked = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            popup_visible = False  # Hide the popup when any key is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_clicked = True

    # --- Game logic should go here

    # -- CLOCK --
    current_time = (pygame.time.get_ticks() - start_ticks) / 6000
    if current_time > next_step_time:
        next_step_time += time_interval
        happiness_bar.decrease_health(20)
        print(current_time)


    # --- Drawing code should go here


    home_rect, clothes_rect = buttons()


    # current_cat = pygame.image.load("Images/basecat.png")

    if happiness_bar.get_health() > 40:
        pygame.draw.rect(screen, BROWN_FLR, [0, 280, 480, 120])
        catRect.topleft = (150,280)
        tiredRect.topleft = (1000,1000)

    else:
        pygame.draw.rect(screen, BROWN_FLR, [0, 280, 480, 120])
        catRect.topleft = (1000,1000)
        tiredRect.topleft = (150,280)
    

    pygame.draw.rect(screen,(92, 64, 51),catRect)
    pygame.draw.rect(screen,(92, 64, 51),tiredRect)
    screen.blit(resized_selectedcat, catRect)
    screen.blit(resized_tiredcat, tiredRect)


    #     new_cat = pygame.image.load("Images/tiredcat.png")
    #     resized_selectedcat = pygame.transform.scale (new_cat, (320, 270))
    #     screen.blit(resized_selectedcat, (95, 150))
    # Draw happiness bar
    happiness_bar.draw(screen)

    todobutton.draw(screen)
    todobutton2.draw(screen)
    todobutton3.draw(screen)

    level.draw(screen)
    level2.draw(screen)
    level3.draw(screen)

    accept.draw(screen)
    accept2.draw(screen)
    accept3.draw(screen)


    popup(screen, popup_visible, accessory)

    if home_rect.collidepoint(mouse_pos) and mouse_clicked:
        screen.fill(LIGHT_BLUE)

        todobutton.setVis(True)
        todobutton2.setVis(True) 
        todobutton3.setVis(True)

        level.setVis(True) 
        level2.setVis(True) 
        level3.setVis(True) 

        accept.setVis(True)  
        accept2.setVis(True)  
        accept3.setVis(True)  

        baseBG(screen)
    if clothes_rect.collidepoint(mouse_pos) and mouse_clicked:
        screen.fill(LIGHT_BLUE)

        todobutton.setVis(False)
        todobutton2.setVis(False) 
        todobutton3.setVis(False)

        level.setVis(False) 
        level2.setVis(False) 
        level3.setVis(False)

        accept.setVis(False)  
        accept2.setVis(False)  
        accept3.setVis(False)

        closetBG(screen)

        squares = hats(screen)  # Get the squares for collision detection


        # Check if any square was clicked and update the selected cat image
        for i, square in enumerate(squares):
            print(f"Checking square {i}: {square}, Mouse position: {mouse_pos}")
            if square.collidepoint(mouse_pos) and mouse_clicked:
                print(f"Square {i} clicked!")
                if i == 0:
                    print("IMAGE 1")
                    selected_cat_image = "Images/chefcat.png"
                elif i == 1:
                    selected_cat_image = "Images/fancycat.png"
                elif i == 2:
                    selected_cat_image = "Images/leafcat.png"
                elif i == 3:
                    selected_cat_image = "Images/sunhatcat.png"
                elif i == 4:
                    selected_cat_image = "Images/tophatcat.png"

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()