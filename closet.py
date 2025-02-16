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

size = (480, 640)
screen = pygame.display.set_mode(size)

selected_cat_image = "Images/basecat.png"

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

# Function to display cat image
def cat(screen, image):
    cat_image = pygame.image.load(image)
    resized_cat = pygame.transform.scale(cat_image, (300, 250))
    screen.blit(resized_cat, (105, 150))
    
# Function to draw and return the squares
def hats(screen):
    # Define positions for the squares (buttons) as Rect objects
    square1 = pygame.Rect(60, 420, 70, 70)
    square2 = pygame.Rect(200, 420, 70, 70)
    square3 = pygame.Rect(340, 420, 70, 70)
    square4 = pygame.Rect(140, 520, 70, 70)
    square5 = pygame.Rect(280, 520, 70, 70)

    # Load and scale images to fit inside the squares
    chefhat_image = pygame.image.load("Images/chefhat.png")
    fancy_image = pygame.image.load("Images/fancy.png")
    leaf_image = pygame.image.load("Images/leaf.png")
    sunhat_image = pygame.image.load("Images/sunhat.png")
    tophat_image = pygame.image.load("Images/tophat.png")

    images = [chefhat_image, fancy_image, leaf_image, sunhat_image, tophat_image]
    squares = [square1, square2, square3, square4, square5]

    for i, square in enumerate(squares):
        img = scale_image(images[i], 60, 60)
        screen.blit(img, (square.x + (square.width - img.get_width()) // 2, square.y + (square.height - img.get_height()) // 2))

    print("Returning squares...")
    return squares  # Return the squares for collision detection

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


    hats(screen)

    cat(screen, selected_cat_image)

      #for font
    font = pygame.font.SysFont('georgia', 14)
    text1 = font.render("Chef's hat", True, (0,0,0))
    text2 = font.render("Stach & Specs", True, (0,0,0))
    text3 = font.render("Leaf", True, (0,0,0))
    text4 = font.render("Sunhat", True, (0,0,0))
    text5 = font.render("Tophat", True, (0,0,0))


    text1_position = (50,490)
    text2_position = (200,490)
    text3_position= (360,490)
    text4_position= (145,590)
    text5_position= (280,590)

    

    screen.blit(text1, text1_position)
    screen.blit(text2, text2_position)
    screen.blit(text3, text3_position)
    screen.blit(text4, text4_position)
    screen.blit(text5, text5_position)

