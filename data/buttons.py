# кнопки

from data.gui import Button
from data.settings import *

new_game = Button(25, 425, 250, 50, (255, 255, 255))
new_game.set_text("New game", 25, (0, 0, 0))

load_game = Button(25, 525, 250, 50, (255, 255, 255))
load_game.set_text("Load game", 25, (0, 0, 0))

game_settings = Button(25, 625, 250, 50, (255, 255, 255))
game_settings.set_text("Settings", 25, (0, 0, 0))

show_fps_button = Button(100, 400, 250, 50, (255, 255, 255))
show_fps_button.set_text("Show FPS: ON" if show_fps else "Show FPS: OFF", 25, (0,0,0))

back_button = Button(750, 625, 250, 50, (255, 255, 255))
back_button.set_text("<- Back", 25, (0, 0, 0))
