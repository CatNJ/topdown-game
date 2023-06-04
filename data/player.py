import random
import math

import pygame

from data.game_window import root
from data.gui import Picture
from data.enemy import Enemy

pygame.init()

class Player(Picture):
    def init(self, sprites_list):
        self.rotate_player = pygame.transform.flip(self.image, True, False)
        self.orginal_player = self.image
        self.sprites_list = sprites_list

    def move(self, key, step):
        if key[pygame.K_w]:
            self.rect.y -= step
            for sprite in self.sprites_list:
                sprite.rect.y += int(step*step)

        if key[pygame.K_s]:
            self.rect.y += step
            for sprite in self.sprites_list:
                sprite.rect.y -= int(step*step)

        if key[pygame.K_a]:
            self.rect.x -= step
            self.image = self.rotate_player
            for sprite in self.sprites_list:
                sprite.rect.x += int(step*step)

        if key[pygame.K_d]:
            self.rect.x += step
            self.image = self.orginal_player
            for sprite in self.sprites_list:
                sprite.rect.x -= int(step*step)

class PlayerBullets:
    def __init__(self, x, y, mouse_x, mouse_y):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = random.randint(20, 25)
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

    def shoot(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(root, (255,255,0), (self.x, self.y), 5)
