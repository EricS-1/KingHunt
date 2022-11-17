import os
import pygame
from const import *

class Piece:

  def __init__(self, name, color, value, texture = None):
    self.name = name
    self.color = color
    self.value = value
    self.setTexture()

  def setTexture(self):
    self.texture = os.path.join("pieces", str(self.color) + str(self.name) + '.png')
    

class Pawn(Piece):
  def __init__(self, color):
    self.dir = 1
    super().__init__('pawn', color, 1)

class Knight(Piece):
  def __init__(self, color):
    super().__init__('knight', color, 3)

class Bishop(Piece):
  def __init__(self, color):
    super().__init__('bishop', color, 3)

class Rook(Piece):
  def __init__(self, color):
    super().__init__('rook', color, 5)
    
class Queen(Piece):
  def __init__(self, color):
    super().__init__('queen', color, 9)
    
class King(Piece):
  def __init__(self, color):
    super().__init__('king', color, 1000)

class Player(Piece):
  def __init__(self):
    super().__init__('player', '', None)

  def updateMovement(self, surface, row, col, upDown, rightLeft):
    texture = 'pieces/player.png'
    img = pygame.image.load(texture) 
    img = pygame.transform.scale(img, (squareSize,squareSize))
    surface.blit(img, (squareSize * (row + rightLeft) + 90, squareSize * (col + upDown) + 40))
    
    if (row + col) % 2 == 0:
      colour = (201,201,177)
    else:
      colour = (147,148,141)

    chessSquare = pygame.Rect(squareSize * row + 90, squareSize * col + 40, squareSize, squareSize)
    pygame.draw.rect(surface, colour, chessSquare)