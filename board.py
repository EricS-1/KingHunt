from const import *
from square import Square
from piece import *

class Board:

  def __init__(self):
    self.squares = [[0,0,0,0,0,0,0,0] for col in range(columns)]
    self.initialPlayerRow = 0
    self.initialPlayerCol = 7
    self.create()
    self.addPieces('black')

  def possibleMoves(self, piece, row, col):

    def knightMoves():
      lShape = [(row-2, col+1), (row-1, col+2), (row+1, col+2),(row+2, col+1),(row+2, col-1),(row+1, col-2),(row-2, col-1),(row-1, col-2)]

      for possibleMove in lShape:
        knightMoveRow,knightMoveColumn = lShape
        
        if Square.inRange(knightMoveRow,knightMoveColumn):
          if self.squares[knightMoveRow][knightMoveColumn].isEmpty():
            pass
          
    if isinstance(piece, Pawn):
      pass
    if isinstance(piece, Knight):
      pass
    if isinstance(piece, Bishop):
      pass
    if isinstance(piece, Rook):
      pass
    if isinstance(piece, Queen):
      pass
    if isinstance(piece, King):
      pass
  
  
  def create(self):
    for row in range(rows):
      for col in range(columns):
        self.squares[row][col] = Square(row,col)

  def addPieces(self, colour):
    
    self.squares[self.initialPlayerRow][self.initialPlayerCol] = Square(self.initialPlayerRow, self.initialPlayerCol, Player())
    self.squares[4][1] = Square(4, 1, Pawn(colour))
    self.squares[1][0] = Square(1, 0, Bishop(colour))
    self.squares[4][3] = Square(4, 3, King(colour))
    self.squares[3][4] = Square(3, 4, Rook(colour))