import pygame
import typing
import queue

pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()

ROWS = 80
COLS = 80
W = screen.get_width()
H = screen.get_height()
BOX_W = W / COLS
BOX_H = H / ROWS

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

def main():
    grid = [[Node(i, j) for j in range(ROWS)] for i in range(COLS)]
    for i in range(COLS):
        for j in range(ROWS):
            grid[i][j].add_neighbors(grid)

    start = grid[int(COLS / 2)][int(ROWS / 2)]
    start.visitable = True
    end = grid[70][10]
    end.visitable = True
    frontier = queue.Queue()
    frontier.put(start)
    reached = set()
    reached.add(start)

    while True:
        if not frontier.empty():
            current = frontier.get()
            current.show("pink")
            for neighbor in current.neighbors:
                if neighbor not in reached and neighbor.visitable:
                    neighbor.previous = current
                    frontier.put(neighbor)
                    reached.add(neighbor)

            if current == end:
                path = []
                tmp = current
                while tmp.previous:
                    path.append(tmp.previous)
                    tmp = tmp.previous

                for node in path:
                    node.show("blue")
                end.show("blue")
                start.show("yellow")
                end.show("yellow")

                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                    pygame.display.flip()
                    clock.tick(60)

        for i in range(COLS):
            for j in range(ROWS):
                grid[i][j].show("gray")

        for node in reached:
            node.show("red")

        for node in list(frontier.queue):
            node.show("green")

        start.show("yellow")
        end.show("yellow")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        clock.tick(60)

main()