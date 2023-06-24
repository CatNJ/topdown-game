import pygame

# імпорт вікна гри
from data.game_window import root

pygame.init()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(0,0,0), window=root):
        self.window = window
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.color_bak = color

        self.rect = pygame.Rect(x, y, width, height)

    def color(self, new_color):
        self.color = new_color

    def fill(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def collidepoint(self, pos):
        return self.rect.collidepoint(pos)

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

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        self.window.blit(self.text, (self.rect.x + shift_x, self.rect.y + shift_y))

class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        super().__init__(x=x, y=y, width=width, height=height, color=(0,0,0))
        self.image = pygame.image.load(filename)

    def draw(self):
        root.blit(self.image, (self.rect.x, self.rect.y))

    def is_clicked(self):
        if self.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True


class Button(Label):
    def is_clicked(self):
        if self.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
