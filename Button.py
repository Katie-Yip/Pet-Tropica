import pygame

class Button:
    def __init__(self, x, y, w, h, font, color, highlight_color):
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.color = color
        self.highlight_color = highlight_color
        self.text = "Accept"
        self.clicked = False

    def draw(self, screen):
        # Change color if hovered
        mouse_pos = pygame.mouse.get_pos()
        current_color = self.highlight_color if self.rect.collidepoint(mouse_pos) else self.color

        pygame.draw.rect(screen, current_color, self.rect)
        pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # Border

        msg = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(msg, msg.get_rect(center=self.rect.center))

    def update(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.clicked = not self.clicked  # Toggle state
                    self.text = "Complete" if self.clicked else "Accept"
