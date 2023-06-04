import time

import pygame
from random import randint as r

from data.game_window import *
from data.gui import *
from data.settings import *
from data.labels import *
from data.buttons import *
from data.player import *
from data.enemy import Enemy

pygame.init()

root.fill((0, 0, 0))

clock = pygame.time.Clock()
FPS = 60


player = Player(x=W/2, y=H/2, width=50, height=50, filename='player.png')
game_map = Picture('map_big.png')

camera_x = player.rect.x - W // 2
camera_y = player.rect.x - H // 2

fps_game = 0
menu = 0

player_bullets = []
enemys = []
enemys_gen = True
enemys_count = 100

bullet_count = 150
bullet_delay = 0.075
bullet_time = time.time()

all_sprites = []

while True:
    root.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if menu == 0 and event.key == pygame.K_ESCAPE:
                exit()

            elif event.key == pygame.K_ESCAPE:
                menu = 0

    if menu != 1:
        main_text.draw()

    if menu != 0 and menu != 1:
        back_button.draw(shift_x=5, shift_y=10)
        back_button.hover_color((255, 255, 0))
        if back_button.is_clicked():
            menu = 0

    if menu == 0:
        game_map.rect.x, game_map.rect.y = 0, 0
        all_sprites = [game_map]
        player.init(all_sprites)
        enemys_gen = True
        enemys = []
        player_bullets = []
        bullet_count = 150

        player.rect.x = W/2
        player.rect.y = H/2

        root.fill((0, 0, 0))
        main_text.draw()

        buttons = [new_game, load_game, game_settings]
        for index, button in enumerate(buttons):
            button.draw(shift_x=5, shift_y=10)
            button.hover_color((255, 255, 0))

            if button.is_clicked():
                menu = index+1

        if new_game.is_clicked():
            menu = 1

        elif load_game.is_clicked():
            menu = 2

        elif game_settings.is_clicked():
            menu = 3
            

    elif menu == 1:
        if len(enemys) == 0 and enemys_gen:
            enemys_gen = False
            for i in range(enemys_count):
                enemy = Enemy(r(50, W-50), r(50, H-50), 40, 40, (255, 0, 0), player, r(1, 3), 'russian_zombie.jpg')
                enemys.append(enemy)
                # all_sprites.append(enemy)

        game_map.draw()
        key = pygame.key.get_pressed()
        player.move(key, 6)
        player.draw()

        for enemy in enemys:
            enemy.move()
            enemy.draw()
            for bullet in player_bullets:
                if enemy.collidepoint((bullet.x, bullet.y)):
                    if enemy in enemys:
                        player_bullets.remove(bullet)
                        enemys.remove(enemy)

        bullet_count_lable.set_text(f'bullet: {bullet_count}', 25, (255,255,255))
        bullet_count_lable.draw()

        if show_fps:
            fps_show.set_text("FPS: " + str(clock.get_fps())[:4], 20, (255, 255, 255))
            fps_show.draw()

        if pygame.mouse.get_pressed()[0] and bullet_count > 0 and time.time() - bullet_time > bullet_delay:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player_bullets.append(PlayerBullets(player.rect.x+25, player.rect.y+25, mouse_x, mouse_y))
            bullet_count -= 1
            bullet_time = time.time()

        if key[pygame.K_r]:
            print(len(player_bullets))

        for bullet in player_bullets:
            bullet.shoot()
            if bullet.x > W or bullet.x < 0 or bullet.y > H or bullet.y < 0:
                player_bullets.remove(bullet)


    elif menu == 3:
        show_fps_button.draw(shift_x=5, shift_y=10)
        show_fps_button.hover_color((255, 255, 0))
        if show_fps_button.is_clicked():
            show_fps = not show_fps
            show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))
            time.sleep(0.1)



    clock.tick(FPS)
    pygame.display.update()
