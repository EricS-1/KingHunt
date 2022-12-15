import pygame
import sys
from button import Button
import cv2

pygame.init()

# create game window
screenWIDTH = 1920
screenHEIGHT = 1080

screen = pygame.display.set_mode((screenWIDTH, screenHEIGHT))

menu_bg = pygame.image.load("menu assets/menu.png")
new_game_bg = pygame.image.load("menu assets/new_game.png")
options_bg = pygame.image.load("menu assets/options_background.jpg")
stats_bg = pygame.image.load("menu assets/scroll.png")

playTime = 0
enemiesDefeated = 0
timesDefeated = 0
completionPercent = 0
masterVol = 100
musicVol = 100
effectsVol = 100
fpsDisplay = 'Yes'
status = False

def get_font(size):
  return pygame.font.Font("menu assets/font.ttf", size)

def startCutscene():
  pygame.display.set_caption("Intro Cutscene")

def newGame():
  pygame.display.set_caption("New Game")

  while True:

    newPosition = pygame.mouse.get_pos()

    screen.blit(new_game_bg, (0,0))

    newText = get_font(31).render("Your story begins now.", True, "White")
    newRect = newText.get_rect(center=(965,460))
    screen.blit(newText,newRect)
    
    new_game_begin = Button(image= None, pos=(980,565), textInput= "Begin", font= get_font(52), baseColor= "white", hoveringColor= "green")
    newBack = Button(image= None, pos=(980,660), textInput= "Back", font= get_font(45), baseColor= "white", hoveringColor= "green")

    for button in [new_game_begin, newBack]:
      button.changeColor(newPosition)
      button.update(screen)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if newBack.checkForInput(newPosition):
          mainMenu()
        if new_game_begin.checkForInput(newPosition):
          startCutscene()

    pygame.display.update()
    
