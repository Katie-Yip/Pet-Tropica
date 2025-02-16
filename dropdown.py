import pygame

class Dropdown:
    def __init__(self, x, y, w, h, seen,level):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen
        self.level=level

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.font = pygame.font.SysFont("comic sans ms", 18)

        self.clicked = False
        self.counter = 0





    def draw(self,surface):
     

        if self.visible:
            if self.rect:
                pygame.draw.rect(surface, (120, 200, 120), self.rect)

            pos = pygame.mouse.get_pos()

            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.counter = self.counter + 1
        
            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                self.clicked = False



            if self.counter == 0:
                if(self.level==0):
                    text = self.font.render("Dishes", True, "white")
                elif(self.level==1):
                    text = self.font.render("Toilets", True, "white")
                elif(self.level==2):
                    text = self.font.render("2hr workout", True, "white")


                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))

            if self.counter == 1: 
                if(self.level==0):
                    text = self.font.render("Laundry", True, "white")
                elif(self.level==1):
                    text = self.font.render("Clean desk", True, "white")
                elif(self.level==2):
                    text = self.font.render("Deep clean", True, "white")

                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 2:
                if(self.level==0):
                    text = self.font.render("Hydrate", True, "white")
                elif(self.level==1):
                    text = self.font.render("Clean windows", True, "white")
                elif(self.level==2):
                    text = self.font.render("Wash car", True, "white")

                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 3:
                if(self.level==0):
                    text = self.font.render("cook", True, "white")
                elif(self.level==1):
                    text = self.font.render("Study 2 hrs", True, "white")
                elif(self.level==2):
                    text = self.font.render("Yard work", True, "white")

                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                                       self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 4:
                if(self.level==0):
                    text = self.font.render("Dust", True, "white")
                elif(self.level==1):
                    text = self.font.render("Clean fridge", True, "white")
                elif(self.level==2):
                    text = self.font.render("Saw a tree", True, "white")

                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2)) 
            if self.counter == 5:
                self.counter = 0              
            
        


    def setVis(self,seen):
        self.visible = seen