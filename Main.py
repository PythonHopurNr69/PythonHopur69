import pygame
import random
import time
import scores as HScores

pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)
display_width = 800
display_height = 600
menuDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay = pygame.display.set_mode((display_width,display_height))
list_Enemies = []
shots_moving = []
points = 0

list_allowed_space = [20,70,120,170,220,270,320,370,420,470,520,570,620,670,720,770]
font = pygame.font.SysFont(None, 25)
  
def maingame():
  
  list_Enemies.clear()
  shots_moving.clear()
  x_cord = 67
  y_cord = 540 
  enemy_cord_x = random.choice(list_allowed_space)
  enemy_cord_y = 20
  list_Enemies.append([enemy_cord_x, enemy_cord_y])
  gameExit = False 
  gameDisplay.fill(white)
  global points
  points = 0
  pygame.display.update()
  while gameExit == False:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          gameExit = True
        elif event.key == pygame.K_LEFT and x_cord > 50:
           x_cord = x_cord - 50
           moveMent(x_cord, y_cord, 10, black)
        elif event.key == pygame.K_RIGHT and x_cord < 750:
            x_cord = x_cord + 50
            moveMent(x_cord, y_cord, 10, black)
        elif event.key == pygame.K_SPACE:
            fireShot(x_cord, y_cord, 2)
            shots_moving.append([x_cord, y_cord])
        elif event.key == pygame.K_e:
          list_Enemies.append([(random.choice(list_allowed_space)), enemy_cord_y])
      elif event.type == pygame.MOUSEBUTTONDOWN:
        print(event)
    gameDisplay.fill(white)
    clock.tick(30)

    for i in shots_moving:
      i[1] -= 3.6
      if i[1] < 0:
        shots_moving.remove(i)
    check_if_hit()

    moveMent(x_cord, y_cord, 10, black)
    displayPoints(points)
    pygame.display.update()

    for i in list_Enemies:
      i[1] += 2.5
      if i[0] > x_cord and i[0] < x_cord +15 or i[0] + 10 > x_cord and i[0] + 10 < x_cord + 15:
        if i[1] > y_cord and i[1] < y_cord + 15 or i[1]+10 > y_cord and i[1] + 10 < y_cord+ 15:
          gameExit = gameOver()
        if i[1]> 650:
          list_Enemies.remove(i)
#          gameExit = gameOver()

def mainMenu():
  menuDisplay.fill(black)

  TitleMessage = font.render("BLOOOCKFUUUDGER", True, red)
  gameDisplay.blit(TitleMessage, [600,100],)

  StartMessage = font.render("1 --- StartGame", True, red)
  gameDisplay.blit(StartMessage, [600,300])

  HighScore = font.render("2 --- HighScore", True, red)
  gameDisplay.blit(HighScore, [600,400])
  
  ExitMessage = font.render("q --- Exit program", True, red)
  gameDisplay.blit(ExitMessage, [600, 500])
  pygame.display.update()
  while 1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return pygame.quit()
        if event.key == pygame.K_2:
          print(displayHighScores())
        if event.key == pygame.K_1:
          return maingame()

def displayHighScores():
    highscores = HScores.load()
    for y, (hi_name, hi_score) in enumerate(highscores):
        FONT.render_to(screen, (100, y*30+40), f'{hi_name} {hi_score}', BLUE)
    gameDisplay.fill((30, 30, 50))


def check_if_hit():
  for i in list_Enemies:
    for e in shots_moving:
        if i[0] > e[0] and i[0] < e[0] +15 or i[0] + 10 > e[0] and i[0] + 10 < e[0] + 15:
          if i[1] > e[1] and i[1] < e[1] + 15 or i[1]+10 > e[1] and i[1] + 10 < e[1]+ 15:
            list_Enemies.remove((i))
            shots_moving.remove(e)
            raisePoints()
     
def moveMent(x, y, size, color):
    pygame.draw.rect(gameDisplay, color, [x,y,size,size])
    displayEnemies(list_Enemies)
    displayShots(shots_moving)
    pygame.display.update()

def fireShot(startPos, endPos, w):
    pygame.draw.circle(gameDisplay, yellow, [startPos + 5, endPos - 10],  10)
    displayShots(shots_moving)
    pygame.display.update()

def displayShots(lisMoving):
    for i in shots_moving:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 5, 5])

def displayEnemies(lisEnemies):
    for i in lisEnemies:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 20, 20])

def gameOver():
  messageToScreen('YOU LOSE!, PLAY AGAIN? (Y/N)')
  pygame.display.update()
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
          maingame()
          return True
        elif event.key == pygame.K_n:
          mainMenu()
          return True

def messageToScreen(msg):
  message = font.render(msg,True, black)
  gameDisplay.blit(message,[400,300])

def displayPoints(points):
    scoreboard = font.render("Score {0}".format(points), 1, (0,0,0))
    gameDisplay.blit(scoreboard, (5, 10))

def raisePoints():
    global points
    points = points + 1

mainMenu()


    