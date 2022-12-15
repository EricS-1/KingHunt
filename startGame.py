import pygame
import sys
import random

from const import *
from game import Game
from board import Board
from hud import *
from ai import Ai
from square import Square
from piece import *

class StartGame:
  '''
  StartGame object that starts the game, takes in user inputs, and loads game screen

  Attributes 
  ----------
  clock: object
    the pygame clock that keeps track of time in the game
    
  currentTime: int
    the elapsed time on the game
    
  seconds: int
    the time it takes for a second to happen

  minutes: int
    the time it takes for a minute to happen

  textFont: object
    the font of the game

  moves: list
    list of all the possible player moves

  check: bool
    to check if the player is attempting to move the player piece to avoid creating piece duplicates

  levels: list
    list of all the levels in the game

  game: object
    the game class

  Methods
  -------
  possiblePlayerMoves() -> returns nothing
    adds all the possible moves for the player to the moves list
    
  playerTime() -> list
    updates the elapsed time on the screen
    
  mainloop() -> returns nothing
    executes the main functions of the game and takes player inputs
  '''
  def __init__(self):
    '''
  	Constructor to build the startGame object
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    pygame.display.set_caption("King Hunt")
    self.clock = pygame.time.Clock()
    self.currentTime = 0
    self.seconds = 0
    self.minutes = 0
    self.textFont = pygame.font.SysFont('Times New Roman', 20)
    self.moves = []
    self.check = False

    self.levels = [Board().level1, Board().level2, Board().level3, Board().level4]
    self.game = Game()
    self.mainloop()

  def possiblePlayerMoves(self, row, col):
    '''
  	Generates all the possible moves of the player
   
  	Parameters
  	----------
      
    row: int
      row number that the player currently on
      
    col: list
      column number that the player currently on

    Returns
    ----------
    nothing
  	'''

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
            final = (possibleMoveRow, possibleMoveCol)
            self.moves.append(final)
            
    def playerMoves():
      '''
  	  Generates all possible player moves

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

    playerMoves()

  def playerTime(self):
    '''
    Updates and displays the elapsed time

    Parameters
    ----------
    nothing

    Returns
    ----------
    a list contaiting the minutes and seconds in a digital clock format
    '''
    clockTime = ['0', str(self.minutes), ':', '0', str(self.seconds)]
    second = pygame.time.get_ticks()
    
    if second - self.currentTime >= 1000:
      self.seconds += 1
      self.currentTime = second
      
      if self.seconds == 60:
        self.seconds = 0
        clockTime.insert(3, '0')
        self.minutes += 1

    if self.seconds >= 10:
      clockTime.pop(3)

    if self.minutes >= 10:
      clockTime.pop(0)
    
    return clockTime
  
  
  def mainloop(self):
    '''
    Executes the game's mechanics and graphics

    Parameters
    ----------
    nothing

    Returns
    ----------
    nothing
    
    '''
    for levels in range(len(self.levels)):
      Board()
      currentLevel = random.choice(self.levels)
      self.levels.remove(currentLevel)
      currentLevel('white')

      health = PlayerHealth(2)
      
      dragger = self.game.dragger
      
      while True:
        #show board and pices
        self.game.board()
        self.game.showPieces()
        Hud()
        health.display()

        #load time Icon and text
        playerTimeIcon = pygame.image.load('gameLayout/hourglass.png')
        playerTimeIcon = pygame.transform.scale(playerTimeIcon, (35/1.5,40/1.5))
        time = self.textFont.render(''.join(self.playerTime()), 1, (0,0,0))
        
        screen.blit(time, (26, 2/25 * height + 73))
        screen.blit(playerTimeIcon, (0, 2/25 * height + 71 + 1/3))
        
        if dragger.dragging:
          dragger.updateBlit(screen)

        #Key button actions
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
          #click  
          if event.type == pygame.MOUSEBUTTONDOWN:
            dragger.updateMouse(event.pos)

            clickedRow = dragger.mouseX // squareSize - 2
            clickedCol = dragger.mouseY // squareSize - 1
            if Square.inRange(clickedRow, clickedCol):
              #if clicked square has piece       
              if squares[clickedRow][clickedCol].isPlayer():
                  piece = squares[clickedRow][clickedCol].piece
                  dragger.saveInitial(clickedRow, clickedCol)
                  dragger.dragPiece(piece)
                  self.check = True
              
          #mouse motion
          elif event.type == pygame.MOUSEMOTION:
            if dragger.dragging:
              dragger.updateMouse(event.pos)
              Game().board()
              Game().showPieces()
              Hud()
              health.display()
              screen.blit(time, (26, 2/25 * height + 73))
              screen.blit(playerTimeIcon, (0, 2/25 * height + 71 + 1/3))
              
              dragger.updateBlit(screen)
              
          #click release
          elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.check:
            
            dragger.updateMouse(event.pos)

            releasedRow = dragger.mouseX // squareSize - 2
            releasedCol = dragger.mouseY // squareSize - 1
            checkColandRow = (releasedRow, releasedCol)

            self.possiblePlayerMoves(dragger.initialRow, dragger.initialCol)

            if checkColandRow in self.moves:         
              squares[dragger.initialRow][dragger.initialCol] = Square(dragger.initialRow, dragger.initialCol, False)
              squares[releasedRow][releasedCol] = Square(releasedRow, releasedCol, Player())
              
              dragger.undragPiece()
              
              #Ai moves
              health.hit(Ai(releasedRow, releasedCol).hit)

            self.check = False
            
          else:
            dragger.undragPiece()

        
        if health.health == 0:
          break
        
        pygame.display.update()
        self.clock.tick(60)