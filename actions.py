import pygame

from const import *
from square import Square
from piece import Player

class Actions:
  def __init__(self):
    self.mouseX = 0
    self.mouseY = 0

  def updateMouse(self, pos):
    self.mouseX, self.mouseY = pos
    