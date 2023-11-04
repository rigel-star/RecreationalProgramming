#!/usr/bin/env python3

import pygame
import typing
import random

pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

ROWS = 50
COLS = 50
W = screen.get_width()
H = screen.get_height()
BOX_W = W / COLS
BOX_H = H / ROWS

grid: typing.Any = None

class Node:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.neighbors: typing.List = list()
        self.alive = False

        if random.random() < 0.099:
            self.alive = True

    def show(self):
        i = self.i
        j = self.j
        if self.alive: col = pygame.Color(255, 0, 0)
        else: col = pygame.Color(255, 255, 255)
        pygame.draw.rect(screen, col, pygame.Rect(i * BOX_W, j * BOX_H, BOX_W, BOX_H))
        pygame.draw.rect(screen, "black", (pygame.Rect(i * BOX_W, j * BOX_H, BOX_W, BOX_H)), width=1)

    def add_neighbors(self, grid):
        i = self.i
        j = self.j
        if i < COLS - 1:
            self.neighbors.append(grid[i + 1][j])
        if i > 0:
            self.neighbors.append(grid[i - 1][j])
        if j < ROWS - 1:
            self.neighbors.append(grid[i][j + 1])
        if j > 0:
            self.neighbors.append(grid[i][j - 1])
        if j > 0 and i > 0:
            self.neighbors.append(grid[i - 1][j - 1])
        if j > 0 and i < COLS - 1:
            self.neighbors.append(grid[i + 1][j - 1])
        if j < ROWS - 1 and i < COLS - 1:
            self.neighbors.append(grid[i + 1][j + 1])
        if j < ROWS - 1 and i > 0:
            self.neighbors.append(grid[i - 1][j + 1])


def setup():
    global grid
    grid = [[Node(i, j) for j in range(ROWS)] for i in range(COLS)]
    for i in range(COLS):
        for j in range(ROWS):
            grid[i][j].add_neighbors(grid)

def main():
    global grid
    setup()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for i in range(COLS):
            for j in range(ROWS):
                item = grid[i][j]
                alive_neighs = [n for n in item.neighbors if n.alive]
                ncount = len(alive_neighs)
                if item.alive:
                    item.alive = ncount == 2 or ncount == 3
                elif ncount == 3:
                    item.alive = True
                else:
                   item.alive = False
        
        # Draw the updated grid
        for list_items in grid:
            for item in list_items:
                item.show()
        pygame.display.flip()
        clock.tick(30)

main()