from piece import Player

class Square:

  def __init__(self, row, col, piece = False):
    self.row = row
    self.col = col
    self.piece = piece

  def __str__(self):
    return str(self.row) + ' ' + str(self.col) + ' ' + str(self.piece)

  def hasPiece(self):
    return self.piece

  def isEmpty(self):
    return not self.hasPiece()

  def isPlayer(self):
    if self.piece == Player():
      return True

  def isEmptyOrPlayer(self):
    self.isEmpty()
    self.isPlayer()

  def inRange(*args):
    for argument in args:
      if argument < 0 or argument > 7:
        return False

    return True
  