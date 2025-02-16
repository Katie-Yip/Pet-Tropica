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
BUTTON_BDY = (255, 206, 134)
BUTTON = (161, 122, 105)

# Function to scale images while maintaining aspect ratio
def scale_image(image, max_width, max_height):
    # Get the original image dimensions
    original_width, original_height = image.get_size()
    
    # Calculate the scaling factor to fit within max_width and max_height
    width_ratio = max_width / original_width
    height_ratio = max_height / original_height
    scale_factor = min(width_ratio, height_ratio)  # Use the smaller ratio to maintain aspect ratio

    # Calculate new dimensions
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)
    
    # Scale the image
    return pygame.transform.scale(image, (new_width, new_height))

def cat(screen, image):
    cat = pygame.image.load(image)
    resized_cat = pygame.transform.scale(cat, (300, 250))
    screen.blit(resized_cat, (105, 150))

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

    cat(screen, "Images/basecat.png")

    hats(screen)

def hats(screen):
    # Define positions for the squares
    # Top row (three squares)
    square1 = pygame.draw.rect(screen, BUTTON_BDY, [60, 420, 70, 70])
    chefhat_image = pygame.image.load("Images/chefhat.png")
    chefhat_image_scaled = scale_image(chefhat_image, 60, 60)
    chefhat_image_pos = (
        square1.x + (65 - chefhat_image_scaled.get_width()) // 2,  
        square1.y + (70 - chefhat_image_scaled.get_height()) // 2  
    )
    screen.blit(chefhat_image_scaled, chefhat_image_pos)

    square2 = pygame.draw.rect(screen, BUTTON_BDY, [200, 420, 70, 70])
    fancy_image = pygame.image.load("Images/fancy.png")
    fancy_image_scaled = scale_image(fancy_image, 55, 55)
    fancy_image_pos = (
        square2.x + (80 - chefhat_image_scaled.get_width()) // 2,  
        square2.y + (60 - chefhat_image_scaled.get_height()) // 2  
    )
    screen.blit(fancy_image_scaled, fancy_image_pos)

    square3 = pygame.draw.rect(screen, BUTTON_BDY, [340, 420, 70, 70])
    leaf_image = pygame.image.load("Images/leaf.png")
    leaf_image_scaled = scale_image(leaf_image, 50, 50)
    leaf_image_pos = (
        square3.x + (80 - chefhat_image_scaled.get_width()) // 2,  
        square3.y + (70 - chefhat_image_scaled.get_height()) // 2  
    )
    screen.blit(leaf_image_scaled, leaf_image_pos)

    # Bottom row (two squares)
    square4 = pygame.draw.rect(screen, BUTTON_BDY, [140, 520, 70, 70])
    sunhat_image = pygame.image.load("Images/sunhat.png")
    sunhat_image_scaled = scale_image(sunhat_image, 60, 60)
    sunhat_image_pos = (
        square4.x + (70 - chefhat_image_scaled.get_width()) // 2,  
        square4.y + (80 - chefhat_image_scaled.get_height()) // 2  
    )
    screen.blit(sunhat_image_scaled, sunhat_image_pos)

    square5 = pygame.draw.rect(screen, BUTTON_BDY, [280, 520, 70, 70])
    tophat_image = pygame.image.load("Images/tophat.png")
    tophat_image_scaled = scale_image(tophat_image, 60, 60)
    tophat_image_pos = (
        square5.x + (70 - tophat_image_scaled.get_width()) // 2,  
        square5.y + (70 - tophat_image_scaled.get_height()) // 2  
    )
    screen.blit(tophat_image_scaled, tophat_image_pos)

    return square1, square2, square3, square4, square5