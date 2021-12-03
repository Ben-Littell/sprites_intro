import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Blocks

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()

running = True
########################################################################################################################
#################
all_sprites = pygame.sprite.Group()
#################
# Player
player_group = pygame.sprite.Group()                       # create a sprite group
player = Player('assets/player.png')                       # create a player object
player_group.add(player)                                   # add player object to group
all_sprites.add(player)
# sounds
fire_sound = pygame.mixer.Sound('assets/shoot.wav')
# Missile
missile_group = pygame.sprite.Group()
# Enemy
Enemy_group = pygame.sprite.Group()
for row in range(1, 4):
    for numb in range(1, 11):
        enemy = Enemy('assets/red.png', x_spacing * numb, y_spacing * row, row)
        Enemy_group.add(enemy)
        all_sprites.add(enemy)

########################################################################################################################
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key is pygame.K_SPACE:
                missile = Missile(player.rect.centerx - missile_width//2, player.rect.top)
                missile_group.add(missile)
                all_sprites.add(missile)
                fire_sound.play()

    # print(all_sprites)
    screen.fill(BLACK)
    missile_group.draw(screen)
    Enemy_group.draw(screen)
    player_group.draw(screen)
    # player_group.update()
    # missile_group.update()

    all_sprites.update()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()







