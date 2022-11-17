class Square:

  def __init__(self, row, col, piece=False):
    self.row = row
    self.col = col
    self.piece = piece

  def hasPiece(self):
    return self.piece

  def isEmpty(self):
    return not self.hasPiece()
  