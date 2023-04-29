import pygame   
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200,659))
pygame.display.set_caption('my game')
pers_forward = pygame.image.load('sprites\pers\pers_forward_1_new.png')
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
running = True
# главный цикл
while running:
    # цвет экрана
    screen.blit(fon_game, (0, 0))
    # вывести изображение на экран
    # действие при нажатии на кнопку 
    keys = pygame.key.get_pressed()
    if not keys[pygame.K_a] and not keys[pygame.K_d] and not keys[pygame.K_w] and not keys[pygame.K_s]:
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
    if keys[pygame.K_a]:
        player_x -= player_speed
    # идти направо
    elif keys[pygame.K_d]:
        player_x += player_speed
    # идти вперед
    elif keys[pygame.K_w]:
        player_y -= player_speed
    #    идти назад
    elif keys[pygame.K_s]:
        player_y += player_speed
    # считает спрайты в списке чтобы они шли бесконечно
    if player_anim_count == 3:
        player_anim_count = 0
    else:
        player_anim_count += 1
    # создание монстра и его хотьбы
    if monster_y >= 609:
        monster_y += monster_speed
        screen.blit(walk_back[player_anim_count], (monster_x, monster_y))
    elif monster_y <= 50:
        screen.blit(walk_forward[player_anim_count], (monster_x, monster_y))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(10)
