import pygame   
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,659))
pygame.display.set_caption('my game')
pers_forward = pygame.image.load('sprites\pers\pers_forward_1_new.png')
pers_back = pygame.image.load('sprites\pers\pers_back_1_new.png')
pers_left = pygame.image.load('sprites\pers\pers_left_1_new.png')
pers_right = pygame.image.load('sprites\pers\pers_right_1_new.png')
fon_game = pygame.image.load('sprites\game_fon.png')
# бежать вперед
walk_forward = [
    pygame.image.load('sprites\pers\pers_forward_1_new.png'),
    pygame.image.load('sprites\pers\pers_forward_2_new.png'),
    pygame.image.load('sprites\pers\pers_forward_1_new.png'),
    pygame.image.load('sprites\pers\pers_forward_3_new.png')
    ]
# бежать назад
walk_back = [
    pygame.image.load('sprites\pers\pers_back_1_new.png'),
    pygame.image.load('sprites\pers\pers_back_2_new.png'),
    pygame.image.load('sprites\pers\pers_back_1_new.png'),
    pygame.image.load('sprites\pers\pers_back_3_new.png')
    ]
# бежать налево
walk_left = [
    pygame.image.load('sprites\pers\pers_left_1_new.png'),
    pygame.image.load('sprites\pers\pers_left_2_new.png'),
    pygame.image.load('sprites\pers\pers_left_1_new.png'),
    pygame.image.load('sprites\pers\pers_left_3_new.png')
    ]
# бежать направо
walk_right = [
    pygame.image.load('sprites\pers\pers_right_1_new.png'),
    pygame.image.load('sprites\pers\pers_right_2_new.png'),
    pygame.image.load('sprites\pers\pers_right_1_new.png'),
    pygame.image.load('sprites\pers\pers_right_3_new.png')
    ]
# позиция спрайта в списке
player_anim_count = 0
# скорость, координаты x и y персонажа
player_speed = 15
player_x = 600
player_y = 329
# скорость, координаты x и y монстра
monster_speed = 15
monster_x = 100
monster_y = 50
# направление
direction = 1
# главный цикл
running = True
while running:
    # цвет экрана
    screen.blit(fon_game, (0, 0))
    # вывести изображение на экран
    # действие при нажатии на кнопку 
    keys = pygame.key.get_pressed()
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and direction == 1:
        screen.blit((pers_left), (player_x, player_y))
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and direction == 2:
        screen.blit((pers_right), (player_x, player_y))
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and direction == 3:
        screen.blit((pers_back), (player_x, player_y))
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s] and direction == 4:
        screen.blit((pers_forward), (player_x, player_y))
    # спрайт налево
    if keys[pygame.K_a]:
        screen.blit(walk_left[player_anim_count], (player_x, player_y))
    # спрайт направо
    elif keys[pygame.K_d]:
        screen.blit(walk_right[player_anim_count], (player_x, player_y))
    # спрайт назад
    elif keys[pygame.K_w]:
        screen.blit(walk_back[player_anim_count], (player_x, player_y))
    # спрайт вперед
    elif keys[pygame.K_s]:
        screen.blit(walk_forward[player_anim_count], (player_x, player_y))
    # идти налево
    if keys[pygame.K_a] and player_x >= 10:
        player_x -= player_speed
        # направление
        direction = 1
    # идти направо
    elif keys[pygame.K_d] and player_x <= 1139:
        player_x += player_speed
        # направление
        direction = 2
    # идти вперед
    elif keys[pygame.K_w] and player_y >= 10:
        player_y -= player_speed
        # направление
        direction = 3
    # идти назад
    elif keys[pygame.K_s] and player_y <= 570:
        player_y += player_speed
        # направление
        direction = 4
    # идти влево и вперед 
    if keys[pygame.K_a] and keys[pygame.K_w] and player_x >= 10 and player_y >= 10:
        player_y -= 6
        player_x -= 6
    # идти вправо и направо
    if keys[pygame.K_w] and keys[pygame.K_d] and player_x >= 10 and player_y >= 10:
        player_y -= 6
        player_x += 6
    # идти вправо и вниз
    if keys[pygame.K_d] and keys[pygame.K_s] and player_x >= 10 and player_y >= 10:
        player_x += 6
        player_y += 6
    # идти влево и вниз
    if keys[pygame.K_a] and keys[pygame.K_s] and player_x >= 10 and player_y >= 10:
        player_y += 6
        player_x -= 6
    # считает спрайты в списке чтобы они шли бесконечно
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1   
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
    clock.tick(10)
