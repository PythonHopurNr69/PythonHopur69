import pygame
import random
import time

pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)
gameDisplay = pygame.display.set_mode((800,600))
list_Enemies = []
shots_moving = []

  
def maingame():
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
        if event.key == pygame.K_SPACE:
            fireShot(x_cord, y_cord, 2)
            shots_moving.append([x_cord, y_cord])
    gameDisplay.fill(white)
    clock.tick(30)
    for i in list_Enemies:
        i[1] += 2.5

    for i in shots_moving:
        i[1] -= 3.6

    moveMent(x_cord, y_cord, 10, black)
    pygame.display.update()
  
def moveMent(x, y, size, color):
    pygame.draw.rect(gameDisplay, color, [x,y,size,size])
    displayEnemies(list_Enemies)
    displayShots(shots_moving)
    pygame.display.update()

def fireShot(startPos, endPos, w):
    #pygame.draw.line(gameDisplay, black, (startPos, startPos), (endPos, endPos), w)
    pygame.draw.circle(gameDisplay, yellow, [startPos + 5, endPos - 10], 4 )
    displayShots(shots_moving)
    

    pygame.display.update()

def displayShots(lisMoving):
    for i in shots_moving:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 5, 5])

def displayEnemies(lisEnemies):
    for i in lisEnemies:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 20, 20])

maingame()


    