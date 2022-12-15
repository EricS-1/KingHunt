import pygame

#list of all constants and global variables used for the game
width = 500
height = 500
rows = 8
columns = 8
squareSize = int((width//rows) - 50/4)
backgroundColor = (185,165,147)
squares = [[0,0,0,0,0,0,0,0] for col in range(columns)]
screen = pygame.display.set_mode((width,height))
background = pygame.image.load("images/Background.png")

playTime = 0
enemiesDefeated = 0
timesDefeated = 0
completionPercent = 0