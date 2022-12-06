import pygame
import random
from const import *
from square import Square
from piece import *


class Ai:

  def __init__(self, surface):
    self.pieces = []
    self.moves = []
    self.makeMove(screen)
    #if not self.makeMove(screen):
      #self.makeRandomMove(screen)

  def addMove(self, move):
    self.moves.append(move)

  def possibleMoves(self, piece, row, col):

    def straightMoves(incriments):

      for incri in incriments:
        rowIncri, colIncri = incri
        possibleMoveRow = row + rowIncri
        possibleMoveCol = col + colIncri

        while Square.inRange(possibleMoveRow, possibleMoveCol):
          
          initial = Square(row, col)
          final = Square(possibleMoveRow, possibleMoveCol)
          
          if squares[possibleMoveRow][possibleMoveCol].isEmpty():
            self.addMove((initial, final))

          else:
            break

          possibleMoveRow = possibleMoveRow + rowIncri
          possibleMoveCol = possibleMoveCol + colIncri

    def nonIncrimentalMoves(moveList):
      for possibleMove in moveList:
        moveRow, moveCol = possibleMove
        possibleMoveRow = row + moveRow
        possibleMoveCol = col + moveCol
        
        if Square.inRange(possibleMoveRow, possibleMoveCol):
  
          if squares[possibleMoveRow][possibleMoveCol].isEmpty():

            initial = Square(row, col)
            final = Square(possibleMoveRow, possibleMoveCol)

            self.addMove((initial, final))

    def rookMoves():
      straightMoves([(-1, 0), (1, 0), (0, 1), (0, -1)])

    def bishopMoves():
      straightMoves([(-1, 1), (-1, -1), (1, 1), (1, -1)])

    def queenMoves():
      rookMoves()
      bishopMoves()

    def kingMoves():
      possibleKingMoves = [(-1, -1), (-1, 0),
                           (-1, 1), (0, 1),
                           (1, 1), (1, 0),
                           (1, -1), (0, -1)]
      nonIncrimentalMoves(possibleKingMoves)

    def pawnMoves():
      if Square.inRange(row, col + 1) and squares[row][col + 1].isEmpty():

        initial = Square(row, col)
        final = Square(row, col + 1)

        self.addMove((initial, final))

      diagonalMoves = [(1, 1), (-1, 1)]

      for possibleMove in diagonalMoves:
        moveRow, moveCol = possibleMove
        possibleMoveRow = row + moveRow
        possibleMoveCol = col + moveCol
        
        if Square.inRange(possibleMoveRow, possibleMoveCol):
  
          if squares[possibleMoveRow][possibleMoveCol].isPlayer():

            initial = Square(row, col)
            final = Square(possibleMoveRow, possibleMoveCol)

            self.addMove((initial, final))

    def knightMoves():
      lShape = [(row - 2, col + 1), (row - 1, col + 2), (row + 1, col + 2),(row + 2, col + 1), (row + 2, col - 1), (row + 1, col - 2),(row - 2, col - 1), (row - 1, col - 2)]

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

  def makeMove(self, surface):
    moved = []

    #Looks at every square
    for row in range(rows):
      for col in range(columns):
        square = squares[row][col]

        #Make sure the piece that the AI is moving isn't the player
        if square.hasPiece() and square.piece.name != 'player':
          #Append all possible moves for that piece
          self.possibleMoves(square.piece, square.row, square.col)
          moved = self.moves.copy()

          #Append all possible moves after making one of the possible moves for that piece
          for move1 in range(len(moved)-1):
            row1 = moved[move1][1].row
            col1 = moved[move1][1].col
            self.moves.clear()
            
            self.possibleMoves(square.piece, row1, col1)

            #Check all possible moves for one that attacks the player
            for move2 in range(len(self.moves)-1):
              afterMovedRow = self.moves[move2][1].row
              afterMovedCol = self.moves[move2][1].col
              
              #Update movement on screen if move found attacks player
              if squares[afterMovedRow][afterMovedCol].isPlayer():

                initialRow = moved[move1][0].row
                initlalCol = moved[move1][0].col
                movedRow = moved[move1][1].row
                movedCol = moved[move1][1].col

                texture = 'pieces/black' + square.piece.name + '.png'

                img = pygame.image.load(texture)
                img = pygame.transform.scale(img, (squareSize, squareSize))

                surface.blit(img, (squareSize * (movedRow) + 90, squareSize*(movedCol) + 40))
                
                squares[movedRow][movedCol] = Square(movedRow, movedCol,square.piece)

                squares[initialRow][initlalCol] = Square(initialRow, initlalCol, False)

                return True
            
            self.moves.clear()
    return False

  def makeRandomMove(self, surface):
    for row in range(rows):
      for col in range(columns):
        square = squares[row][col]
        if square.hasPiece() and square.piece.name != 'player':
          self.pieces.append(square)

    randomPiece = self.pieces[random.randint(0, len(self.pieces) - 1)]
    self.possibleMoves(randomPiece.piece, randomPiece.row,randomPiece.col)
  
    while len(self.moves) <= 0:
      if len(self.moves) <= 0:
        self.pieces.remove(randomPiece)

      if len(self.pieces) == 0:
        print('win')
        
      randomPiece = random.choice(self.pieces)
      self.possibleMoves(randomPiece.piece, randomPiece.row,randomPiece.col)
        
    randomMove = random.randint(0, len(self.moves) - 1)

    #updates movement
    initialRow = self.moves[randomMove][0].row
    initlalCol = self.moves[randomMove][0].col
    movedRow = self.moves[randomMove][1].row
    movedCol = self.moves[randomMove][1].col

    texture = 'pieces/black' + randomPiece.piece.name + '.png'

    img = pygame.image.load(texture)
    img = pygame.transform.scale(img, (squareSize, squareSize))

    surface.blit(img,(squareSize * (movedRow) + 90, squareSize * (movedCol) + 40))

    squares[initialRow][initlalCol] = Square(initialRow, initlalCol)
    
    squares[movedRow][movedCol] = Square(movedRow, movedCol, randomPiece.piece)
