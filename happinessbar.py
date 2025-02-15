"""import pygame

class happinessbar:
        
    def happy_bar(surf, pos, size, borderC, backC, barC, progress):
        pygame.draw.rect(surf, backC, (*pos, *size)) #background
        pygame.draw.rect(surf, borderC, (*pos, *size), 1)  # Border
        innerPos = (pos[0] + 3, pos[1] + 3)
        innerSize = ((size[0] - 6) * progress, size[1] - 6)

        pygame.draw.rect(surf, barC, (*innerPos, *innerSize))  # Progress bar"""