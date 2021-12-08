import random
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH // 2, HEIGHT - self.rect.height
        self.change_x = change_x

    def update(self):
        self.rect.x += self.change_x
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.change_x = 4
        elif keys[pygame.K_LEFT]:
            self.change_x = -4
        else:
            self.change_x = 0
        if self.rect.x >= WIDTH:
            self.rect.x = -10
        if self.rect.x <= -self.rect.width:
            self.rect.x = WIDTH


class Enemy(pygame.sprite.Sprite):

    # y_level = 0
    # changex = 1

    def __init__(self, image_path, x, y, row, x_velo, y_level):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = x + x_spacing, y
        self.row = row
        self.x_velo = x_velo
        self.y_level = y_level

    def update(self):
        self.rect.x += self.x_velo
        self.rect.y = (self.y_level + self.row) * y_spacing

    def test(self):
        print(self.x_velo)
        print('Test Complete')


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.display = display
        self.y_velo = 2
        self.image = pygame.Surface((missile_width, missile_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image.fill(WHITE)
        pygame.draw.rect(self.image, GREEN, [self.rect.x, self.rect.y, missile_width, missile_height])

    def update(self):
        self.rect.y -= self.y_velo
        if self.rect.bottom <= 0:
            self.kill()


class Blocks(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((block_dimensions, block_dimensions))
