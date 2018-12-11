import pygame

pygame.init()
white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,600))

  
def maingame():
  x_cord = 67
  y_cord = 540 
  gameExit = False 
  gameDisplay.fill(white)
  pygame.display.update()
  while gameExit == False: 
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          gameExit = True
        if event.key == pygame.K_LEFT:
           x_cord = x_cord - 10
           moveMent(x_cord, y_cord, 10)
        if event.key == pygame.K_RIGHT:
            x_cord = x_cord + 10
            moveMent(x_cord, y_cord, 10)
    pygame.draw.rect(gameDisplay,black, [10,10,10,10])
  

def moveMent(x, y, size):
    pygame.draw.rect(gameDisplay, black, [x,y,size,size])
    pygame.display.update()
  
maingame()


    