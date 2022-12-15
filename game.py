import pygame
import time
import sys

from button import Button
from const import *
from board import Board
from dragger import Dragger
#from dragger import Dragger 

class Game:
  '''
  Game object that loads the board and the pieces onto the screen 

  Attributes 
  ----------
  dragger: class
    opens the dragger class
  
  Methods
  -------
  board() -> returns none
    loads the chess board on the screen
    
  showPieces() -> returns none
    loads all of the pieces on the screen
  '''
  
  def __init__(self):
    '''
  	Constructor to build a Game object
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''

    self.dragger = Dragger()
    
  def board(self):
    '''
  	Loads the chess board on the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    
    #prints board on screen
    screen.fill(backgroundColor)

    img = pygame.image.load('gameLayout/board.png')
    img = pygame.transform.scale(img, (squareSize * 8, squareSize * 8))
    
    screen.blit(img, (9/50 * width, 2/25 * height))
  
  def showPieces(self):
    '''
  	Loads the pieces on the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''

    #shows pieces on the screen
    for row in range(rows):
      for col in range(columns):
        if squares[row][col].hasPiece():
          piece = squares[row][col].piece
          
          img = pygame.image.load(piece.texture)
          img = pygame.transform.scale(img, (squareSize,squareSize))
          screen.blit(img, (squareSize * squares[row][col].row + 9/50 * (width), squareSize * squares[row][col].col + 2/25 * (height)))

