from const import *
from square import Square
from piece import *

class Board:
  '''
  Board object that sets the pieces to its repsective squares on the board

  Attributes 
  ----------
  nothing

  Methods
  -------
  addMove() -> returns none
    adds move to a list
    
  possibleMoves(piece, row, col) -> returns none
    generates all the possible moves of the piece

  makeMove() -> bool
    searches for a possible move that attacks the player

  makeRandomMove() -> returns none
    make a random possible move
  '''

  def __init__(self):
    '''
  	Constructor to build the board object and runs the create() method
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    
    self.create()  
  
  def create(self):
    '''
  	Sets each square on the board as an object
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    for row in range(rows):
      for col in range(columns):
        squares[row][col] = Square(row,col)

  
  def level1(self, colour):
    '''
  	Sets the squares on the board to contain pieces for the first level
   
  	Parameters
  	----------
    colour: str
      the colour of the enemy pieces
    
    Returns
    ----------
    nothing
  	'''
    
    squares[0][7] = Square(0, 7, Player())
    squares[4][1] = Square(4, 1, Pawn(colour))
    squares[1][0] = Square(1, 0, Bishop(colour))
    squares[4][3] = Square(4, 3, King(colour))
    squares[3][4] = Square(3, 4, Rook(colour))

  def level2(self, colour):
    '''
  	Sets the squares on the board to contain pieces for the second level
   
  	Parameters
  	----------
    colour: str
      the colour of the enemy pieces
    
    Returns
    ----------
    nothing
  	'''
    
    squares[1][7] = Square(1, 7, Player())
    squares[0][1] = Square(0, 1, Pawn(colour))
    squares[1][1] = Square(1, 1, Pawn(colour))
    squares[3][0] = Square(3, 0, Queen(colour))
    squares[5][0] = Square(5, 0, Rook(colour))
    squares[6][0] = Square(6, 0, King(colour))
    squares[6][1] = Square(6, 1, Bishop(colour))
    squares[7][1] = Square(7, 1, Pawn(colour))
    squares[3][2] = Square(3, 2, Pawn(colour))
    squares[5][2] = Square(5, 2, Pawn(colour))
    squares[5][3] = Square(5, 3, Pawn(colour))
    squares[2][4] = Square(2, 4, Rook(colour))

  def level3(self, colour):
    '''
  	Sets the squares on the board to contain pieces for the third level
   
  	Parameters
  	----------
    colour: str
      the colour of the enemy pieces
    
    Returns
    ----------
    nothing
  	'''

    squares[2][7] = Square(2, 7, Player())
    squares[0][2] = Square(0, 2, Pawn(colour))
    squares[1][3] = Square(1, 3, Pawn(colour))
    squares[2][3] = Square(2, 3, Pawn(colour))
    squares[1][2] = Square(1, 2, King(colour))
    squares[2][2] = Square(2, 2, Queen(colour))
    squares[3][1] = Square(3, 1, Rook(colour))
    squares[3][2] = Square(3, 2, Rook(colour))
    squares[3][3] = Square(3, 3, Bishop(colour))
    squares[7][2] = Square(7, 2, Pawn(colour))
    squares[6][3] = Square(6, 3, Pawn(colour))

  def level4(self, colour):
    '''
  	Sets the squares on the board to contain pieces for the fourth level
   
  	Parameters
  	----------
    colour: str
      the colour of the enemy pieces
    
    Returns
    ----------
    nothing
  	'''

    squares[3][7] = Square(3, 7, Player())
    
    for i in range(8):
      squares[i][1] = Square(i, 1, Pawn(colour))

    squares[0][0] = Square(0, 0, Rook(colour))
    squares[1][0] = Square(1, 0, Knight(colour))
    squares[2][0] = Square(2, 0, Bishop(colour))
    squares[3][0] = Square(3, 0, Queen(colour))
    squares[4][0] = Square(4, 0, King(colour))
    squares[5][0] = Square(5, 0, Bishop(colour))
    squares[6][0] = Square(6, 0, Knight(colour))
    squares[7][0] = Square(7, 0, Rook(colour))
    