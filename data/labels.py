from data.gui import Label
from data.game_window import W, H

main_label = Label(25, 25, 250, 80, (255, 255, 255))
main_label.set_text("Zombie Rush", 75, (100, 0, 0))

fps_show = Label(25, 25, 0, 0)
bullet_count_label = Label(25, 75, 0, 0)

money_label = Label(25, 125, 0, 0)

player_health_label = Label(25, 175, 0, 0)

zombie_count_label = Label(25, 225, 0, 0)

shop_price_label = Label(W//2-200+225//2-16, H/2-200+150//2+16, 0, 0)

wave_label = Label(W//2-750/6, H//2-325, 0, 0)

game_over_label = Label(W//2-750/4, H//2-37, 0, 0)
game_over_label.set_text('Game over!', 90, (255, 0, 0))
