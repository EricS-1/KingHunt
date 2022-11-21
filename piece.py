import os
import pygame
from const import *

class Piece:

  def __init__(self, name, color, healthPoints, value, texture = None):
    self.name = name
    self.color = color
    self.healthPoints = healthPoints
    self.value = value
    self.moves = []
    self.setTexture()

  def setTexture(self):
    self.texture = os.path.join("pieces", str(self.color) + str(self.name) + '.png')

  def addMove(self, move):
    self.moves.append(move)

class Pawn(Piece):
  def __init__(self, color):
    super().__init__('pawn', color, 1, 1)

class Knight(Piece):
  def __init__(self, color):
    super().__init__('knight', color, 2, 3)

class Bishop(Piece):
  def __init__(self, color):
    super().__init__('bishop', color, 2, 3)

class Rook(Piece):
  def __init__(self, color):
    super().__init__('rook', color, 3, 5)
    
class Queen(Piece):
  def __init__(self, color):
    super().__init__('queen', color, 3, 9)
    
class King(Piece):
  def __init__(self, color):
    super().__init__('king', color, 4, 1000)

class Player(Piece):
  def __init__(self):
    super().__init__('player', '', 3, None)