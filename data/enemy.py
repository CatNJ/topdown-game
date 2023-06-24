import time
import math

import pygame

from data.gui import Picture
from data.game_window import *


pygame.init()

class Enemy(Picture):
    def __init__(self, x=0, y=0, width=0, height=0, color=(255, 0, 0), player=None, health=100, speed=1, reward=1, filename=None, window=root):
        super().__init__(x=x, y=y, width=width, height=height, filename=filename)
        self.player = player
        self.health = health
        self.speed = speed
        self.reward = reward
        self.color = color
        self.color_bak = color
        self.orginal_image = self.image
        self.rotate_image = pygame.transform.flip(self.image, True, False)


    def move(self):
        if self.player is not None:
            player_x, player_y = self.player.rect.x, self.player.rect.y
            if player_x > self.rect.x:
                self.rect.x += self.speed
                self.image = self.orginal_image
            if player_x < self.rect.x:
                self.rect.x -= self.speed
                self.image = self.rotate_image
            if player_y > self.rect.y:
                self.rect.y += self.speed
            if player_y < self.rect.y:
                self.rect.y -= self.speed
