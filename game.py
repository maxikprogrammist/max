# импортируем и инициализируем pygame
import pygame
pygame.init()
# создаём окно, название и иконку окна, фон, FPS
HEIGHT = 720
WIDTH = 360
screen = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption('динозаврик')
monster = pygame.image.load('monster_2.png').convert_alpha()
pygame.display.set_icon(monster)
game_fon = pygame.image.load('game_fon.png').convert_alpha()
fon_x = 0
clock = pygame.time.Clock()
FPS = 20

label = pygame.font.Font(None, 40)
lose_label = label.render('Вы проиграли', False, (193, 196, 199))
restart_label = label.render('начать заново', False, (193, 196, 199))
restart_label_rect = restart_label.get_rect(topleft = (250, 200))

# список, содержащий картинки player 
player_walk = [
    pygame.image.load('player_right_1.png').convert_alpha(),
    pygame.image.load('player_right_2.png').convert_alpha(),
    pygame.image.load('player_right_1.png').convert_alpha(),
    pygame.image.load('player_right_3.png').convert_alpha()
]
# список, запоминающий количество монстров на экране
monster_list = []
# характеристики player
monster_x = 750
monster_y = 250
# характеристики player
player_x = 100
player_y = 250
player_anim_count = 0
# характеристики прыжка
with open ('1.txt', 'r') as file:
    top_score = file.read()
if top_score != '':
    top = int(top_score)
else:
    top = 0

is_jump = False
jump_count = 8
# новый таймер для появления monster
monster_timer = pygame.USEREVENT + 1
pygame.time.set_timer(monster_timer, 2000)
# проверка, есть ли проигрыш или нет
# счёт игрока
score = 0
gameplay = True
# главный цикл
running = True
while running:
    # отрисовываем на экране фон, player, monster
    screen.blit(game_fon, (fon_x, 0))
    screen.blit(game_fon, (fon_x + 720, 0))
    screen.blit(player_walk[player_anim_count], (player_x, player_y))
    if gameplay:
        text_score = label.render("Набрано очков:" + str(score),1,(255,255,255))
        screen.blit(text_score, (10, 10))
        # создаем невидимый квадрат вокруг player и monster чтобы отслеживать их соприкосновения
        player_rect = player_walk[0].get_rect(topleft = (player_x, player_y))
        if monster_list:
            for (i, el) in enumerate(monster_list):
                screen.blit(monster, el)
                el.x -= 12
                if el.x < -60:
                    monster_list.pop(i)
                if el.x == 66:
                    score += 1
                    if top <= score:
                        top+=1
                if player_rect.colliderect(el):
                    gameplay = False
        # дыижение фона, если фон закончился то в конец добавляется новый фон
        fon_x -= 4
        if fon_x == -720:
            fon_x = 0
        # движение монстра
        if monster_x <= -60:
            monster_x = 750
        # теперь можно обрабатывать события на нажатие клавишь
        keys = pygame.key.get_pressed()
        # прыжок
        if not is_jump:
            if keys[pygame.K_SPACE]:
                is_jump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 2
                else:
                    player_y += (jump_count ** 2) / 2
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 8
        # счётчик анимации player
        if player_anim_count == 3:
            player_anim_count = 0
        else:
            player_anim_count += 1 
    else:
        screen.fill((0, 0, 0))
        screen.blit(lose_label, (240, 100))
        screen.blit(restart_label, restart_label_rect)
        with open('1.txt','w') as file:
            file.write(str(top))
        text_top = label.render('Максимум очков: ' + str(top), 1, (255, 255, 255))
        screen.blit(text_top, (10, 10))
        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            monster_list.clear()
            score = 0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == monster_timer:
            monster_list.append(monster.get_rect(topleft = (750, 250)))
    clock.tick(FPS)
        
