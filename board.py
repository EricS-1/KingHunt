from const import *
from square import Square
from piece import *
from move import Move

class Board:

  def __init__(self):
    self.initialPlayerRow = 0
    self.initialPlayerCol = 7
    self.create()
    self.addPieces('black')

  def possibleMoves(self, piece, row, col):
    def straightMoves(incrs):
      for incri in incriments:
        rowIncri, colIncri = incri
        possibleMoveRow = row + rowIncri
        possibleMoveCol = col + colIncri

        while True:
          if Square.inRange(possibleMoveRow,possibleMoveCol):

            initial = Square(row, col)
            final = Square(possibleMoveRow, possibleMoveCol)
            
            if squares[possibleMoveRow][possibleMoveCol].isEmpty():
              Piece().addMove((initial, final))

            if squares[possibleMoveRow][possibleMoveCol].isPlayer():
              Piece().addMove((initial, final))
              break

            else:
              break

          possibleMoveRow = row + rowIncri
          possibleMoveCol = col + colIncri 
          
    def nonIncrimentalMoves(moveList):
      for possibleMove in moveList:
        moveRow, moveCol = possibleMove

        if Square.inRange(moveRow,moveCol):
          if squares[moveRow][moveCol].isEmptyOrPlayer():
            
            initial = Square(row, col)
            final = Square(moveRow, moveCol)

            Piece().addMove((initial, final))
      
    def rookMoves():
      straightMoves([(-1, 0), (1, 0), (0, 1), (0,-1)])

    def bishopMoves():
      straightMoves([(-1, 1), (-1, -1), (1, 1), (1,-1)])

    def queenMoves():
      rookMoves()
      bishopMoves()

    def kingMoves():
      possibleKingMoves = [(row-1, col-1), (row-1, col), (row-1, col+1), (row,col+1), (row+1, col+1), (row+1, col), (row+1, col-1), (row, col-1)]
      nonIncrimentalMoves(possibleKingMoves)
      
    def pawnMoves():
      if Square.inRange(row, col + 1) and squares[row][col + 1].isEmpty():

        initial = Square(row, col)
        final = Square(row, col + 1)
        
        Piece().addMove((initial, final))

      diagonalMoves = [(row + 1, col + 1), (row - 1, col + 1)]

      nonIncrimentalMoves(diagonalMoves)
  
    def knightMoves():
      lShape = [(row-2, col+1), (row-1, col+2), (row+1, col+2),(row+2, col+1),(row+2, col-1),(row+1, col-2),(row-2, col-1),(row-1, col-2)]

      nonIncrimentalMoves(lShape)          
    
    if isinstance(piece, Pawn):
      pawnMoves()
    if isinstance(piece, Knight):
      knightMoves()
    if isinstance(piece, Bishop):
      bishopMoves()
    if isinstance(piece, Rook):
      rookMoves()
    if isinstance(piece, Queen):
      queenMoves()
    if isinstance(piece, King):
      kingMoves()   
  
  def create(self):
    for row in range(rows):
      for col in range(columns):
        squares[row][col] = Square(row,col)

  def addPieces(self, colour):
    
    squares[self.initialPlayerRow][self.initialPlayerCol] = Square(self.initialPlayerRow, self.initialPlayerCol, Player())
    squares[4][1] = Square(4, 1, Pawn(colour))
    squares[1][0] = Square(1, 0, Bishop(colour))
    squares[4][3] = Square(4, 3, King(colour))
    squares[3][4] = Square(3, 4, Rook(colour))