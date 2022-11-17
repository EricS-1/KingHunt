import pygame
import sys

from const import *
from game import Game
from board import Board
from piece import Player

class Main:

  def __init__(self):
    pygame.init()
    self.initialRow = Board().initialPlayerRow
    self.initialCol = Board().initialPlayerCol
    self.window = pygame.display.set_mode((width,height))
    pygame.display.set_caption("King Hunt")
    self.game = Game()
    
    
  def mainloop(self):
    self.game.board(self.window)
    self.game.showPieces(self.window)
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_UP:
            if self.initialCol - 1 >= 0 and Board().squares[self.initialRow][self.initialCol - 1].isEmpty():
              Player().updateMovement(self.window, self.initialRow, self.initialCol, -1,0)
              self.initialCol -= 1
              
          if event.key == pygame.K_RIGHT:
            if self.initialRow + 1 <= 7 and Board().squares[self.initialRow + 1][self.initialCol].isEmpty():
              Player().updateMovement(self.window, self.initialRow, self.initialCol, 0,1)
              self.initialRow += 1
      
          if event.key == pygame.K_DOWN:
            if self.initialCol + 1 <= 7 and Board().squares[self.initialRow][self.initialCol + 1].isEmpty():
              Player().updateMovement(self.window, self.initialRow, self.initialCol, 1,0)
              self.initialCol += 1
      
          if event.key == pygame.K_LEFT:
            if self.initialRow - 1 >= 0 and Board().squares[self.initialRow - 1][self.initialCol].isEmpty():
              Player().updateMovement(self.window, self.initialRow, self.initialCol, 0,-1)
              self.initialRow -= 1
      
      pygame.display.update()

main = Main()
main.mainloop()