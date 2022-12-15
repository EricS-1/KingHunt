import os
import pygame
from const import *

class Piece:
  '''
  Piece object that contains all the information of all the pieces

  Attributes 
  ----------
  name: str
    the piece name
  
  color: int
    the piece's colour
    
  value: int
    the value of the piece

  texture: str
    the directory of the piece's image

  Methods
  -------
  setTexture() -> returns none
    sets the proper piece texture
  '''

  def __init__(self, name, color, value, texture = None):
    '''
  	Constructor to build a AI object and to execute its functions
   
  	Parameters
  	----------
    name: str
      the piece name
  
    color: int
      the piece's colour
    
    value: int
      the value of the piece
  
    texture: str
      the directory of the piece's image

    Returns
    ----------
    nothing
  	'''
    self.name = name
    self.color = color
    self.value = value
    self.setTexture()

  def setTexture(self):
    '''
  	Finds and sets the proper piece texture
   
  	Parameters
  	----------
    none

    Returns
    ----------
    nothing
  	'''
    self.texture = os.path.join("pieces", str(self.color) + str(self.name) + '.png')

class Pawn(Piece): 
  '''
  Pawn object that is a child class to Piece and contains all the information the pawn

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the Pawn object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('pawn', color, 1)

class Knight(Piece):
  '''
  Knight object that is a child class to Piece and contains all the information the knight

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the Knight object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('knight', color, 3)

class Bishop(Piece):
  '''
  Bishop object that is a child class to Piece and contains all the information of the bishop

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the Bishop object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('bishop', color, 3)

class Rook(Piece):
  '''
  Rook object that is a child class to Piece and contains all the information of the rook

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the Rook object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('rook', color, 5)
    
class Queen(Piece):
  '''
  Queen object that is a child class to Piece and contains all the information of the queen

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the Queen object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('queen', color, 9)
    
class King(Piece):
  '''
  King object that is a child class to Piece and contains all the information of the king

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self, color):
    '''
  	Constructor to build the King object
   
  	Parameters
  	----------
    color: str
      color of the piece

    Returns
    ----------
    nothing
  	'''
    super().__init__('king', color, 1000)

class Player(Piece):
  '''
  Player object that is a child class to Piece and contains all the information of the player

  Attributes 
  ----------
  color: str
    color of the piece
    
  Methods
  -------
  none
  '''
  def __init__(self):
    '''
  	Constructor to build the Player object
   
  	Parameters
  	----------
    nothing

    Returns
    ----------
    nothing
  	'''
    super().__init__('player', '', None)