#!/usr/bin/env python3

import pygame
import typing
import math

pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

ROWS = 80
COLS = 80
W = screen.get_width()
H = screen.get_height()
BOX_W = W / COLS
BOX_H = H / ROWS

grid: typing.Any = None

class Node:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.f = 0
        self.g = 0
        self.h = 0
        self.previous: None = None
        self.neighbors: typing.List = list()
        self.visitable = True

        import random
        if random.random() < 0.2:
            self.visitable = False

    def show(self, color: str):
        i = self.i
        j = self.j
        if self.visitable:
            pygame.draw.rect(screen, color, pygame.Rect(i * BOX_W, j * BOX_H, BOX_W, BOX_H))
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), (pygame.Rect(i * BOX_W, j * BOX_H, BOX_W, BOX_H)), width=1)
        else:
            pygame.draw.rect(screen, pygame.Color(0, 0, 0), pygame.Rect(i * BOX_W, j * BOX_H, BOX_W, BOX_H))

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

openSet: typing.List = []
closedSet: typing.List = []
start: None = None
end: None = None

def heuristic(a, b):
    return math.sqrt(((b.i - a.i) * (b.i - a.i)) + ((b.j - a.j) * (b.j - a.j)))

def setup():
    global grid
    global openSet
    global closedSet
    global start
    global end
    grid = [[Node(i, j) for j in range(ROWS)] for i in range(COLS)]
    for i in range(COLS):
        for j in range(ROWS):
            grid[i][j].add_neighbors(grid)

    start = grid[int(COLS / 2)][int(ROWS / 2)]
    end = grid[70][10]
    openSet.append(start)

def main():
    setup()
    while True:
        if len(openSet) > 0:
            lowIdx: int = 0
            for (i, node) in enumerate(openSet):
                if node.f < openSet[lowIdx].f:
                    lowIdx = i

            current = openSet[lowIdx]
            if current == end:
                path: typing.List = []
                temp = current
                while temp.previous:
                    path.append(temp.previous)
                    temp = temp.previous
                
                for node in path:
                    node.show(pygame.Color(0, 0, 255))
                end.show("yellow")
                start.show("yellow")
                
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                    pygame.display.flip()
                    clock.tick(60)

            openSet.remove(current)
            closedSet.append(current)

            for neighbor in current.neighbors:
                if neighbor not in closedSet and neighbor.visitable:
                    g = current.g + 1
                    if neighbor in openSet:
                        if g < neighbor.g:
                            neighbor.g = g
                    else:
                        neighbor.g = g
                        openSet.append(neighbor)
                    
                    neighbor.h = heuristic(neighbor, end)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.previous = current

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for list_items in grid:
            for item in list_items:
                item.show(pygame.Color(255, 255, 255))

        for item in openSet:
            item.show(pygame.Color(0, 255, 0))

        for item in closedSet:
            item.show(pygame.Color(255, 0, 0))

        end.show("yellow")
        start.show("yellow")

        pygame.display.flip()
        clock.tick(60)

main()