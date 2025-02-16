import pygame
import dropdown

from happinessbar import HappinessBar

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



def baseBG(screen):
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

def popup(screen, popup_visible, accessory):
    #SUNHAT
    chefhat_image = pygame.image.load("Images/chefhat.png")
    fancy_image = pygame.image.load("Images/fancy.png")
    leaf_image = pygame.image.load("Images/leaf.png")
    sunhat_image = pygame.image.load("Images/sunhat.png")
    tophat_image = pygame.image.load("Images/tophat.png")

    resized_sunhat = pygame.transform.scale(sunhat_image, (250, 150))
    resized_chefhat = pygame.transform.scale(chefhat_image, (250, 150))
    resized_fancy = pygame.transform.scale(fancy_image, (250,150))
    resized_leaf = pygame.transform.scale(leaf_image,(250, 150))
    resized_tophat = pygame.transform.scale(tophat_image,(250,150))

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
        if accessory == 1:
            screen.blit(resized_chefhat, (130, 250))
        if accessory == 2:
            screen.blit(resized_leaf, (130, 250))
        if accessory == 3:
            screen.blit(resized_tophat, (130, 250))
        if accessory == 4:
            screen.blit(resized_fancy, (130, 250))

        accessory == accessory + 1

# def todo(screen):
#     mouse_x, mouse_y = pygame.mouse.get_pos()

#     todobutton = dropdown.Dropdown(20,450,120,30,options) 
#     todobutton2 = dropdown.Dropdown(20,490,120,30,options) 
#     todobutton3 = dropdown.Dropdown(20,530,120,30,options) 

#     level = dropdown.Dropdown(170,450,140,30,modes) 
#     level2 = dropdown.Dropdown(170,490,140,30,modes) 
#     level3 = dropdown.Dropdown(170,530,140,30,modes) 

#     #TO DO buttons
#     todobutton3.draw()
#     todobutton2.draw()
#     todobutton.draw()
#     #mode button
#     level3.draw() 
#     level2.draw()
#     level.draw()



     
