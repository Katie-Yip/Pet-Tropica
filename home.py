import pygame

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

    #CAT
    cat = pygame.image.load("Images/basecat.png")
    resized_cat = pygame.transform.scale(cat, (300, 250))
    screen.blit(resized_cat, (105, 150))

def popup(screen, popup_visible, accessory):
    #SUNHAT
    sunhat = pygame.image.load("Images/cat_sunhat.png")
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