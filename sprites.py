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


class Enemy:
    pass


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
        self.image = pygame.Surface(())
