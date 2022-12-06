'''
if dragger.dragging:
  dragger.updateBlit(screen)

if piece is not self.dragger.piece:
  #all pieces except draggr piece
  piece.setTexture(size=80)
  img = pygame.image.load(piece.texture)
  imgCenter = col * SQSIZE + SQSIZE // 2, row + SQSIZE +SQSIZE //2
  self.piece.textureRect = img.getRect(center=imgCenter)
  surface.blit(img, self.piece.textureRect)  
  
#click
if event.type == pygame.MOUSEBUTTONDOWN:
  dragger.updateMouse(event.pos)
  
  clickedRow = dragger.mouseY // SQSIZE
  clickedCol = dragger.mouseX // SQSIZE

  #if clicked square has a piece already
  if board.squares[clickedRow][clickedCol].hasPiece():
    piece = board.squares[clickedRow][clickedCol].piece
    dragger.saveInitial(event.pos)
    dragger.dragPiece(piece)

    
#mouse motion
elif evet.type ==pygame.MOUSEMOTION:
  if dragger.dragging:
    dragger.updateMouse(event.pos)
    game.showBg(screen)
    game.showPieces(screen)
    dragger.updateBlit(screen)

  
#click release
elif event.type ==pygame.MOUSEBUTTONUP:
  dragger.undragPiece()

#quit application
elif event.type == pygame.QUIT:
  pygame.quit()
  sys.exit()


import pygame
from const import *

class Dragger:
  def __innit__(self):
    self.piece = None
    self.dragging = False
    self.mouseX = 0
    self.mouseY = 0
    self.initialRow = 0
    self.intialCol = 0

  #blit method

    
  def updateBlit(self, surface):
    #texture
    self.piece.setTexture(size=128)
    texture = self.piece.texture
    #img
    img = pygame.image.load(texture)
    #rect
    imgCenter = (self.mouseX,self.mouseY)
    self.piece.textureRect = img.getRect(center=imgCenter)
    #update Blit
    surface.blit(img, self.piece.textureRect)

  # other methods
    
  def updateMouse(self, pos):
    self.mouseX, self.mouseY = pos # (xcor,ycor)

  def saveInitial(self, pos):
    self.initialRow = pos[1] //SQSIZE
    self.initialCol = pos[0] //SQSIZE

  def dragPiece(self, piece):
    self.piece = piece
    self.dragging = True

  def undragPiece(self):
    self.piece = None
    self.dragging = False
'''