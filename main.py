import pygame
import sys

from button import Button
from startGame import StartGame
from const import *


pygame.init()

def starCutscene():
  '''code'''
  StartGame()
def get_font(size):
  return pygame.font.Font("images/font.ttf", size)

def newGame():

  pygame.display.set_caption("New Game")

  while True:

    newPosition = pygame.mouse.get_pos()

    screen.fill("green")

    newText = get_font(45).render("Your story begins now.", True, "White")
    newRect = newText.get_rect(center=(960,460))
    screen.blit(newText,newRect)

    newBack = Button(image= None, pos=(960,660), textInput= "Back", font= get_font(75), baseColor= "white", hoveringColor= "black")

    newBack.changeColor(newPosition)
    newBack.update(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if newBack.checkForInput(newPosition):
          mainMenu()

    pygame.display.update()
    
def options():
  pygame.display.set_caption("Options")

  while True:
    optionsPosition = pygame.mouse.get_pos()

    screen.fill("white")

    optionsText = get_font(45).render("Options Menu", True, "Black")
    optionsRect = optionsText.get_rect(center=(960,260))
    screen.blit(optionsText, optionsRect)

    optionsGameplay = Button(image=None, pos=(960,360), textInput= "GAMEPLAY", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsVideo = Button(image=None, pos=(960,460), textInput= "VIDEO", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsAudio = Button(image=None, pos=(960,560), textInput= "AUDIO", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsControls = Button(image=None, pos=(960,660), textInput= "CONTROLS", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsBack = Button(image=None, pos=(960, 760), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")

    for button in [optionsGameplay, optionsVideo, optionsAudio, optionsControls, optionsBack]:
      button.changeColor(optionsPosition)
      button.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if optionsGameplay.checkForInput(optionsPosition):
          gameplay()
        if optionsVideo.checkForInput(optionsPosition):
          video()
        if optionsAudio.checkForInput(optionsPosition):
          audio()
        if optionsControls.checkForInput(optionsPosition):
          controls()
        if optionsBack.checkForInput(optionsPosition):
          mainMenu()

    pygame.display.update()

def gameplay():
  pygame.display.set_caption("Gameplay Options")

  while True:
    gameplayPosition = pygame.mouse.get_pos()

    screen.fill("white")

    gameplayText = get_font(45).render("Gameplay Options", True, "Black")
    gameplayRect = gameplayText.get_rect(center=(960,260))
    screen.blit(gameplayText, gameplayRect)
    tutorialText = get_font(34).render("Display Tutorial Messages", True, "Black")
    tutorialRect = tutorialText.get_rect(center=(480, 400))
    screen.blit(tutorialText, tutorialRect)
    brightText = get_font(41).render("Brightness", True, "Black")
    brightRect = brightText.get_rect(center=(261,500))
    screen.blit(brightText, brightRect)
    fpsText = get_font(45).render("Display FPS", True, "Black")
    fpsRect = fpsText.get_rect(center=(304,600))
    screen.blit(fpsText, fpsRect)
    
    gameplayBack = Button(image=None, pos=(960, 750), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")

    gameplayBack.changeColor(gameplayPosition)
    gameplayBack.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if gameplayBack.checkForInput(gameplayPosition):
          options()

    pygame.display.update()

def video(): 
  pygame.display.set_caption("Video Options")

  while True:
    videoPosition = pygame.mouse.get_pos()

    screen.fill("white")

    videoText = get_font(45).render("Video Options", True, "Black")
    videoRect = videoText.get_rect(center=(960,260))
    screen.blit(videoText, videoRect)
    resText = get_font(45).render("Resolution", True, "Black")
    resRect = resText.get_rect(center=(380,400))
    screen.blit(resText, resRect)
    chosenText = get_font(35).render(str(screenWIDTH) + "x" + str(screenHEIGHT), True, "Black")
    chosenRect = chosenText.get_rect(center=(960,400))
    screen.blit(chosenText, chosenRect)
    
    videoBack = Button(image=None, pos=(960, 520), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")
    resLeft = Button(image=None, pos=(720, 400), textInput= "<-", font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    resRight = Button(image=None, pos=(1200, 400), textInput= "->", font= get_font(55), baseColor= "Black", hoveringColor= "Green")

    for button in [videoBack, resLeft, resRight]:
      button.changeColor(videoPosition)
      button.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if videoBack.checkForInput(videoPosition):
          options()
          
    pygame.display.update()

def audio():
  pygame.display.set_caption("Audio Options")

  while True:
    audioPosition = pygame.mouse.get_pos()

    screen.fill("white")

    audioText = get_font(45).render("Audio Options", True, "Black")
    audioRect = audioText.get_rect(center=(960,260))
    screen.blit(audioText, audioRect)
    masterText = get_font(45).render("Master Volume", True, "Black")
    masterRect = masterText.get_rect(center=(380,360))
    screen.blit(masterText, masterRect)
    musicText = get_font(45).render("Music Volume", True, "Black")
    musicRect = musicText.get_rect(center=(380,460))
    screen.blit(musicText, musicRect)
    sfxText = get_font(35).render("Sound Effects Volume", True, "Black")
    sfxRect = sfxText.get_rect(center=(380,560))
    screen.blit(sfxText, sfxRect)
    

    audioBack = Button(image=None, pos=(960, 460), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")

    audioBack.changeColor(audioPosition)
    audioBack.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if audioBack.checkForInput(audioPosition):
          options()

    pygame.display.update()

def controls():
  pygame.display.set_caption("Controls Options")
  
  while True:
      controlsPosition = pygame.mouse.get_pos()
  
      screen.fill("white")
  
      controlsText = get_font(45).render("Controls Options", True, "Black")
      controlsRect = controlsText.get_rect(center=(960,260))
      screen.blit(controlsText, controlsRect)
  
      controlsBack = Button(image=None, pos=(960, 460), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")
  
      controlsBack.changeColor(controlsPosition)
      controlsBack.update(screen)
        
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          if controlsBack.checkForInput(controlsPosition):
            options()
  
      pygame.display.update()
    
def stats():
  pygame.display.set_caption("Game Statistics")
  
  while True:
    statsPosition = pygame.mouse.get_pos()

    screen.fill("#32CD32")

    titleText = get_font(42).render("Game Statistics", True, "Black")
    titleRect = titleText.get_rect(center=(380,150))
    screen.blit(titleText, titleRect)
    timeText = get_font(35).render("Total Play Time = " + str(playTime), True, "Black")
    timeRect = timeText.get_rect(center=(380,250))
    screen.blit(timeText, timeRect)
    enemyText = get_font(35).render("Enemies Defeated = " + str(enemiesDefeated), True, "Black")
    enemyRect = enemyText.get_rect(center=(380,350))
    screen.blit(enemyText, enemyRect)
    defeatedText = get_font(35).render("Times Defeated = " + str(timesDefeated), True, "Black")
    defeatedRect = defeatedText.get_rect(center=(380,450))
    screen.blit(defeatedText, defeatedRect)
    completionText = get_font(35).render("Completion % = " + str(completionPercent), True, "Black")
    completionRect = completionText.get_rect(center=(380,550))
    screen.blit(completionText, completionRect)

    statsBack = Button(image=None, pos=(380, 700), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "White")

    statsBack.changeColor(statsPosition)
    statsBack.update(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if statsBack.checkForInput(statsPosition):
          mainMenu()

    pygame.display.update()

def exit():
  pygame.display.set_caption("Exit")

  while True:
    exitPosition = pygame.mouse.get_pos()

    screen.fill("Black")

    exitText = get_font(42).render("Are you sure you want to quit King Hunt?", True, "White")
    exitRect = exitText.get_rect(center=(960,360))
    screen.blit(exitText, exitRect)

    exitYes = Button(image=None, pos=(480, 700), textInput= "Yes", font= get_font(45), baseColor= "White", hoveringColor= "Green")
    exitNo = Button(image=None, pos=(1440, 700), textInput= "No", font= get_font(45), baseColor= "White", hoveringColor= "Green")

    for button in [exitYes, exitNo]:
      button.changeColor(exitPosition)
      button.update(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if exitNo.checkForInput(exitPosition):
          mainMenu()
        if exitYes.checkForInput(exitPosition):
          pygame.quit()
          sys.exit()

    pygame.display.update()

def mainMenu():
  pygame.display.set_caption("Main Menu")

  while True:
    screen.blit(background, (0,0))
    
    menuPosition = pygame.mouse.get_pos()

    mainText = get_font(42).render("King Hunt", True, "white")
    mainRect = mainText.get_rect(center=(380,150))

    newButton = Button(image=None, pos=(380,300), textInput= "New Game", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")
    continueButton = Button(image=None, pos=(390,400), textInput= "Continue ", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")
    loadButton = Button(image=None, pos=(380,500), textInput= "Load Game", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")
    optionsButton = Button(image=None, pos=(380,600), textInput= "Options", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")
    statsButton = Button(image=None, pos=(380,700), textInput= "Stats", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")
    exitButton = Button(image=None, pos=(380,800), textInput= "Exit", font= get_font(35), baseColor= "#d7fcd4", hoveringColor= "White")

    screen.blit(mainText,mainRect)

    for button in [newButton, continueButton, loadButton, optionsButton, statsButton, exitButton]:
      button.changeColor(menuPosition)
      button.update(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if newButton.checkForInput(menuPosition):
          newGame()
        if optionsButton.checkForInput(menuPosition):
          options()
        if statsButton.checkForInput(menuPosition):
          stats()
        if exitButton.checkForInput(menuPosition):
          exit()

    pygame.display.update()

StartGame()