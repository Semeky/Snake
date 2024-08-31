import pygame 
from random import randrange

pygame.init()
res = 800
clock = pygame.time.Clock()
screen = pygame.display.set_mode((res, res))
fps = 10
cell_size = 50
apple = randrange(0, 800, cell_size), randrange(0, 800, cell_size)
length = 1 #длинна змейки
x, y = randrange(0, 800, cell_size), randrange(0, 800, cell_size)
snake = [(x, y)]
dx, dy = 0, 0 #направление движения
dirs = {'W': True, 'S': True, 'A': True, 'D': True }

while True:
    screen.fill(pygame.Color('black'))    
    #отрисовывание змейки
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, cell_size, cell_size))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, cell_size, cell_size))    
    #движение змейки
    x += dx * cell_size
    y += dy * cell_size
    snake.append ((x, y))
    snake = snake[-length:]
    #поедание яблока
    if snake[0] == apple:
        apple = randrange(0, 800, cell_size), randrange(0, 800, cell_size)
        length += 1
    #колизия предметов
    if x < 0 or x > res - cell_size or y < 0 or y  > res - cell_size:
        break
    if len(snake) != len(set(snake)):
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.display.flip()
    clock.tick(fps)
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs ['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs ['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs ['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs ['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}