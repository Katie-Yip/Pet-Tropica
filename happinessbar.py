import pygame

class HappinessBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.max_hp = max_hp
        self.hp = max_hp  # Initialize health value

    def draw(self, surface):
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))  # green
        pygame.draw.rect(surface, (119,221,119), (self.x, self.y, self.w * ratio, self.h))  # red
        pygame.draw.rect(surface, "black", (self.x, self.y, self.w, self.h), 3)  # The '3' is the width of the border


    def set_health(self, health):
        """ Set the health value directly. """
        self.hp = health

    def decrease_health(self, amount):
        """ Decrease health by a specific amount. """
        self.hp = max(0, self.hp - amount)

    def increase_health(self, amount):
        """ Increase health by a specific amount. """
        self.hp = min(self.max_hp, self.hp + amount)