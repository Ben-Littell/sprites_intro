import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Blocks, EnemyExplosion

pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Animation Intro')

clock = pygame.time.Clock()
missile_previous_fire = pygame.time.get_ticks()
running = True
########################################################################################################################
#################
all_sprites = pygame.sprite.Group()
#################
# Player
player_group = pygame.sprite.Group()  # create a sprite group
player = Player('assets/player.png')  # create a player object
player_group.add(player)  # add player object to group
all_sprites.add(player)
# sounds
fire_sound = pygame.mixer.Sound('assets/shoot.wav')
enemy_killed = pygame.mixer.Sound('assets/invaderkilled.wav')
# Missile
missile_group = pygame.sprite.Group()
# Enemy
Enemy_group = pygame.sprite.Group()
off_set = 20
v_scale = HEIGHT // 18
h_scale = WIDTH // 12
for row in range(1, 7):
    for numb in range(11):
        x_pos = numb * h_scale + off_set
        y_pos = row * v_scale + off_set
        enemy = Enemy('assets/red.png', x_pos, y_pos)
        Enemy_group.add(enemy)
enemy_direction = 1
# blocks
block_group = pygame.sprite.Group()
start_values = [100, 225, 350, 475]
for start in start_values:
    for row_index, row in enumerate(LAYOUT):
        for col_index, col in enumerate(row):
            if col == 'X':
                x_position = col_index*block_width + start
                y_position = row_index*block_height + 600
                block = Blocks(x_position, y_position, screen)
                block_group.add(block)
                all_sprites.add(block)
# fonts
score = 0
# explosion group
explosion_group = pygame.sprite.Group()
########################################################################################################################
# game loop
while running:
    # get all mouse, keyboard, controller events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key is pygame.K_SPACE:
                missile_current_fire = pygame.time.get_ticks()
                if missile_current_fire - missile_previous_fire > MISSILE_DELAY:
                    missile_previous_fire = missile_current_fire
                    missile = Missile(player.rect.centerx - missile_width // 2, player.rect.top)
                    missile_group.add(missile)
                    all_sprites.add(missile)
                    fire_sound.play()

    # print(all_sprites)
    enemy_kills = pygame.sprite.groupcollide(missile_group, Enemy_group, True, True)
    player_kills = pygame.sprite.groupcollide(player_group, Enemy_group, True, True)
    enemy_blocks = pygame.sprite.groupcollide(Enemy_group, block_group, False, True)
    missile_blocks = pygame.sprite.groupcollide(missile_group, block_group, True, True)
    if enemy_kills:
        enemy_killed.play()
        score += 1
        for hit in enemy_kills:
            explosion = EnemyExplosion(hit.rect.center)
            explosion_group.add(explosion)
            all_sprites.add(explosion)
    enemies = Enemy_group.sprites()
    for enemy in enemies:
        if enemy.rect.right >= WIDTH:
            enemy_direction = -1
            if enemies:
                for alien in enemies:
                    alien.rect.y += 2
        elif enemy.rect.x <= 0:
            enemy_direction = 1
            if enemies:
                for alien in enemies:
                    alien.rect.y += 2

    screen.fill(BLACK)
    score_object = sm_font.render(f'Score: {score}', True, WHITE)
    score_rect = score_object.get_rect()
    score_rect.center = 100, 20
    screen.blit(score_object, score_rect)
    missile_group.draw(screen)
    Enemy_group.draw(screen)
    player_group.draw(screen)
    block_group.draw(screen)
    explosion_group.draw(screen)

    # missile_group.update()
    all_sprites.update()
    Enemy_group.update(enemy_direction)
    # player_group.update()
    pygame.display.flip()

    clock.tick(FPS)

# outside of game loop
pygame.quit()
