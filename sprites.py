import random
import pygame
from settings import *


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.center = WIDTH//2, HEIGHT - self.rect.height
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


class Missile:
    pass
