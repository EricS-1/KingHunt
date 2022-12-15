import pygame
import random

from const import *
from square import Square
from hud import *
from piece import *


class Ai:
  '''
  AI object that executes all of the AI's functions such as the movement, attacks, and hits

  Attributes 
  ----------
  pieces: list
    list of all the pieces on the board

  moves: list
    list of the inital and possible positions of a piece on the board

  inCheck: list
    list of all the possible positions on the board 

  attacksPlayer: list
    list of moves that attack the player

  playerPos: str
    the row and column that the player is moving to

  hit: int
    the number of times the player has been hit by a piece
  
  playerX: int
    row number that player wants to move to
  
  playerY: int
    column number that player wants to move to

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
  def __init__(self, playerX, playerY):
    '''
  	Constructor to build a AI object and to execute its functions
   
  	Parameters
  	----------
    playerX: int
      row number that player wants to move to
    
    playerY: int
      column number that player wants to move to

    Returns
    ----------
    nothing
  	'''
    
    self.pieces = []
    self.moves = []
    self.inCheck = []
    self.attacksPlayer = []
    self.playerPos = str(playerX) + ' ' + str(playerY)
    self.hit = 0
    
    if not self.makeMove():
      self.makeRandomMove()

  def addMove(self, move):
    '''
  	Adds move to a list
   
  	Parameters
  	----------
    move: list
      list that contains possible moves
      
    Returns
    ----------
    nothing
  	'''
    
    self.moves.append(move)
  
  def possibleMoves(self, piece, row, col):
    '''
  	Generates all the possible moves of the piece
   
  	Parameters
  	----------
    piece: class
      piece object that holds all the information about the piece
      
    row: int
      row number that the piece currently on
      
    col: list
      column number that the piece currently on

    Returns
    ----------
    nothing
  	'''

    def straightMoves(incriments):
      '''
  	  Generates all the possible moves for when the piece moves in horizontal, vertical or diagonal lines
     
    	Parameters
    	----------
      incriments: list
        list that contains tuples with the pieces possible row and column movement increments
    	
      Returns
      ----------
      nothing
      '''

      for incri in incriments:
        rowIncri, colIncri = incri
        possibleMoveRow = row + rowIncri
        possibleMoveCol = col + colIncri

        while Square.inRange(possibleMoveRow, possibleMoveCol):
          
          initial = Square(row, col)
          final = Square(possibleMoveRow, possibleMoveCol)
          
          if squares[possibleMoveRow][possibleMoveCol].isEmptyOrPlayer():
            self.addMove((initial, final))

          else:
            break

          possibleMoveRow = possibleMoveRow + rowIncri
          possibleMoveCol = possibleMoveCol + colIncri

    def nonIncrimentalMoves(moveList):
      '''
  	  Generates all the possible moves for when the piece can only move one square at a time
     
    	Parameters
    	----------
      moveList: list
        list that contains tuples with the pieces possible row and column movement increments

      Returns
      ----------
      nothing
    	'''
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
      '''
  	  Generates all possible rook moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
    	'''
      straightMoves([(-1, 0), (1, 0), (0, 1), (0, -1)])

    def bishopMoves():
      '''
  	  Generates all possible bishop moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
      '''
      straightMoves([(-1, 1), (-1, -1), (1, 1), (1, -1)])

    def queenMoves():
      '''
  	  Generates all possible queen moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
    	'''
      rookMoves()
      bishopMoves()

    def kingMoves():
      '''
  	  Generates all possible king moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
    	'''
      possibleKingMoves = [(-1, -1), (-1, 0),
                           (-1, 1), (0, 1),
                           (1, 1), (1, 0),
                           (1, -1), (0, -1)]
      nonIncrimentalMoves(possibleKingMoves)

    def pawnMoves():
      '''
  	  Generates all possible pawn moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
    	'''
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
      '''
  	  Generates all possible knight moves

      Parameters
    	----------
      nothing

      Returns
      ----------
      nothing
    	'''
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

  def makeMove(self):
    '''
  	Searches for a possible move that attacks the player

    Parameters
    ----------
    nothing

    Returns
    ----------
    True if the AI finds a move that attacks the player
    False if the AI cannot find a move that attacks the player
  	'''
    
    moved = []

    #Looks at every square
    for row in range(rows):
      for col in range(columns):
        square = squares[row][col]
        

        #Make sure the piece that the AI is moving isn't the player
        if square.hasPiece() and square.piece.name != 'player':
          
          #Append all possible moves for that piece
          self.possibleMoves(square.piece, square.row, square.col)
          
          for move in self.moves:
            final = str(move[-1])
            self.inCheck.append(final)

          if not self.playerPos in self.inCheck:
          
            moved = self.moves.copy()
  
            #Append all possible moves after making one of the possible moves for that piece
            for move1 in range(len(moved)):
              self.moves.clear()
          
              self.possibleMoves(square.piece, moved[move1][1].row, moved[move1][1].col)
  
              
              #Check all possible moves for one that attacks the player
              for move2 in range(len(self.moves)):
                afterMovedRow = self.moves[move2][1].row
                afterMovedCol = self.moves[move2][1].col
            
                #Update movement on screen if move found that attacks player
                if squares[afterMovedRow][afterMovedCol].isPlayer():

                  attacks = moved[move1]
                  piece = square.piece
                  move = (piece, attacks)
                  self.attacksPlayer.append(move)
  
              self.moves.clear()   
              self.inCheck.clear()
          
          
          else:
            self.hit += 1
            translateX = 9/50 * width + squareSize/2
            translateY = 2/25 * height + squareSize/2

            playerXandY = self.playerPos.split()
            playerXandY[0] = int(playerXandY[0]) * squareSize + translateX  
            playerXandY[1] = int(playerXandY[1]) * squareSize + translateY
            
            pygame.draw.line(screen, (255,0,0), (row * squareSize + translateX, col * squareSize + translateY), (playerXandY))

            self.moves.clear()
            self.inCheck.clear()

    if len(self.attacksPlayer) > 0:
      randomAttack = random.randint(0,len(self.attacksPlayer) - 1)
      
      initialRow = self.attacksPlayer[randomAttack][1][0].row
      initlalCol = self.attacksPlayer[randomAttack][1][0].col
      movedRow = self.attacksPlayer[randomAttack][1][1].row
      movedCol = self.attacksPlayer[randomAttack][1][1].col

      texture = 'pieces/white' + self.attacksPlayer[randomAttack][0].name + '.png'

      img = pygame.image.load(texture)
      img = pygame.transform.scale(img, (squareSize, squareSize))

      screen.blit(img, (squareSize * (movedRow) + 90, squareSize*(movedCol) + 40))
      
      squares[movedRow][movedCol] = Square(movedRow, movedCol,self.attacksPlayer[randomAttack][0])

      squares[initialRow][initlalCol] = Square(initialRow, initlalCol, False)

      return True
    
    return False

  def makeRandomMove(self):
    '''
  	Make a random possible move
   
    Parameters
    ----------
    nothing

    Returns
    ----------
    nothing
  	'''
    
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
        return 1
        
      randomPiece = random.choice(self.pieces)
      self.possibleMoves(randomPiece.piece, randomPiece.row,randomPiece.col)
        
    randomMove = random.randint(0, len(self.moves) - 1)

    #updates movement
    initialRow = self.moves[randomMove][0].row
    initlalCol = self.moves[randomMove][0].col
    movedRow = self.moves[randomMove][1].row
    movedCol = self.moves[randomMove][1].col

    texture = 'pieces/white' + randomPiece.piece.name + '.png'

    img = pygame.image.load(texture)
    img = pygame.transform.scale(img, (squareSize, squareSize))

    screen.blit(img,(squareSize * (movedRow) + 90, squareSize * (movedCol) + 40))

    squares[initialRow][initlalCol] = Square(initialRow, initlalCol)
    
    squares[movedRow][movedCol] = Square(movedRow, movedCol, randomPiece.piece)
