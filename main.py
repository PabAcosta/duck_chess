import pygame
import sys

from game.board import Board

pygame.init()

WIDTH, HEIGHT = 640, 640
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Duck Chess")

clock = pygame.time.Clock()
board = Board()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))
    board.draw_board(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()