import time
import math

import pygame

from data.gui import Picture
from data.game_window import *


pygame.init()

# class Enemy_test(Area):
#     def set_cord(self, x, y):
#         self.x = x
#         self.y = y

#     def move(self, player_x, player_y):
#         self.speed = 1
#         dx = player_x - self.x
#         dy = player_y - self.y
#         distance = math.hypot(dx, dy)
#         if distance != 0:
#             self.rect.x += (dx / distance) * self.speed
#             self.rect.y += (dy / distance) * self.speed

class Enemy(Picture):
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 0, 0), player=None, speed=1, filename=None, window=root):
        super().__init__(x=x, y=y, width=width, height=height, filename=filename)
        self.player = player
        self.speed = speed
        self.color = color
        self.color_bak = color

    def load_image(self, image_file):
        self.image = image_file

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
