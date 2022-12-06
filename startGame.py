import pygame
import sys

from const import *
from game import Game
from board import Board
from actions import Actions
from ai import Ai

class StartGame:

  def __init__(self):
    pygame.display.set_caption("King Hunt")
    self.game = Game()
    self.action = Actions()
    self.mainloop()
  
  def mainloop(self):
    Board()
    Board().level1('black')

    while True:
      #show board and pices
      self.game.board(screen)
      self.game.showPieces(screen)
      
      #Key button actions
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
          
        if event.type == pygame.MOUSEBUTTONDOWN:
          self.action.updateMouse(event.pos)

        if event.type == pygame.MOUSEBUTTONUP:

          #Ai moves
          Ai(screen)
      
      pygame.display.update()