import pygame

from data.game_window import root
from data.gui import Label

pygame.init()

class Player(Label):
    health = 100

    def move(self, key, step):
        if key[pygame.K_w]:
            self.rect.y -= step

        if key[pygame.K_s]:
            self.rect.y += step

        if key[pygame.K_a]:
            self.rect.x -= step

        if key[pygame.K_d]:
            self.rect.x += step

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)
