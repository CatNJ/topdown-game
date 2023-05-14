import pygame

# імпорт вікна гри
from data.game_window import root

pygame.init()

# клас
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(0,0,0), window=root):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color_bak = color

        # створення прямокутника
        self.rect = pygame.Rect(x, y, width, height)

    # зміна кольору на новий
    def color(self, new_color):
        self.color = new_color

    # малювання прямокутника на екрані
    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    # точка пересічення
    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

    # пересічення з іншим прямокутником
    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text='', font_size=12, text_color=(255, 255, 255)):
        font = pygame.font.SysFont('verdana', font_size)
        self.text = font.render(text, True, text_color)

    def hover_color(self, color):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = color

        else:
            self.color = self.color_bak

    # малюєм прямокунтник з текстом
    def draw(self, shift_x=0, shift_y=0):
        self.draw()
        self.window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))


class Button(Label):
    def is_clicked(self):
        # якщо мишка наведина на кнопку і нажата ліваклавіша миші
        if self.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
