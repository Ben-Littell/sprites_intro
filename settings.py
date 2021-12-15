import pygame
pygame.init()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
block_color = (252, 53, 3)
COLORS = [RED, GREEN, BLUE, BLACK]
x_spacing = 50
y_spacing = 40
enemy_border_check = False
WIDTH = 600
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)
FPS = 60
change_x = 0
change_x_e = 0
change_y_e = 0
missile_width = 6
missile_height = 15
block_height = 7
block_width = 7
LAYOUT = ['  XXXXXXX',
          ' XXXXXXXXX',
          'XXXXXXXXXXX',
          'XXXXXXXXXXX',
          'XXX     XXX',
          'XX       XX']
MISSILE_DELAY = 300
# fonts
sm_font = pygame.font.Font('assets/unifont.ttf', 32)
med_font = pygame.font.Font('assets/unifont.ttf', 38)
lg_font = pygame.font.Font('assets/unifont.ttf', 44)
###################
explosion_list = []
for i in range(1, 5):
    image_path = pygame.image.load(f'assets/explosion_{i}.png')
    explosion_list.append(image_path)


