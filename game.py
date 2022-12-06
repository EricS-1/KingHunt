import pygame
import time
import sys

from button import Button
from const import *
from board import Board
#from dragger import Dragger 

class Game:

  def __init__(self):
    pass
    #self.dragger= Dragger
    
  def board(self, surface):
    #prints board on screen
    surface.fill(backgroundColor)

    img = pygame.image.load('board.png')
    img = pygame.transform.scale(img, (squareSize * 8, squareSize * 8))
    screen.blit(img, (9/50 * width, 2/25 * height))
  
  def showPieces(self, surface):

    #shows pieces on the screen
    for row in range(rows):
      for col in range(columns):
        if squares[row][col].hasPiece():
          piece = squares[row][col].piece
          
          img = pygame.image.load(piece.texture)
          img = pygame.transform.scale(img, (squareSize,squareSize))
          surface.blit(img, (squareSize * squares[row][col].row + 9/50 * (width), squareSize * squares[row][col].col + 2/25 * (height)))