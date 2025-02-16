import pygame
import dropdown
import update

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

#FOR DROPDOWN
options = ["thing1","thing2","thing3"]
modes = ["easy","medium","hard"]  
happy = True

def baseBG(screen,mouse_clicked):
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
    if happy:
        cat = pygame.image.load("Images/basecat.png")
        resized_cat = pygame.transform.scale(cat, (300, 250))
        screen.blit(resized_cat, (105, 150))
    tiredcat = pygame.image.load("Images/tiredcat.png")
    resized_tiredcat = pygame.transform.scale(tiredcat, (300, 250))

    #for font
    font = pygame.font.SysFont('georgia', 18)
    text1 = font.render("To Do", True, (0,0,0))
    text2 = font.render("Level", True, (0,0,0))
    text3 = font.render("Update", True, (0,0,0))

    text1_position = (50,410)
    text2_position = (220,410)
    text3_position= (380,410)

    screen.blit(text1, text1_position)
    screen.blit(text2, text2_position)
    screen.blit(text3, text3_position)

    todo(screen,mouse_clicked)


    updating(screen,)

def popup(screen, popup_visible, accessory):
    #SUNHAT
    sunhat = pygame.image.load("Images/sunhatcat.png")
    resized_sunhat = pygame.transform.scale(sunhat, (250, 150))

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
        popup_font = pygame.font.Font(None, 40)
        popup_rect = pygame.Rect(100, 70, 300, 500)
        pygame.draw.rect(screen, CREAM, popup_rect, border_radius=30)
        popup_text = popup_font.render("New Accessory", True, BLACK)
        popuptext_rect = popup_text.get_rect(midtop=(popup_rect.centerx, 90))
        screen.blit(popup_text, popuptext_rect)

        exit_text = popup_font.render("Press a button to exit", True, BLACK)
        exittext_rect = exit_text.get_rect(midtop=(popup_rect.centerx, 520))
        screen.blit(exit_text, exittext_rect)

        if accessory == 0:
            screen.blit(resized_sunhat, (130, 250))

def todo(screen,mouse_clicked):
    mouse_x, mouse_y = pygame.mouse.get_pos()

    todobutton = dropdown.Dropdown(20,450,120,30,options) 
    todobutton2 = dropdown.Dropdown(20,490,120,30,options) 
    todobutton3 = dropdown.Dropdown(20,530,120,30,options) 

    level = dropdown.Dropdown(170,450,140,30,modes) 
    level2 = dropdown.Dropdown(170,490,140,30,modes) 
    level3 = dropdown.Dropdown(170,530,140,30,modes) 

    #TO DO buttons
    todobutton3.draw(screen,mouse_x,mouse_y)
    todobutton2.draw(screen,mouse_x,mouse_y)
    todobutton.draw(screen,mouse_x,mouse_y)
    #mode button
    level3.draw(screen,mouse_x,mouse_y) 
    level2.draw(screen,mouse_x,mouse_y)
    level.draw(screen,mouse_x,mouse_y)

    if(mouse_clicked):
        todobutton3.check_click(mouse_x,mouse_y)
        todobutton2.check_click(mouse_x,mouse_y)
        todobutton.check_click(mouse_x,mouse_y)

        level3.check_click(mouse_x,mouse_y) 
        level2.check_click(mouse_x,mouse_y)
        level.check_click(mouse_x,mouse_y)

def updating(screen):
    font = pygame.font.Font(None, 36)
    accept=update.Update(330,450,140,30,GREEN,"Accept",font,WHITE)
    accept2=update.Update(330,490,140,30,GREEN,"Accept",font,WHITE)
    accept3=update.Update(330,530,140,30,GREEN,"Accept",font,WHITE)

    accept.draw(screen)
    accept2.draw(screen)
    accept3.draw(screen)

    if accept.is_clicked():
        accept=update.Update(330,450,140,30,RED,"Accept",font,WHITE)


  

