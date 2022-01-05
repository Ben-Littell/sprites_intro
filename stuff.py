import pygame
import random
from settings import *
from sprites import Player, Enemy, Missile, Blocks, EnemyExplosion, EnemyMissiles, SpaceShip

pygame.init()


def start_screen():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Space Invaders')
    clock = pygame.time.Clock()
    running = True
    while running:
        # get all mouse, keyboard, controller events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_RETURN:
                    running = False

        screen.fill(BLACK)
        title = sm_font.render(f'Welcome to Space invaders', True, WHITE)
        title_rect = title.get_rect()
        title_rect.center = 300, 20
        screen.blit(title, title_rect)
        start = sm_font.render(f'Press Enter to start', True, WHITE)
        start_rect = start.get_rect()
        start_rect.center = 300, 100
        screen.blit(start, start_rect)
        pygame.display.flip()

        clock.tick(FPS)


def game_over():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Space Invaders')
    clock = pygame.time.Clock()
    running = True
    while running:
        # get all mouse, keyboard, controller events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key is pygame.K_RETURN:
                    running = False
                if event.key is pygame.K_q:
                    quit()

        screen.fill(BLACK)
        game_done = sm_font.render(f'Game Over', True, WHITE)
        game_rect = game_done.get_rect()
        game_rect.center = 300, 20
        screen.blit(game_done, game_rect)
        exit_game = sm_font.render(f'Press Q to Exit', True, WHITE)
        exit_rect = exit_game.get_rect()
        exit_rect.center = 300, 100
        screen.blit(exit_game, exit_rect)
        restart_game = sm_font.render(f'Press Enter to Restart', True, WHITE)
        restart_rect = restart_game.get_rect()
        restart_rect.center = 300, 180
        screen.blit(restart_game, restart_rect)
        with open('score.txt') as file:
            line = file.readline()
            score_game = sm_font.render(f'High Score: {line}', True, WHITE)
            score_rect = score_game.get_rect()
            score_rect.center = 300, 260
            screen.blit(score_game, score_rect)
        pygame.display.flip()

        clock.tick(FPS)


