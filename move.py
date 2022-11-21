import pygame

from const import *
from square import Square
from piece import Player

class Move:
  def __init__(self):
    pass

  def updateMovement(self, surface, row, col, upDown, rightLeft):
    texture = 'pieces/player.png'
    img = pygame.image.load(texture) 
    img = pygame.transform.scale(img, (squareSize,squareSize))
    
    movedRow = row + rightLeft
    movedCol = col + upDown
    
    surface.blit(img, (squareSize * (movedRow) + 90, squareSize * (movedCol) + 40))

    squares[row][col] = Square(row,col)
    squares[movedRow][movedCol] = Square(movedRow,movedCol,Player())
    
    print(squares[row][col])
    print(squares[movedRow][movedCol])
    
    if (row + col) % 2 == 0:
      colour = (201,201,177)
    else:
      colour = (147,148,141)
    chessSquare = pygame.Rect(squareSize * row + 90, squareSize * col + 40, squareSize, squareSize)
    pygame.draw.rect(surface, colour, chessSquare)