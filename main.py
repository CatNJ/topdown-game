import time

import pygame
from random import randint as r

# імпортужмо всі важливі класи
from data.game_window import *
from data.gui import *
from data.settings import *
from data.labels import *
from data.buttons import *
from data.player import Player

# ініціалізація пайГЕЙм
pygame.init()

# заливка фону чорним кольором (по РГБ палітрі)
root.fill((0, 0, 0))

clock = pygame.time.Clock()
FPS = 60

# задній фон (чомусь не робить)
bg = pygame.image.load('data/maps/forest.png').convert_alpha()

# обжкт гравця (перші 2 параметра - кординати х і у, 3 і 4 параметер - ширина і висота, 5 - колір)
player = Player(W/2, H/2, 50, 50, (0, 255, 0))

# фпс в ігрі (який будемо показувати)
fps_game = 0
menu = 0

while True:
    #bg.blit(bg, (100, 100))

    # заливайм екран чорним кольром
    root.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if menu == 0 and event.key == pygame.K_ESCAPE:
                exit()

            elif event.key == pygame.K_ESCAPE:
                menu = 0
    
    # якщо ми не всамій ігрі, відображаєм назву
    if menu != 1:
        main_text.draw()

    # якщо ми не в головному меню і не в самій ігрі, малюжм кнопку назад (hover_color це колір кнопки коли ми на неї наводимось, shift_x|y - зміщення тексту)
    if menu != 0 and menu != 1:
        back_button.draw(shift_x=5, shift_y=10)
        back_button.hover_color((255, 255, 0))
        if back_button.is_clicked():
            menu = 0

    # головне меню
    if menu == 0:
        # якщо ми в головному меню, ставим гравця по середині екрана (коли вже начинажм нову гру)
        player.rect.x = W/2
        player.rect.y = H/2
        
        root.fill((0, 0, 0))
        main_text.draw()

        buttons = [new_game, load_game, game_settings]
        for button in buttons:
            button.draw(shift_x=5, shift_y=10)
            button.hover_color((255, 255, 0))


        if new_game.is_clicked():
            menu = 1

        elif load_game.is_clicked():
            menu = 2

        elif game_settings.is_clicked():
            menu = 3

    # коли нажали на кнопку нова гра
    elif menu == 1:
        # получаємо нажату клавішу
        key = pygame.key.get_pressed()
        # переміщажм гравця (перший параметер прижмає нажату клавушу, якщо w - ідем в гору і т.д, другий пареметер кількість пікселів пройдену за 1 нажимання)
        player.move(key, 5)
        player.draw()

        # виводим фпс на екран
        if show_fps:
            fps_show.set_text("FPS: " + str(clock.get_fps())[:4], 20, (255, 255, 255))
            fps_show.draw()

    # налаштування
    elif menu == 3:
        show_fps_button.draw(shift_x=5, shift_y=10)
        show_fps_button.hover_color((255, 255, 0))
        if show_fps_button.is_clicked():
            show_fps = not show_fps
            show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))
            time.sleep(0.1)



    #bg.blit(bg, (0, 0))
    clock.tick(FPS)
    pygame.display.update()
