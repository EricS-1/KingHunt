from const import *
import pygame

class Hud:
  '''
  Hud object that loads the icon, kills, and weapon 

  Attributes 
  ----------
  playerSize: tuple
    the size of the player icon

  textFont: object
    the font used for the hud
  
  Methods
  -------
  playerIcon() -> returns none
    loads the player icon
    
  playerKills() -> returns none
    loads the kill icon and the number of kills

  playerWeapon() -> returns none
    loads the weapon and the amount of ammo
  '''
  def __init__(self):
    '''
  	Constructor to build the Hud object and executes all of its functions
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    
    self.playerSize = (80,80)
    self.textFont = pygame.font.Font('gameLayout/arcadeclassic.ttf', 28)
    self.playerIcon()
    self.playerKills()
    self.playerWeapon()


  def playerIcon(self):
    '''
  	Loads the player icon onto the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''

    playerFace = pygame.image.load('gameLayout/player.png')
    playerFace = pygame.transform.scale(playerFace, self.playerSize)
    playerBackground = pygame.Rect(2, 2/25 * height + 120, 86, 86)

    pygame.draw.rect(screen, (158,124,108), playerBackground)
    screen.blit(playerFace, (5, 2/25 * height + 120))

  def playerKills(self):
    '''
  	Loads the kill icon and number of kills onto the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    
    killIcon = pygame.image.load('gameLayout/kills.png')
    killIcon = pygame.transform.scale(killIcon, (25,25))
    
    killNumber = ['0','0',str(enemiesDefeated)]

    if enemiesDefeated >= 10:
      killNumber.pop(0)

    if enemiesDefeated >= 100:
      killNumber.pop(0)

    killed = self.textFont.render(''.join(killNumber), 1, (0,0,0))
    
    screen.blit(killIcon, (5, 2/25 * height + 290))
    screen.blit(killed, (36, 2/25 * height + 290))

  def playerWeapon(self):
    '''
  	Loads the weapon icon and ammount of ammo onto the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    
    weaponIcon = pygame.image.load('gameLayout/weapon.png')
    weaponIcon = pygame.transform.scale(weaponIcon, (50,50))
    
    firstBullet = pygame.image.load('gameLayout/firstBullet.png')
    secondBullet = pygame.image.load('gameLayout/secondBullet.png')
    thirdBullet = pygame.image.load('gameLayout/thirdBullet.png')
    firstBullet = pygame.transform.scale(firstBullet, (50,50))
    secondBullet = pygame.transform.scale(secondBullet, (50,50))
    thirdBullet = pygame.transform.scale(thirdBullet, (42,42))

    for bullets in range(9):
      
      if bullets <= 2:
        translate = (bullets + 1) * 30 + 25
        screen.blit(firstBullet, (9/50 * width + translate, 2/25 * height + 402))
      elif bullets <= 5:
        translate = (bullets - 3) * 35 + 148
        screen.blit(secondBullet, (9/50 * width + translate, 2/25 * height + 402))

      else:
        translate = (bullets - 5) * 40 + 220
        screen.blit(thirdBullet, (9/50 * width + translate, 2/25 * height + 405))
        
    screen.blit(weaponIcon, (9/50 * width + 15, 2/25 * height + 402))

class PlayerHealth:
  '''
  PlayerHealth object that loads and updates the player's health

  Attributes 
  ----------
  health: int
    current health of the player
  
  Methods
  -------
  hit(hits) -> int
    subtracts health from the player
    
  display() -> returns none
    displays the player's health onto the screen
  '''
  def __init__(self, health):
    '''
  	Constructor to build the Hud object and executes all of its functions
   
  	Parameters
  	----------
    health: int
      current health of the player
    
    Returns
    ----------
    nothing
  	'''
    self.health = health

  def hit(self, hits):
    '''
  	Subtract the player's health by the amount of times the player was hit
   
  	Parameters
  	----------
    hits: int
      amount to subtract from player health
    
    Returns
    ----------
    resulting health of the player
  	'''
    self.health -= hits
    return self.health
    
  def display(self):
    '''
  	Display the player's health on the screen
   
  	Parameters
  	----------
    nothing
    
    Returns
    ----------
    nothing
  	'''
    playerHearts = pygame.image.load('gameLayout/heart.png')
    playerHearts = pygame.transform.scale(playerHearts, (37,37))
    playerEmptyHearts = pygame.image.load('gameLayout/emptyheart.png')
    playerEmptyHearts = pygame.transform.scale(playerEmptyHearts, (37,37))
    
    if self.health == 2:
      screen.blit(playerHearts, (5, 2/25 * height + 226))
      screen.blit(playerHearts, (47, 2/25 * height + 226))

    else:
      screen.blit(playerHearts, (5, 2/25 * height + 226))
      screen.blit(playerEmptyHearts, (47, 2/25 * height + 226))