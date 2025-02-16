import pygame

class Task:
    def __init__(self, x, y, w, h, seen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen

        self.font = pygame.font.Font(None, 36)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


        self.clicked = False
        self.counter = 0



    def draw(self,surface):
        if self.visible:
            if self.rect:
                pygame.draw.rect(surface, (0, 255, 0), self.rect)

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.counter = self.counter + 1
                    print('CLICKED')
        
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False

            if self.counter == 0:
                text = self.font.render("Accept", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))

            if self.counter == 1: 
                text = self.font.render("Complete", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 2:
                self.counter = 0
        


    def setVis(self,seen):
        self.visible = seen

