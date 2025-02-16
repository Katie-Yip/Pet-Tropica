import pygame

class Dropdown:
    def __init__(self, x, y, w, h, seen):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


        self.clicked = False




    def draw(self,surface):
        if self.visible:
            if self.rect:
                pygame.draw.rect(surface, (0, 255, 0), self.rect)

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    print('CLICKED')
        
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False
        


    def setVis(self,seen):
        self.visible = seen