import pygame

class Mode:
    def __init__(self, x, y, w, h, seen, level):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen
        self.level = level  # This is used to determine the button's text

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.font = pygame.font.SysFont("comic sans ms", 24)

    def draw(self, surface):
        if self.visible:
            if self.rect:
                pygame.draw.rect(surface, (120, 200, 120), self.rect)

            # Set the text based on the level
            if self.level == 0:
                text = self.font.render("Easy", True, "white")
            elif self.level == 1:
                text = self.font.render("Medium", True, "white")
            elif self.level == 2:
                text = self.font.render("Hard", True, "white")

            # Draw the text centered in the button
            surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                               self.rect.y + (self.h - text.get_height()) // 2))

    def setVis(self, seen):
        self.visible = seen
