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

    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, x_velo):
        self.rect.x += x_velo


class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        # self.display = display
        self.y_velo = 4
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
    def __init__(self, x, y, display):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((block_height, block_width))
        self.image.fill(block_color)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        pygame.draw.rect(display, block_color, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])


class EnemyMissiles(pygame.sprite.Sprite):
    def __init__(self, x, y, display):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((missile_width, missile_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = x, y
        self.y_velo = 1
        pygame.draw.rect(display, WHITE, [self.rect.x, self.rect.y, self.rect.width, self.rect.height])

    def update(self):
        self.rect.y += self.y_velo
        if self.rect.top >= HEIGHT:
            self.kill()


class EnemyExplosion(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_list[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.frame_rate = 50
        self.kill_center = center
        self.prev_update = pygame.time.get_ticks()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.prev_update > self.frame_rate:
            self.prev_update = now
            self.frame += 1
        if self.frame == len(explosion_list):
            self.kill()
        else:
            self.image = explosion_list[self.frame]
            self.rect = self.image.get_rect()
            self.rect.center = self.kill_center
