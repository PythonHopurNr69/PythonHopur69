import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
gameDisplay = pygame.display.set_mode((800,600))
list_Enemies = []
high_svores = [0,0,0]
#font style for all text
font = pygame.font.SysFont(None,25)

def maingame():
  list_Enemies.clear()
  x_cord = 67
  y_cord = 540 
  enemy_cord_x = random.randint(50, 750)
  enemy_cord_y = 20
  list_Enemies.append([enemy_cord_x, enemy_cord_y])
  gameExit = False 
  gameDisplay.fill(white)
  pygame.display.update()
  while gameExit == False:
    for event in pygame.event.get():
      print('as')
      print(event)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          gameExit = True
        if event.key == pygame.K_LEFT and x_cord > 50:
           x_cord = x_cord - 50
           moveMent(x_cord, y_cord, 10, black)
        if event.key == pygame.K_RIGHT and x_cord < 750:
            x_cord = x_cord + 50
            moveMent(x_cord, y_cord, 10, black)
#        if event.key == pygame.K_SPACE:
#            fireShot(x_cord, y_cord, 2)
#            shots_moving.append([x_cord, y_cord])
    gameDisplay.fill(white)
#    for i in shots_moving:
#        i[1] -= 3.6
    for i in list_Enemies:
        i[1] += 10
        if i[1] > 690:
          gameExit = GameOver()
          break
    moveMent(x_cord, y_cord, 10, black)
    pygame.display.update()


def moveMent(x, y, size, color):
    pygame.draw.rect(gameDisplay, color, [x,y,size,size])
    displayEnemies(list_Enemies)
    pygame.display.update()

def fireShot(startPos, endPos, w):
    pygame.draw.line(gameDisplay, black, startPos, endPos, w)
    pygame.display.update()


def displayEnemies(lisEnemies):
    for i in lisEnemies:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 20, 20])

def display_message(msg):
  screen_text = font.render(msg,True,black)
  gameDisplay.blit(screen_text,[ 400, 300])

def GameOver():
  display_message('YOU LOSE!!, play again? (Y/N)')
  pygame.display.update()
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
          maingame()
          return True
        elif event.key == pygame.K_n:
          return True

  gameExit = True

maingame()


    