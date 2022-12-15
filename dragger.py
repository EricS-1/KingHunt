import pygame

from const import *
#Created and edited by Zara
class Dragger:
  '''
    An object that moves the player's piece around by clicking and dragging to the desired position
    
    Attributes
    ----------
	  piece : void  
      the player chess piece 
  	dragging : bool
  		if the piece is being dragged or not 
  	mouseX: int
  		the position of the mouse on the x axis
    mouseY: int
      the position of the mouse on the y axis
    initialRow: int
      the inintial row position 
    initialCol: int 
    the initial column position
    
    Methods
    -------
    # note, do not list private methods in this section.  Do not include this line
    updateBlit() -> void
      updates the blitting on the screen
    updateMouse() -> tuple (int)
      updates the position of the mouse 
    saveInitial() -> tuple (int)
      saves the initial position of the mouse
    dragPiece() -> bool
      drags the player piece 
    undragPiece() -> bool
      undrags the player piece

  '''
  def __init__(self):
    '''
	Parameters
	---------
  Nothing   
    '''    
    self.piece = None
    self.dragging = False
    self.mouseX = 0
    self.mouseY = 0
    self.initialRow = 0
    self.intialCol = 0

  #blit method
  def updateBlit(self, surface):
    '''
	  Returns the updated blitted image on screen
	  Returns
	  -------
	  The updated blitted image
	  '''
    #texture
    self.piece.setTexture()
    texture = self.piece.texture
    #img
    img = pygame.image.load(texture)
    img = pygame.transform.scale(img, (80, 80))
    #rect
    imgCenter = (self.mouseX,self.mouseY)
    self.piece.texture_rect = img.get_rect(center=imgCenter)
    #update Blit
    surface.blit(img, self.piece.texture_rect)

  # other methods 
  def updateMouse(self, pos):
    '''
	  Returns the updated mouse position
	  Returns
	  -------
	  The updated mouse position
	  '''    
    self.mouseX, self.mouseY = pos # (xcor,ycor)

  def saveInitial(self, initialRow, initialCol):
    '''
	  Returns the initial position  
	  Returns
	  -------
	  The initial position of the chess piece 
	  '''        
    self.initialRow = initialRow
    self.initialCol = initialCol

  def dragPiece(self, piece):
    '''
	  Returns the initial position  
	  Returns
	  -------
	  The initial position of the chess piece 
	  '''         
    self.piece = piece
    self.dragging = True

  def undragPiece(self):
    '''
	  Returns the initial position  
	  Returns
	  -------
	  The initial position of the chess piece 
	  '''       
    self.piece = None
    self.dragging = False
