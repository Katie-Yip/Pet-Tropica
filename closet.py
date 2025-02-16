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

def closetBG(screen):
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

def buttons():
    #BUTTON
    font = pygame.font.Font(None, 36)
    #accept_rect = pygame.Rect(200, 150, 200, 60)  # (x, y, width, height)
    #button_text = font.render("Accept", True, BLACK)
    #pygame.draw.rect(screen, LIGHT_BLUE, accept_rect, border_radius=30)  # Increase border_radius for rounder corners

    # Draw text inside the button (centered)
    #text_rect = button_text.get_rect(center=accept_rect.center)
    #screen.blit(button_text, text_rect)