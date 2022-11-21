import pygame
import time

from const import *
from board import Board

class Game:

  def __init__(self):
    pass
    
  def board(self, surface):
    
    surface.fill(backgroundColor)

    for row in range(rows):
      for column in range(columns):
        if (row + column) % 2 == 0:
          colour = (201,201,177)
        else:
          colour = (147,148,141)

        chessSquare = pygame.Rect(squareSize * row + 90, squareSize * column + 40, squareSize, squareSize)
        
        pygame.draw.rect(surface, colour, chessSquare)

  def showPieces(self, surface):
    for row in range(rows):
      for col in range(columns):
        if squares[row][col].hasPiece():
          piece = squares[row][col].piece
          
          img = pygame.image.load(piece.texture)
          img = pygame.transform.scale(img, (squareSize,squareSize))
          surface.blit(img, (squareSize * squares[row][col].row + 90, squareSize * squares[row][col].col + 40))