def options():
  pygame.display.set_caption("Options")

  while True:
    optionsPosition = pygame.mouse.get_pos()

    screen.blit(options_bg, (0,0))

    optionsText = get_font(45).render("Options Menu", True, "Black")
    optionsRect = optionsText.get_rect(center=(960,260))
    screen.blit(optionsText, optionsRect)

    optionsVideo = Button(image=None, pos=(960,360), textInput= "VIDEO", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsAudio = Button(image=None, pos=(960,460), textInput= "AUDIO", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsControls = Button(image=None, pos=(960,560), textInput= "CONTROLS", font= get_font(42), baseColor= "Black", hoveringColor= "Green")
    optionsBack = Button(image=None, pos=(960, 660), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")

    for button in [optionsVideo, optionsAudio, optionsControls, optionsBack]:
      button.changeColor(optionsPosition)
      button.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if optionsVideo.checkForInput(optionsPosition):
          video()
        if optionsAudio.checkForInput(optionsPosition):
          audio()
        if optionsControls.checkForInput(optionsPosition):
          controls()
        if optionsBack.checkForInput(optionsPosition):
          mainMenu()

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
    chosenText = get_font(35).render("> " + str(screenWIDTH) + "x" + str(screenHEIGHT) + " <", True, "Black")
    chosenRect = chosenText.get_rect(center=(1360,400))
    screen.blit(chosenText, chosenRect)
    
    videoBack = Button(image=None, pos=(960, 520), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")

    for button in [videoBack]:
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
  
  global masterVol
  global musicVol
  global effectsVol
  
  while True:
    audioPosition = pygame.mouse.get_pos()

    screen.fill("white")

    audioText = get_font(45).render("Audio Options", True, "Black")
    audioRect = audioText.get_rect(center=(960,260))
    screen.blit(audioText, audioRect)
    masterText = get_font(45).render("Master Volume", True, "Black")
    masterRect = masterText.get_rect(center=(360,360))
    screen.blit(masterText, masterRect)
    musicText = get_font(45).render("Music Volume", True, "Black")
    musicRect = musicText.get_rect(center=(340,465))
    screen.blit(musicText, musicRect)
    effectsText = get_font(35).render("Sound Effects Volume", True, "Black")
    effectsRect = effectsText.get_rect(center=(415,560))
    screen.blit(effectsText, effectsRect)
    masterVolume = get_font(35).render(str(masterVol) + "%", True, "Black")
    master_volume_rect = masterVolume.get_rect(center=(1510,360))
    screen.blit(masterVolume, master_volume_rect)
    musicVolume = get_font(35).render(str(musicVol) + "%", True, "Black")
    music_volume_rect = musicVolume.get_rect(center=(1510,465))
    screen.blit(musicVolume, music_volume_rect)
    effectsVolume = get_font(35).render(str(effectsVol) + "%", True, "Black")
    effects_volume_rect = effectsVolume.get_rect(center=(1510,560))
    screen.blit(effectsVolume, effects_volume_rect)
    
    audioBack = Button(image=None, pos=(960, 660), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")
    effectsLeft = Button(image=None, pos=(1250, 560), textInput= "<-" , font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    effectsRight = Button(image=None, pos=(1750, 560), textInput= "->", font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    musicLeft = Button(image=None, pos=(1250, 465), textInput= "<-", font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    musicRight = Button(image=None, pos=(1750, 465), textInput= "->", font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    masterLeft = Button(image=None, pos=(1250, 360), textInput= "<-", font= get_font(55), baseColor= "Black", hoveringColor= "Green")
    masterRight = Button(image=None, pos=(1750, 360), textInput= "->", font= get_font(55), baseColor= "Black", hoveringColor= "Green")

    for button in [audioBack, effectsLeft, effectsRight, musicRight, musicLeft, masterRight, masterLeft]:
      button.changeColor(audioPosition)
      button.update(screen)
      
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if audioBack.checkForInput(audioPosition):
          options()
        elif masterLeft.checkForInput(audioPosition):
          if masterVol > 0 and masterVol <= 100:
            masterVol -= 5
          elif masterVol == 0:
            pass
        elif masterRight.checkForInput(audioPosition):
          if masterVol >= 0 and masterVol < 100:
            masterVol += 5
          elif masterVol == 100:
            pass
        elif musicLeft.checkForInput(audioPosition):
          if musicVol > 0 and musicVol <= 100:
            musicVol -= 5
          elif musicVol == 0:
            pass
        elif musicRight.checkForInput(audioPosition):
          if musicVol >= 0 and musicVol < 100:
            musicVol += 5
          elif musicVol == 100:
            pass
        elif effectsLeft.checkForInput(audioPosition):
          if effectsVol > 0 and effectsVol <= 100:
            effectsVol -= 5
          elif effectsVol == 0:
            pass
        elif effectsRight.checkForInput(audioPosition):
          if effectsVol >= 0 and effectsVol < 100:
            effectsVol += 5
          elif effectsVol == 100:
            pass

        
    pygame.display.update()

def controls():
  pygame.display.set_caption("Controls")
  
  while True:
      controlsPosition = pygame.mouse.get_pos()
  
      screen.fill("white")
  
      controlsText = get_font(45).render("Controls", True, "Black")
      controlsRect = controlsText.get_rect(center=(960,260))
      screen.blit(controlsText, controlsRect)
      pick_piece_text = get_font(38).render("Picking a Piece", True, "Black")
      pick_piece_Rect = pick_piece_text.get_rect(center=(420,400))
      screen.blit(pick_piece_text, pick_piece_Rect)
      piece_choice_text = get_font(32).render("> Press Left Mouse Button <", True, "Black")
      pick_choice_Rect = piece_choice_text.get_rect(center=(1320,400))
      screen.blit(piece_choice_text, pick_choice_Rect)
      move_piece_text = get_font(38).render("Moving a Piece", True, "Black")
      move_piece_rect = move_piece_text.get_rect(center=(400,500))
      screen.blit(move_piece_text, move_piece_rect)
      move_control_text = get_font(32).render("> Drag Left Mouse Button <", True, "Black")
      move_control_rect = move_control_text.get_rect(center=(1300,500))
      screen.blit(move_control_text, move_control_rect)
      shoot_text = get_font(38).render("Shoot", True, "Black")
      shoot_Rect = shoot_text.get_rect(center=(225,600))
      screen.blit(shoot_text, shoot_Rect)
      shoot_control = get_font(32).render("> Press Right Mouse Button <", True, "Black")
      shoot_control_Rect = shoot_control.get_rect(center=(1335,600))
      screen.blit(shoot_control, shoot_control_Rect)
    
      controlsBack = Button(image=None, pos=(960, 700), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "Green")
  
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

    screen.blit(stats_bg, (0,0))

    titleText = get_font(40).render("Game Statistics", True, "Black")
    titleRect = titleText.get_rect(center=(462,150))
    screen.blit(titleText, titleRect)
    timeText = get_font(30).render("Total Play Time = " + str(playTime), True, "Black")
    timeRect = timeText.get_rect(center=(470,250))
    screen.blit(timeText, timeRect)
    enemyText = get_font(30).render("Enemies Defeated = " + str(enemiesDefeated), True, "Black")
    enemyRect = enemyText.get_rect(center=(468,350))
    screen.blit(enemyText, enemyRect)
    defeatedText = get_font(30).render("Times Defeated = " + str(timesDefeated), True, "Black")
    defeatedRect = defeatedText.get_rect(center=(455,450))
    screen.blit(defeatedText, defeatedRect)

    statsBack = Button(image=None, pos=(525, 550), textInput= "BACK", font= get_font(45), baseColor= "Black", hoveringColor= "White")

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

  global frt

  while True:
    screen.blit(menu_bg, (0,0))
    
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

mainMenu()