#!/usr/bin/env python3

import pygame
from  pygame.locals import *

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Connect 4')

#define variables
line_width = 6

#define colours

def draw_grid():
    bg = (128, 128, 128)
    grid = (50, 50, 50)
    screen.fill(bg)
    #six rows for x-axis
    for x in range(1,6):
        pygame.draw.line(screen, grid, (0, x * 100), (screen_width, x * 100), line_width)
    #seven columns for y-axis
    for x in range(1,7):
        pygame.draw.line(screen, grid, (x * 142, 0), (x * 142, screen_height), line_width)
        


run = True
while run:

    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update() 

pygame.quit()