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


player = Player(x=W//2, y=H//2, width=35, height=64, filename='data/game_texture/player/pistol.png')
player_skins = [pygame.image.load('data/game_texture/player/pistol.png'), pygame.image.load('data/game_texture/player/gun.png')]
weapon_skins = ['data/game_texture/shop/bullet.png', 'data/game_texture/shop/gun.png']
shop_price = [50, 500]

shop = Picture(x=W//2+150, y=H//2+150, width=128, height=128, filename='data/game_texture/shop/shop.png')
shop_menu = Area(x=W//2-200, y=H//2-200, width=225, height=150, color=(100, 100, 0))
shop_arrow_right = Picture(x=W//2-200+(200-15*2), y=H//2-200+(150/4), filename='data/game_texture/shop/arrow_right.png')
shop_arrow_left = Picture(x=W//2-200-5, y=H//2-200+(150/4), filename='data/game_texture/shop/arrow_left.png')
player_select = 0
shop_select = 0
weapon_image = pygame.image.load(weapon_skins[shop_select])
shop_weapon = Picture(x=W//2-200+225//2-32, y=H/2-200+150//2-36, filename=weapon_skins[shop_select])

fps_game = 0
menu = 0

player_bullets = []
inventory = []
enemys = []
map_blocks = []
enemys_ = True
enemys_count = 5

money = 0
# bullet_count = 150
bullet_delay = 0.2
bullet_damage = [50, 150]

wave_count = 0

all_sprites = []

bg = pygame.image.load('data/game_texture/bg.png')

# for i in range(2):
#     ii = i*1024
#     for j in range(1):
#         map_blocks.append(Picture('1024_map.png', x=1024*j, y=ii))

bullet_time = time.time()
shop_time = time.time()
select_time = time.time()
wave_draw_time = time.time()
zombie_spawn_time = time.time()

null_rect = Enemy(x=10000, y=10000, filename='data/game_texture/shop/shop.png')

player.image_init()
player.image = player_skins[player_select]
player.orginal_player = player_skins[player_select]
player.rotate_image = player_skins[player_select]

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
        main_label.draw()

    if menu != 0 and menu != 1:
        back_button.draw(shift_x=5, shift_y=10)
        back_button.hover_color((255, 255, 0))
        if back_button.is_clicked():
            menu = 0

    if menu == 0:
        game_map.rect.x, game_map.rect.y = 0, 0
        shop.rect.x, shop.rect.y = W/2+150, H//2+150
        all_sprites = [shop]
        shop_price = [50, 500]
        player.init(health=100)
        player.image_init()
        player.image = player_skins[player_select]
        player.orginal_player = player_skins[player_select]
        player.rotate_image = player_skins[player_select]
        player.image = player.orginal_player
        enemys_first_spawn = True
        enemys = []
        player_bullets = []
        bullet_count = 50
        shop_select = 0
        money = 0
        inventory = [0]
        wave_count = 0
        player_select = 0
        enemys_health = 0


        player.rect.x = W//2
        player.rect.y = H//2

        root.fill((0, 0, 0))
        main_label.draw()

        buttons = [new_game, game_settings]
        for index, button in enumerate(buttons):
            button.draw(shift_x=5, shift_y=10)
            button.hover_color((255, 255, 0))

            if button.is_clicked():
                menu = index+1

        if new_game.is_clicked():
            menu = 1

        elif game_settings.is_clicked():
            menu = 3


    elif menu == 1:
        # if null_rect not in enemys:
        #     enemys.append(null_rect)

        root.blit(bg, (player.bg_x, player.bg_y))  # основний фон
        root.blit(bg, (player.bg_x + 1224, player.bg_y))  # фон справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y))  # фон зліва
        root.blit(bg, (player.bg_x, player.bg_y + 615))  # фон знизу
        root.blit(bg, (player.bg_x, player.bg_y - 615))  # фон зверху
        root.blit(bg, (player.bg_x - 1224, player.bg_y - 615))  # фон зверху зліва
        root.blit(bg, (player.bg_x + 1224, player.bg_y + 615))  # фон знизу справа
        root.blit(bg, (player.bg_x + 1224, player.bg_y - 615))  # фон зверху справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y + 615))  # фон знизу зліва



        if (null_rect in enemys or enemys_first_spawn) and time.time() - zombie_spawn_time > 3:
            enemys_first_spawn = False
            try:
                enemys.remove(null_rect)
            except ValueError:
                pass

            if wave_count % 2:
                enemys_health += 25

            for i in range(enemys_count*wave_count):
                random_spawn = r(1, 5)

                if random_spawn == 1:
                    enemy = Enemy(x=r(-1224, 1224), y=r(-615, -475), width=35, height=64, player=player, health=enemys_health, speed=2, reward=5*wave_count, filename='data/game_texture/zombie/zombie.png')
                elif random_spawn == 2:
                    enemy = Enemy(x=r(-1224, 1224), y=r(1100, 1500), width=35, height=64, player=player, health=enemys_health, speed=3, reward=5*wave_count, filename='data/game_texture/zombie/zombie.png')
                elif random_spawn == 3:
                    enemy = Enemy(x=r(-1350, -1224), y=r(-615, 615), width=35, height=64, player=player, health=enemys_health, speed=2, reward=5*wave_count, filename='data/game_texture/zombie/zombie.png')
                elif random_spawn == 4:
                    enemy = Enemy(x=r(1450, 1650), y=r(-615, 615), width=35, height=64, player=player, health=enemys_health, speed=3, reward=5*wave_count, filename='data/game_texture/zombie/zombie.png')
                elif random_spawn == 5:
                    enemy = Enemy(x=r(-1224, 1224), y=r(-615, -475), width=35, height=64, player=player, health=enemys_health, speed=6, reward=50, filename='data/game_texture/zombie/zombie.png')

                print(enemy.health)

                enemys.append(enemy)
                all_sprites.append(enemy)


        shop.draw()
        # player.image = player_skins[player_select]
        # player.orginal_player = player_skins[player_select]
        # player.rotate_image = player_skins[player_select]

        # game_map.draw()
        key = pygame.key.get_pressed()
        player.move(key, 2, all_sprites)
        player.draw()

        for enemy in enemys:
            if enemy.health < 1:
                enemys.remove(enemy)
                money += enemy.reward

            enemy.move()
            enemy.draw()
            for bullet in player_bullets:
                if enemy.collidepoint((bullet.x, bullet.y)):
                    if enemy in enemys:
                        player_bullets.remove(bullet)
                        # enemys.remove(enemy)
                        enemy.health -= bullet.damage

        bullet_count_label.set_text(f'Bullet: {bullet_count}', 25)
        bullet_count_label.draw()

        if money < 0:
            money = 0

        money_label.set_text(f'Money: {money}', 25)
        money_label.draw()

        player_health_label.set_text(f'Health: {player.health}', 25)
        player_health_label.draw()

        if len(enemys) == 0:
            wave_draw_time = time.time()
            zombie_spawn_time = time.time()
            enemys.append(null_rect)
            wave_count += 1

        if time.time() - wave_draw_time < 3 and len(enemys) == 1:
            wave_label.set_text(f'wave {wave_count}', 80, (255, 50, 25))
            wave_label.draw()

        if show_fps:
            fps_show.set_text("FPS: " + str(clock.get_fps())[:4], 20, (255, 255, 255))
            fps_show.draw()

        if pygame.mouse.get_pressed()[0] and bullet_count > 0 and time.time() - bullet_time > bullet_delay:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            player_bullets.append(PlayerBullets(player.rect.x+25, player.rect.y+25, mouse_x, mouse_y, bullet_damage[player_select]))
            bullet_count -= 1
            bullet_time = time.time()

        # if key[pygame.K_r]:
        #     print(len(player_bullets))

        if key[pygame.K_UP] and time.time() - select_time > 0.1:
            select_time = time.time()
            player_select += 1
            if player_select == 2:
                player_select = 0

            if player_select not in inventory:
                player_select += 1
                if player_select == 2:
                    player_select = 0

            player.image_init()
            player.image = player_skins[player_select]
            player.orginal_player = player_skins[player_select]
            player.rotate_image = player_skins[player_select]
            player.image_init()

        if key[pygame.K_DOWN] and time.time() - select_time > 0.1:
            select_time = time.time()
            player_select += 1
            if player_select == 2:
                player_select = 0

            if player_select not in inventory:
                player_select += 1
                if player_select == 2:
                    player_select = 0

            player.image_init()
            player.image = player_skins[player_select]
            player.orginal_player = player_skins[player_select]
            player.rotate_image = player_skins[player_select]
            player.image_init()

        # print(player_select)

        for bullet in player_bullets:
            bullet.shoot()
            if bullet.x > W or bullet.x < 0 or bullet.y > H or bullet.y < 0:
                player_bullets.remove(bullet)


        if player.colliderect(shop.rect):
            shop_menu.fill()
            shop_arrow_right.draw()
            shop_arrow_left.draw()
            shop_weapon.draw()

            shop_price_label.set_text(f'price {shop_price[shop_select]}')
            shop_price_label.draw()

            if key[pygame.K_RIGHT] and time.time() - shop_time > 0.2:
                shop_time = time.time()
                shop_select += 1
                if shop_select == 2:
                    shop_select = 0

                weapon_image = pygame.image.load(weapon_skins[shop_select])
                shop_weapon.image = weapon_image

            elif key[pygame.K_LEFT] and time.time() - shop_time > 0.2:
                shop_time = time.time()
                shop_select -= 1
                if shop_select == -1:
                    shop_select = 1

                weapon_image = pygame.image.load(weapon_skins[shop_select])
                shop_weapon.image = weapon_image

            if key[pygame.K_RETURN] and money >= shop_price[shop_select] and time.time() - shop_time > 0.2:
                if shop_select == 0:
                    bullet_count += 100+(wave_count*25)
                    shop_price[shop_select] += 50

                shop_time = time.time()
                money -= shop_price[shop_select]
                if shop_select not in inventory:
                    inventory.append(shop_select)



        for enemy in enemys:
            if player.colliderect(enemy.rect) and enemy in enemys:
                player.health -= 10
                enemys.remove(enemy)

        if player.health < 1:
            menu = 4

        # print(len(enemys))



    elif menu == 3:
        show_fps_button.draw(shift_x=5, shift_y=10)
        show_fps_button.hover_color((255, 255, 0))
        if show_fps_button.is_clicked():
            show_fps = not show_fps
            show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))
            time.sleep(0.1)

    # game over
    elif menu == 4:
        root.blit(bg, (player.bg_x, player.bg_y))  # основний фон
        root.blit(bg, (player.bg_x + 1224, player.bg_y))  # фон справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y))  # фон зліва
        root.blit(bg, (player.bg_x, player.bg_y + 615))  # фон знизу
        root.blit(bg, (player.bg_x, player.bg_y - 615))  # фон зверху
        root.blit(bg, (player.bg_x - 1224, player.bg_y - 615))  # фон зверху зліва
        root.blit(bg, (player.bg_x + 1224, player.bg_y + 615))  # фон знизу справа
        root.blit(bg, (player.bg_x + 1224, player.bg_y - 615))  # фон зверху справа
        root.blit(bg, (player.bg_x - 1224, player.bg_y + 615))  # фон знизу зліва

        player_health_label.set_text(f'Health: 0', 25)
        player.draw()
        for enemy in enemys:
            enemy.draw()

        bullet_count_label.draw()
        money_label.draw()
        player_health_label.draw()

        shop.draw()
        game_over_label.draw()



    clock.tick(FPS)
    pygame.display.update()
