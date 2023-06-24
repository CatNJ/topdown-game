import random
import math

import pygame

from data.game_window import root
from data.game_map import *
from data.gui import Picture
from data.enemy import Enemy


pygame.init()

multiplicand = 2

class Player(Picture):
    def image_init(self):
        self.rotate_player = pygame.transform.flip(self.image, True, False)
        self.orginal_player = self.image

    def init(self, health):
        # self.rotate_player = pygame.transform.flip(self.image, True, False)
        # self.orginal_player = self.image
        self.health = health
        self.bg_x = 0
        self.bg_y = 0

    def move(self, key, step, sprites_list):
        if key[pygame.K_w]:
            if self.bg_y < 615:
                self.bg_y += 5
                self.rect.y -= step
                for sprite in sprites_list:
                    sprite.rect.y += int(step*multiplicand)
                game_map.rect.y += int(step*multiplicand)

            else:
                pass

        if key[pygame.K_s]:
            if self.bg_y > -525:
                self.bg_y -= 5
                self.rect.y += step
                for sprite in sprites_list:
                    sprite.rect.y -= int(step*multiplicand)
                game_map.rect.y -= int(step*multiplicand)

            else:
                pass

        if key[pygame.K_a]:
            if self.bg_x < 1224:
                self.bg_x += 5
                self.rect.x -= step
                self.image = self.rotate_player
                for sprite in sprites_list:
                    sprite.rect.x += int(step*multiplicand)
                game_map.rect.x += int(step*multiplicand)

            else:
                pass

        if key[pygame.K_d]:
            if self.bg_x > -1150:
                self.bg_x -= 5
                self.rect.x += step
                self.image = self.orginal_player
                for sprite in sprites_list:
                    sprite.rect.x -= int(step*multiplicand)
                game_map.rect.x -= int(step*multiplicand)

            else:
                pass

class PlayerBullets:
    def __init__(self, x, y, mouse_x, mouse_y, damage=50):
        self.x = x
        self.y = y
        self.mouse_x = mouse_x
        self.mouse_y = mouse_y
        self.speed = random.randint(20, 25)
        self.angle = math.atan2(y-mouse_y, x-mouse_x)
        self.x_vel = math.cos(self.angle) * self.speed
        self.y_vel = math.sin(self.angle) * self.speed

        self.damage = damage

    def shoot(self):
        self.x -= int(self.x_vel)
        self.y -= int(self.y_vel)

        pygame.draw.circle(root, (255,255,0), (self.x, self.y), 5)
