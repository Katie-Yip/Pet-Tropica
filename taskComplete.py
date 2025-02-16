import pygame
import happinessbar

class Task:
    def __init__(self, x, y, w, h, seen, happiness_bar):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.visible = seen
        #new
        self.happiness_bar = happiness_bar

        self.font = pygame.font.SysFont("comic sans ms", 24)
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)


        self.clicked = False
        self.coinCondition = False
        self.counter = 0
        self.next_step_time = 0
        self.time_interval = 1


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
                text = self.font.render("Accept", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                           self.rect.y + (self.h - text.get_height()) // 2))

            if self.counter == 1: 
                text = self.font.render("Complete", True, "white")
                surface.blit(text, (self.rect.x + (self.w - text.get_width()) // 2, 
                    self.rect.y + (self.h - text.get_height()) // 2))
            if self.counter == 2:
                coinCondition = True
                self.happiness_bar.increase_health(10) 
                if self.happiness_bar.get_health == 100:
                    print("YOU WIN")

                self.counter = 0
        
        coinCondition = False

    def setVis(self,seen):
        self.visible = seen

    def getCoin(self):
        return self.coinCondition



    """ def update_health(self):
        if self.difficulty == "easy":
            self.happinessbar.increase_health(10)
        elif self.happinessbar == "medium":
            self.happinessbar.increase_health(20)
        elif self.difficulty == "hard":
            self.happinessbar.increase_health(30)"""