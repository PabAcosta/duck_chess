import pygame as pg

class Board:

  WHITE = (239, 222, 205)
  BROWN = (111, 78, 55)

  def __init__(self, x_start=0, y_start=0, width_height=640):
    self.x_start = x_start
    self.y_start = y_start
    self.width_height = width_height

  def draw_board(self, destination):
    self.square_size = self.width_height // 8

    for row in range(8):
      for col in range(8):
        x = self.x_start + col * self.square_size
        y = self.y_start + row * self.square_size

        if (row + col) % 2 == 0:
          #WHITE
          pg.draw.rect(destination, self.WHITE, (x, y, self.square_size, self.square_size))
        else:
          #BROWN
          pg.draw.rect(destination, self.BROWN, (x, y, self.square_size, self.square_size))

  def add_pieces():
    pass