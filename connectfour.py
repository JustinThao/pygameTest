#!/usr/bin/env python3
#update from macos

import pygame
from  pygame.locals import *

screen_width = 850
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Connect 4')

#define variables
line_width = 10
clicked = False
markers = []
pos = []
player = 1

#define colour
black = (0, 0, 0)
red = (255, 0, 0)

#playing grid
def draw_grid():
    bg = (128, 128, 128)
    grid = (50, 50, 50)
    screen.fill(bg)
    #six rows for x-axis
    for x in range(1,6):
        pygame.draw.line(screen, grid, (0, x * 108), (screen_width, x * 108), line_width)
    #seven columns for y-axis
    for x in range(1,7):
        pygame.draw.line(screen, grid, (x * 121, 0), (x * 121, screen_height), line_width)

for x in range(7):
    row = [0] * 6
    markers.append(row)
        
#markers for grid
def draw_makers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.circle(screen, red, (x_pos * 100 + 2, y_pos * 100 + 2), 38, line_width)
            if y == -1:
                pygame.draw.circle(screen, black, (x_pos * 100 + 2, y_pos * 100 + 2))
            y_pos += 1
        x_pos += 1


#game loop
run = True
while run:

    draw_grid()

    #add event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            cell_x = pos[0]
            cell_y = pos[1]
            print(pos)
            print(markers)
            if markers[cell_x // 108][cell_y // 121] == 0:
                markers[cell_x // 108][cell_y // 121] = player
                player *= -1
            


    pygame.display.update() 

pygame.quit()
