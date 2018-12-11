import pygame

pygame.init()
white = (255,255,255)
black = (0,0,0)
gameDisplay = pygame.display.set_mode((800,600))

gameExit = False 
gameDisplay.fill(white)
pygame.display.update()
while not gameExit: 
  for event in pygame.event.get():
    print(event)
    if event.type == pygame.KEYDOWN:
      gameExit = True
  pygame.draw.rect(gameDisplay,black, [10,10,10,10])
  pygame.display.update()