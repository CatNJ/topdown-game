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


player = Player(x=W/2, y=H/2, width=35, height=64, filename='data/game_texture/player/pistol.png')
player_skin = ['data/game_texture/player/pistol.png', 'data/game_texture/player/gun.png']


camera_x = player.rect.x - W // 2
camera_y = player.rect.x - H // 2

fps_game = 0
menu = 0

player_bullets = []
enemys = []
map_blocks = []
enemys_gen = True
enemys_count = 100

money = 0
bullet_count = 150
bullet_delay = 0.2
bullet_time = time.time()

all_sprites = []

bg = pygame.image.load('data/game_texture/bg.png')

# for i in range(2):
#     ii = i*1024
#     for j in range(1):
#         map_blocks.append(Picture('1024_map.png', x=1024*j, y=ii))

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
        main_lable.draw()

    if menu != 0 and menu != 1:
        back_button.draw(shift_x=5, shift_y=10)
        back_button.hover_color((255, 255, 0))
        if back_button.is_clicked():
            menu = 0

    if menu == 0:
        game_map.rect.x, game_map.rect.y = 0, 0
        all_sprites = []
        player.init(all_sprites)
        enemys_gen = True
        enemys = []
        player_bullets = []
        bullet_count = 150

        player.rect.x = W/2
        player.rect.y = H/2

        root.fill((0, 0, 0))
        main_lable.draw()

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
        root.blit(bg, (player.bg_x, player.bg_y))  # основний фон
        root.blit(bg, (player.bg_x + 1224, player.bg_y))  # фон справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y))  # фон зліва
        root.blit(bg, (player.bg_x, player.bg_y + 615))  # фон знизу
        root.blit(bg, (player.bg_x, player.bg_y - 615))  # фон зверху
        root.blit(bg, (player.bg_x - 1224, player.bg_y - 615))  # фон зверху зліва
        root.blit(bg, (player.bg_x + 1224, player.bg_y + 615))  # фон знизу справа
        root.blit(bg, (player.bg_x + 1224, player.bg_y - 615))  # фон зверху справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y + 615))  # фон знизу зліва



        if len(enemys) == 0 and enemys_gen:
            enemys_gen = False
            for i in range(enemys_count):
                enemy = Enemy(r(-500, W+500), r(-500, H+500), 35, 64, (255, 0, 0), player, 0.1, 'data/game_texture/zombie/zombie.png')
                enemys.append(enemy)
                all_sprites.append(enemy)

        # game_map.draw()
        key = pygame.key.get_pressed()
        player.move(key, 2)
        player.draw()

        for enemy in enemys:
            enemy.move()
            enemy.draw()
            for bullet in player_bullets:
                if enemy.collidepoint((bullet.x, bullet.y)):
                    if enemy in enemys:
                        player_bullets.remove(bullet)
                        enemys.remove(enemy)
                        money += 2

        bullet_count_lable.set_text(f'bullet: {bullet_count}', 25, (255,255,255))
        bullet_count_lable.draw()

        money_lable.set_text(f'money: {money}', 25)
        money_lable.draw()

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
