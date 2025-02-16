import pygame

class Dropdown:
    def __init__(self,x,y,w,h,array):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.array = array
        length = len(array)


    #x, y, w, h    
    def draw(self, surface):
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h)) 

     

    
    # def drawDropDown(self,click):
    #     #while loop, create length amount of rectangles that are x + whatever down

        