def play():
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Animation Intro')

    clock = pygame.time.Clock()
    missile_previous_fire = pygame.time.get_ticks()
    ship_previous = pygame.time.get_ticks()
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
    rounds_counter = 0
    Enemy_group_m = pygame.sprite.Group()
    Enemy_group_g = pygame.sprite.Group()
    Enemy_group_r = pygame.sprite.Group()
    Enemy_group_y = pygame.sprite.Group()
    off_set = 20
    v_scale = HEIGHT // 18
    h_scale = WIDTH // 12
    for row in range(1, 7):
        for numb in range(11):
            x_pos = numb * h_scale + off_set
            y_pos = row * v_scale + off_set
            if row <= 2:
                point_val = 10
                enemy = Enemy('assets/green.png', x_pos, y_pos, point_val)
                Enemy_group_g.add(enemy)
                Enemy_group_m.add(enemy)
            elif row <= 4:
                point_val = 5
                enemy = Enemy('assets/yellow.png', x_pos, y_pos, point_val)
                Enemy_group_y.add(enemy)
                Enemy_group_m.add(enemy)
            else:
                point_val = 1
                enemy = Enemy('assets/red.png', x_pos, y_pos, point_val)
                Enemy_group_r.add(enemy)
                Enemy_group_m.add(enemy)
    enemy_direction = 1
    # blocks
    block_group = pygame.sprite.Group()
    start_values = [100, 225, 350, 475]
    for start in start_values:
        for row_index, row in enumerate(LAYOUT):
            for col_index, col in enumerate(row):
                if col == 'X':
                    x_position = col_index * block_width + start
                    y_position = row_index * block_height + 600
                    block = Blocks(x_position, y_position, screen)
                    block_group.add(block)
                    all_sprites.add(block)
    # fonts
    score = 0
    player_lives = 2
    # explosion group
    explosion_group = pygame.sprite.Group()
    # bombs
    bomb_group = pygame.sprite.Group()
    # Space Ship
    ship_delay = 10000
    ship_group = pygame.sprite.Group()

    ########################################################################################################################
    # game loop
    while running:
        # get all mouse, keyboard, controller events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

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
        if not Enemy_group_g and not Enemy_group_r and not Enemy_group_y:
            running = False
        ship_ticks = pygame.time.get_ticks()
        if ship_ticks - ship_previous >= ship_delay:
            ship_previous = ship_ticks
            ship = SpaceShip('assets/ufo.png')
            ship_group.add(ship)
        enemy_kills_g = pygame.sprite.groupcollide(Enemy_group_g, missile_group, True, True)
        enemy_kills_y = pygame.sprite.groupcollide(Enemy_group_y, missile_group, True, True)
        enemy_kills_r = pygame.sprite.groupcollide(Enemy_group_r, missile_group, True, True)
        player_kills = pygame.sprite.groupcollide(player_group, Enemy_group_m, True, True)
        enemy_blocks = pygame.sprite.groupcollide(Enemy_group_m, block_group, False, True)
        missile_blocks = pygame.sprite.groupcollide(missile_group, block_group, True, True)
        enemy_missile_blocks = pygame.sprite.groupcollide(bomb_group, block_group, True, True)
        enemy_missile_player = pygame.sprite.groupcollide(bomb_group, player_group, True, False)
        missile_missile = pygame.sprite.groupcollide(missile_group, bomb_group, True, True)
        ship_missile = pygame.sprite.groupcollide(missile_group, ship_group, True, True)
        if ship_missile:
            enemy_killed.play()
            score += 20
            explosion = EnemyExplosion(ship.rect.center)
            explosion_group.add(explosion)
            all_sprites.add(explosion)
        if enemy_kills_r:
            enemy_killed.play()
            for hit in enemy_kills_r:
                score += 1
                explosion = EnemyExplosion(hit.rect.center)
                explosion_group.add(explosion)
                all_sprites.add(explosion)
        if enemy_kills_y:
            enemy_killed.play()
            for hit in enemy_kills_y:
                score += 5
                explosion = EnemyExplosion(hit.rect.center)
                explosion_group.add(explosion)
                all_sprites.add(explosion)
        if enemy_kills_g:
            enemy_killed.play()
            for hit in enemy_kills_g:
                score += 10
                explosion = EnemyExplosion(hit.rect.center)
                explosion_group.add(explosion)
                all_sprites.add(explosion)
        if player_kills:
            running = False
        if enemy_missile_player:
            enemy_killed.play()
            explosion = EnemyExplosion(player.rect.center)
            explosion_group.add(explosion)
            all_sprites.add(explosion)
            player_lives -= 1
            if player_lives < 0:
                running = False
        enemies = Enemy_group_m.sprites()
        for enemy in enemies:
            if enemy.rect.top > HEIGHT:
                running = False
        for enemy in enemies:
            chance = random.randint(0, 1000)
            if chance == 10 or chance == 1:
                enemy_missile = EnemyMissiles(enemy.rect.centerx, enemy.rect.centery, screen)
                bomb_group.add(enemy_missile)
                all_sprites.add(enemy_missile)
            if enemy.rect.right >= WIDTH:
                if enemy.rect.y <= 500:
                    enemy_direction = -1
                else:
                    enemy_direction = -2
                if enemies:
                    for alien in enemies:
                        alien.rect.y += 2
            elif enemy.rect.x <= 0:
                if enemy.rect.y <= 500:
                    enemy_direction = 1
                else:
                    enemy_direction = 2
                if enemies:
                    for alien in enemies:
                        alien.rect.y += 2
        for ship in ship_group:
            chance2 = random.randint(0, 50)
            if chance2 == 10:
                enemy_missile = EnemyMissiles(ship.rect.centerx, ship.rect.centery, screen)
                bomb_group.add(enemy_missile)
                all_sprites.add(enemy_missile)

        screen.fill(BLACK)
        score_object = sm_font.render(f'Score: {score}', True, WHITE)
        score_rect = score_object.get_rect()
        score_rect.center = 100, 20
        screen.blit(score_object, score_rect)
        lives_object = sm_font.render(f'Lives: {player_lives}', True, WHITE)
        lives_rect = lives_object.get_rect()
        lives_rect.center = 500, 20
        screen.blit(lives_object, lives_rect)
        missile_group.draw(screen)
        Enemy_group_m.draw(screen)
        player_group.draw(screen)
        block_group.draw(screen)
        bomb_group.draw(screen)
        explosion_group.draw(screen)
        ship_group.draw(screen)

        # missile_group.update()
        all_sprites.update()
        Enemy_group_m.update(enemy_direction)
        # player_group.update()
        pygame.display.flip()
        ship_group.update()

        clock.tick(FPS)
    with open('score.txt', 'r') as file:
        line = file.readline()
        if int(line) < score:
            with open('score.txt', 'w') as file2:
                file2.write(str(score))


start_screen()
while True:
    play()
    game_over()
# outside of game loop
pygame.quit()
