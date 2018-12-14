import pygame
import random
import time
from tkinter import *
import tkinter.messagebox
from score_repo import HighScores


pygame.init()
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)
display_width = 800
display_height = 600
jump_movement = 50
spawn_enemy = pygame.USEREVENT  + 1
timer = 1000
lvl_up = 20
lvl = 1
shot_speed = 3.5
enemy_speed = 2.5
menuDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay = pygame.display.set_mode((display_width,display_height))
list_Enemies = []
shots_moving = []
list_allowed_space = []
font = pygame.font.SysFont(None, 25)
_highscores = HighScores()
entry = Entry()

def initialize():
  global timer
  global list_Enemies
  global shot_speed
  global enemy_speed
  global lvl 
  global lvl_up
  lvl_up = 20
  lvl = 1 
  timer = 1000
  shot_speed = 3.5
  enemy_speed =2.5
  list_Enemies.clear()
  shots_moving.clear()
  for i in range(int(display_height/40),display_width, jump_movement):
    list_allowed_space.append(i)
  clock.tick()
  pygame.time.set_timer(spawn_enemy, timer)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.time.set_timer(pygame.USEREVENT +1, timer)
  
  
def maingame():
  initialize()
  x_cord = 67
  y_cord = int(display_height - (display_height/10)) 
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
        elif event.key == pygame.K_LEFT and x_cord > jump_movement:
           x_cord = x_cord - jump_movement
           moveMent(x_cord, y_cord, 10, black)
        elif event.key == pygame.K_RIGHT and x_cord < int(display_width-jump_movement):
            x_cord = x_cord + jump_movement
            moveMent(x_cord, y_cord, 10, black)
        elif event.key == pygame.K_SPACE:
            fireShot(x_cord, y_cord, 2)
            shots_moving.append([x_cord, y_cord])
        elif event.key == pygame.K_e:
          list_Enemies.append([(random.choice(list_allowed_space)), enemy_cord_y])
      elif event.type == pygame.MOUSEBUTTONDOWN:
        print(event)
      elif event.type == spawn_enemy:
        add_enemy()
    gameDisplay.fill(white)
    clock.tick(30)

    for i in shots_moving:
      i[1] -= shot_speed
      if i[1] < 0:
        shots_moving.remove(i)
    check_if_hit()
    displayPoints(points)
    for i in list_Enemies:
      i[1] += enemy_speed
      if i[0] > x_cord and i[0] < x_cord +20 or i[0] + 10 > x_cord and i[0] + 10 < x_cord + 20:
        if i[1] > y_cord and i[1] < y_cord + 20 or i[1]+10 > y_cord and i[1] + 10 < y_cord+ 20:
          gameExit = gameOver()
      if i[1]> display_height:
        if i in list_Enemies:
          list_Enemies.remove(i)
    check_if_hit()
    moveMent(x_cord, y_cord, 10, black)
#        gameExit = gameOver()

def mainMenu():
  menuDisplay.fill(black)

  TitleMessage = font.render("BLOOOCKFUUUDGER", True, red)
  gameDisplay.blit(TitleMessage, [600,100],)

  TitleMessage = font.render("3 --- HOW TO PLAY", True, red)
  gameDisplay.blit(TitleMessage, [600,500],)

  StartMessage = font.render("1 --- StartGame", True, red)
  gameDisplay.blit(StartMessage, [600,200])

  HighScore = font.render("2 --- HighScore", True, red)
  gameDisplay.blit(HighScore, [600,300])
  
  ExitMessage = font.render("q --- Exit program", True, red)
  gameDisplay.blit(ExitMessage, [600, 400])
  pygame.display.update()
  while 1:
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return pygame.quit()
        elif event.key == pygame.K_2:
          print(displayHighScores())
        elif event.key == pygame.K_1:
          return maingame()
        elif event.key == pygame.K_3:
          how_to_play()
def how_to_play():
  message = font.render('in this game you play as a black box and your goal is to shoot the red boxes for points',True, red)
  gameDisplay.blit(message,[display_height/4,display_width/2])
def displayHighScores():
  window = Tk()
  disp_scores = StringVar()
  window.title("HighScores")
  window.configure(background='pink')
  Frame(width=500, height=500, background='pink').pack()
  for score in _highscores.get_scores():
      tmp = disp_scores.get()
      tmp += '\n' + score
      disp_scores.set(tmp)
  the_jokes = Label(textvariable=disp_scores, anchor='w', justify='left', wraplength=500, background='pink')
  the_jokes.pack()
  the_jokes.place(y=0)
  window.mainloop()
  mainMenu()  
  
    
def saveHighScores():
  root = Tk()
  root.geometry("200x100")
  #textBox=Text(root, height=2, width=10)
  #inputVal = textBox.get("1.0")
  #textBox.pack()
  #global points
  #buttonCommit = Button(root, height=1, width=1, text="commit",
                  #command=lambda: _highscores.add_score(inputVal))
  #buttonCommit.pack()
  
  Button(text='Submit name', command=commitHighScores, background='green').pack()
  entry.pack(fill=X)
  mainloop()


def commitHighScores():
  disp_scores = StringVar()
  global points
  newHighScore = entry.get()

  if newHighScore and _highscores.add_score(newHighScore):
      tmp = disp_scores.get()
      tmp += '\n' + newHighScore
      disp_scores.set(tmp)
  else:
      tkinter.messagebox.showinfo('Error, could not add scores')

  

def check_if_hit():
  for i in list_Enemies:
    for e in shots_moving:
        if i[0] > e[0] and i[0] < e[0] +15 or i[0] + 10 > e[0] and i[0] + 10 < e[0] + 15:
          if i[1] > e[1] and i[1] < e[1] + 15 or i[1]+10 > e[1] and i[1] + 10 < e[1]+ 15:
            list_Enemies.remove(i)
            shots_moving.remove(e)
            raisePoints()

def add_enemy():
  list_Enemies.append([random.choice(list_allowed_space),0])
      
def moveMent(x, y, size, color):
  gameDisplay.fill(white)
  displayPoints(points)
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
#  messageToScreen('YOU LOSE!, PLAY AGAIN? (Y/N)')
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_y:
          maingame()
          return True
        elif event.key == pygame.K_n:
          saveHighScores()
          mainMenu()
          return True


def messageToScreen(msg):
  message = font.render(msg,True, red)
  gameDisplay.blit(message,[display_height/4,display_width/2])
  pygame.display.update()

def displayPoints(points):
  scoreboard = font.render("Score {0}".format(points) + " lvl: " + str(lvl), 1, (0,0,0))
  gameDisplay.blit(scoreboard, (5, 10))


def raisePoints():
    global lvl
    global points
    global timer
    global lvl_up
    global shot_speed
    global enemy_speed
    points = points + 1
    if points > lvl_up:
      lvl += 1
      if timer > 600:
        timer -= 200
      elif timer > 100:
        timer -=100
      else:
        timer = (int(timer/2))+1
      if lvl == 10:
        enemy_speed =2.5
      lvl_up += 20
      shot_speed += 2
      enemy_speed += 1
      pygame.time.set_timer(spawn_enemy, timer)

mainMenu()
