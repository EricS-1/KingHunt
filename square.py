from piece import Player

class Square:
  '''
  Square object that assigns an object for every square on the board

  Attributes 
  ----------
  row: int
    the row of the square
    
  col: int
    the column of the square
    
  piece: object
    the piece that the square is occupying, if there is no piece

  Methods
  -------
  hasPiece() -> object
    checks if the square contains a piece
    
  isEmpty() -> bool
    checks if the square dosen't contain
    
  isPlayer() -> bool
    checks if the square contains the player
    
  isEmptyOrPlayer() -> bool
    checks if the square is empty or contains a player
    
  inRange() -> bool
    checks if the row and columns of the square is within the board
  '''

  def __init__(self, row, col, piece = False):
    '''
  	Constructor to build the Square object
   
  	Parameters
  	----------
    row: int
      the row of the square
      
    col: int
      the column of the square
      
    piece: object
      the piece that the square is occupying, if there is no piece it is default to false
    
    Returns
    ----------
    nothing
  	'''
    self.row = row
    self.col = col
    self.piece = piece

  def __str__(self):
    '''
  	Returns the row and column of the square
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    the row and column of the square
  	'''
    return str(self.row) + ' ' + str(self.col)

  def __repr__(self):
    '''
  	Returns the row and column of the square
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    the row and column of the square
  	'''
    return self.__str__()

  def hasPiece(self):
    '''
  	Checks if there is a piece on the square
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    the piece on the current square
  	'''
    return self.piece

  def isEmpty(self):
    '''
  	Checks if the square is empty
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    True if the square is empty
  	'''
    return not self.hasPiece()

  def isPlayer(self):
    '''
  	Checks if the square contains a player
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    True if there is a player
    False if there is no player
  	'''
    
    if self.piece == False:
      return False
      
    elif self.piece.name != 'player':
      return False

    else:
      return True

  def isEmptyOrPlayer(self):
    '''
  	Checks if the square is empty or contains a player
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    True if there if it's empty or contains a player
    False if there is an enemy piece
  	'''
    return self.isEmpty() or self.isPlayer()

  def inRange(*args):
    '''
  	Checks if the row or column is within the board
   
  	Parameters
  	----------
    *args: int
      the rows or columns
    
    Returns
    ----------
    True if all the rows or columns are within the board
    False if the row or column rests outside the board
  	'''
    for argument in args:
      if argument < 0 or argument > 7:
        return False
    return True
  