import pygame

class Dropdown:
    def __init__(self, x, y, width, height, options):
        self.button_rect = pygame.Rect(x, y, width, height)
        self.options = options
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 28)
        self.dropdown_height = height
        self.dropdown_rects = [pygame.Rect(x, y + height + i * self.dropdown_height, width, height) for i in range(len(options))]
    
    def draw(self, screen, mouse_x, mouse_y):
        # Check if mouse is over the button
        hovered = self.button_rect.collidepoint(mouse_x, mouse_y)

        # Draw button
        button_color = "red" if hovered else "green"
        pygame.draw.rect(screen, button_color, self.button_rect)

        # Draw button text
        text = self.font.render("Click me", True, "white")
        screen.blit(text, self.button_rect.move((self.button_rect.width - text.get_width()) // 2, 
                                                (self.button_rect.height - text.get_height()) // 2))

        # Show dropdown menu when hovered
        if hovered:
            for i, rect in enumerate(self.dropdown_rects):
                pygame.draw.rect(screen, "gray", rect)
                option_text = self.small_font.render(self.options[i], True, "black")
                screen.blit(option_text, rect.move((rect.width - option_text.get_width()) // 2, 
                                                   (rect.height - option_text.get_height()) // 2))
                

    def check_click(self, mouse_x, mouse_y):
        # Check if any of the dropdown options were clicked
        for i, rect in enumerate(self.dropdown_rects):
            if rect.collidepoint(mouse_x, mouse_y):
                self.selected_option = self.options[i]
                return True
        return False