# button.py

import pygame

class Update:
    def __init__(self, x, y, width, height, color, text, font, text_color):
        self.rect = pygame.Rect(x, y, width, height)  # Button position and size
        self.color = color  # Button color
        self.text = text  # Text to display on the button
        self.font = font  # Font object for the text
        self.text_color = text_color  # Color for the text

    def draw(self, screen):

        # Draw the button
        pygame.draw.rect(screen, self.color, self.rect)
        
        # Render the text
        text_surface = self.font.render(self.text, True, self.text_color)
        
        # Center the text on the button
        text_rect = text_surface.get_rect(center=self.rect.center)
        
        # Blit (draw) the text onto the screen
        screen.blit(text_surface, text_rect)

      
    def is_clicked(self):
        # Check if the mouse clicked inside the button's rectangle
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        
        # Use the button's own rect for collision detection
        if left_click and self.rect.collidepoint(mouse_pos):
            return True
        else:
            return False #i wanna kill someone omg

