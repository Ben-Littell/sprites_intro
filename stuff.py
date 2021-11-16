import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()

running = True
########################################################################################################################
player_group = pygame.sprite.Group()                       # create a sprite group
player = Player('assets/sprite_ship_3.png')                # create a player object
player_group.add(player)                                   # add player object to group
########################################################################################################################
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)
    player_group.draw(screen)
    player_group.update()

    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()







