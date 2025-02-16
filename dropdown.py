import pygame

class Dropdown:
    def __init__(self, x, y, w, h, seen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.font = pygame.font.Font(None, 36)

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
        
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False



            if self.counter == 0:
                text = self.font.render("Dishes", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))

            if self.counter == 1: 
                text = self.font.render("Laundry", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 2:
                text = self.font.render("Hydrate", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 3:
                text = self.font.render("Study", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                                       self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 4:
                text = self.font.render("Exercise", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2)) 
            if self.counter == 5:
                self.counter = 0              
            
        


    def setVis(self,seen):
        self.visible = seen