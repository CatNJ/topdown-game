import math

import pygame

from data.gui import Area
from data.game_window import *


pygame.init()

# class Enemy(Area):
#     def set_cord(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self, player_x, player_y):
#         self.speed = 1
#         dx = player_x - self.x
#         dy = player_y - self.y
#         distance = math.hypot(dx, dy)
#         if distance != 0:
#             self.rect.x += (dx / distance) * self.speed
#             self.rect.y += (dy / distance) * self.speed

class Enemy(Area):
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 0, 0), player=None, speed=1, window=root):
        super().__init__(x, y, width, height, color, window)
        self.player = player
        self.speed = speed

    def move(self):
        if self.player is not None:
            player_x, player_y = self.player.rect.x, self.player.rect.y
            if player_x > self.x:
                self.x += self.speed
            elif player_x < self.x:
                self.x -= self.speed
            if player_y > self.y:
                self.y += self.speed
            elif player_y < self.y:
                self.y -= self.speed
            self.rect.x = self.x
            self.rect.y = self.y
