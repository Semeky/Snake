import pygame
from settings import *
from random import randrange

length = 1 #длинна змейки
x, y = randrange(0, 800, cell_size), randrange(0, 800, cell_size)
snake = [(x, y)]
dx, dy = 0, 0 #направление движения
