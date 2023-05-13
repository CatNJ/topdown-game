import time

import pygame
from random import randint as r

from data.game_window import *
from data.gui import *
from data.player import Player


pygame.init()


root.fill((0, 0, 0))

clock = pygame.time.Clock()

show_fps = False


main_text = Label(25, 25, 150, 75, (255, 255, 255))
main_text.set_text("fuck game", 75, (100, 0, 0))

new_game = Button(25, 425, 250, 50, (255, 255, 255))
new_game.set_text("New game", 25, (0, 0, 0))

load_game = Button(25, 525, 250, 50, (255, 255, 255))
load_game.set_text("Load game", 25, (0, 0, 0))

game_settings = Button(25, 625, 250, 50, (255, 255, 255))
game_settings.set_text("Settings", 25, (0, 0, 0))

show_fps_button = Button(100, 400, 250, 50, (255, 255, 255))

show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))

player = Player(W/2, H/2, 50, 50, (0, 255, 0))

fps_show = Label(25, 25, 0, 0)
back_button = Button(750, 625, 250, 50, (255, 255, 255))
back_button.set_text("<- Back", 25, (0, 0, 0))



fps_game = 0
menu = 0

while True:
    root.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu = 0


    if menu != 1:
        main_text.draw()

    if menu != 0 and menu != 1:
        back_button.draw()
        back_button.hover_color((255, 255, 0))
        if back_button.is_clicked():
            menu = 0

    if menu == 0:
        # new_game.rect.x = 25
        # load_game.rect.x = 25
        # game_settings.rect.x = 25
        player.rect.x = W/2
        player.rect.y = H/2

        root.fill((0, 0, 0))
        main_text.draw()

        new_game.draw(shift_x=5, shift_y=10)
        new_game.hover_color((255, 255, 0))


        load_game.draw(shift_x=5, shift_y=10)
        load_game.hover_color((255, 255, 0))


        game_settings.draw(shift_x=5, shift_y=10)
        game_settings.hover_color((255, 255, 0))


        if new_game.is_clicked():
            menu = 1

        elif load_game.is_clicked():
            menu = 2

        elif game_settings.is_clicked():
            menu = 3

    elif menu == 1:
        key = pygame.key.get_pressed()
        player.move(key, 5)
        player.draw()

        if show_fps:
            fps_show.set_text("FPS: " + str(clock.get_fps())[:4], 20, (255, 255, 255))
            fps_show.draw()

    elif menu == 3:
        show_fps_button.draw(shift_x=5, shift_y=10)
        show_fps_button.hover_color((255, 255, 0))
        if show_fps_button.is_clicked():
            show_fps = not show_fps
            show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))
            time.sleep(0.1)



    clock.tick(60)
    pygame.display.update()
