import pygame
import random
import time
from tkinter import *
import tkinter.messagebox
from score_repo import HighScores


pygame.init()

#pygame.time.clock is used to make the game feel more natural when playing (30 fps)
clock = pygame.time.Clock()
FPS = 30
#setting up the colors before we use them
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255, 255, 0)

#display width and height so we din't hard code the display. rather use a changable variable (can be changed while not changeing the core game)
display_width = 800
display_height = 600

#movement for the main caracter (the player)
jump_movement = 50

#timer and set_timer is so an enemy spawnes every "timer" milliseconds (timer changes througout game check def raise_point)
spawn_enemy = pygame.USEREVENT +1
timer = 1000
pygame.time.set_timer(pygame.USEREVENT +1, timer)

#lvl_up is used to display how mutch points the player has to get to lvl up, and lvl is the current lvl
lvl_up = 20
lvl = 1

#shot_speed and enemy_speed, determins the speed of the enemy and bullets, is changed throughout the game
shot_speed = 3.5
enemy_speed = 2.5

#our displays, for our game and menu
menuDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay = pygame.display.set_mode((display_width,display_height))

# to create the enemies and shots we appended them into these lists and removed when destroyed or out of bounds
list_Enemies = []
shots_moving = []

# list allowed space is so that an enemy will never appear in a place that the player can't shoot from
list_allowed_space = []

#our font for the text that appiers through out the game
font = pygame.font.SysFont(None, 25)
_highscores = HighScores()
entry = Entry()

#def initialize initializes everything we need in the main loop, 
# (it's basicly reseting everything to make the game play from lvl 1)
def initialize():
  global timer
  global list_Enemies
  global shot_speed
  global enemy_speed
  global lvl 
  global lvl_up
  global points
  points = 0
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

#our game loop
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

  #game loop starst
  while gameExit == False:

    #the for "event" and if "event.type" takes the values of what the player has pressed on their keyboard
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          #if the Q key is pressed, quit the game 
          gameExit = True
        
        elif event.key == pygame.K_LEFT and x_cord > jump_movement:
          # if the left key is pressed, the player x-coordinates will move left for 50 pixles (jump_movement) if the player is not out of bounds
          x_cord = x_cord - jump_movement
          moveMent(x_cord, y_cord, 10, black)
        
        elif event.key == pygame.K_RIGHT and x_cord < int(display_width-jump_movement):
          # if the right key is pressed the x-coordinates of the player will be moved right 50 pixles (jump_movemnt) if the player is not out of bounds
          x_cord = x_cord + jump_movement
          moveMent(x_cord, y_cord, 10, black)
        
        elif event.key == pygame.K_SPACE:
          #if the spacebar is pressed a shot will be appended into "shots moveing" containing the x and y coordinates of the shot 
          fireShot(x_cord, y_cord, 2)
          shots_moving.append([x_cord, y_cord])
      elif event.type == spawn_enemy:
        # the timer that is set in initialize will send an event "spawn enemy" every "timer"-milliseconds, and that will trigger this to spawn the enemy
        add_enemy()
    gameDisplay.fill(white)
    #This makes the clock tick every "FPS"-per second, and makes the game run at 30 fps 
    clock.tick(FPS)

#this for loop changes the y coordinates of the shots to make them seem like they'r moving,
# and if the y-coordinates is less then 0 then remove it from the list (so it doesn't get unnessiserily large)
    for i in shots_moving:
      i[1] -= shot_speed
      if i[1] < 0:
        shots_moving.remove(i)
    check_if_hit()
    displayPoints(points)

# this for loop changes the y coordinates of every enemy to make it seem like they're moving 
#and check if any one of them are touching the player and if that is true, the game is over
    for i in list_Enemies:
      i[1] += enemy_speed
      #check if the player is hit
      if i[0] > x_cord and i[0] < x_cord +20 or i[0] + 10 > x_cord and i[0] + 10 < x_cord + 20:
        if i[1] > y_cord and i[1] < y_cord + 20 or i[1]+10 > y_cord and i[1] + 10 < y_cord+ 20:
          gameExit = gameOver()
      #this if is if multiple shots hit the same target the game doesnt crash
      if i[1]> display_height:
        if i in list_Enemies:
          list_Enemies.remove(i)
    check_if_hit()
    #and in the end displays the movement 
    moveMent(x_cord, y_cord, 10, black)
#        gameExit = gameOver()

#our main menu
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
  #this while loop checks every event that the player makes and if it't a certain event (for example: hits 3 on his/her keyboard) and does something
  while 1:
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          return pygame.quit()
        elif event.key == pygame.K_2:
          print(displayHighScores())
        elif event.key == pygame.K_1:
          return maingame()
        elif event.key == pygame.K_3:
          how_to_play()


#this displayes the insturctions on how to play 
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
  str_point = str(points)
  newHighScore = entry.get()
  newHighScore = 'name: ' + newHighScore + ' ' + 'Score: ' + str_point

  if newHighScore and _highscores.add_score(newHighScore):
      tmp = disp_scores.get()
      tmp += '\n' + newHighScore
      disp_scores.set(tmp)
  else:
      tkinter.messagebox.showinfo('Error, could not add scores')

  
#check if hit is called either when an enemy has moved or when a shot has been moved to check if
#an enemy was hit and has to be "deleted" from the enemy list and shot list
def check_if_hit():
  for i in list_Enemies:
    for e in shots_moving:
        if i[0] > e[0] and i[0] < e[0] +15 or i[0] + 10 > e[0] and i[0] + 10 < e[0] + 15:
          if i[1] > e[1] and i[1] < e[1] + 15 or i[1]+10 > e[1] and i[1] + 10 < e[1]+ 15:
            list_Enemies.remove(i)
            shots_moving.remove(e)
            raisePoints()

#add enemy adds an enemy from a set x-coordinate (0, at the top) and a random y-coordinate form a list of allowed y coordinates that the player can hit 
def add_enemy():
  list_Enemies.append([random.choice(list_allowed_space),0])

#our def moveMent is called when the player moves a caracter or when an enemy moves
def moveMent(x, y, size, color):
  gameDisplay.fill(white)
  displayPoints(points)
  pygame.draw.rect(gameDisplay, color, [x,y,size,size])
  displayEnemies(list_Enemies)
  displayShots(shots_moving)
  pygame.display.update()

#when a shot is fired, what position it should take
def fireShot(startPos, endPos, w):
  pygame.draw.circle(gameDisplay, yellow, [startPos + 5, endPos - 10],  10)
  displayShots(shots_moving)
  pygame.display.update()

#displays our shots, is called mainly in our def moveMent 
def displayShots(lisMoving):
    for i in shots_moving:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 5, 5])

#def displayEnemies is used to display enemies and is primaraly used in def moveMent
def displayEnemies(lisEnemies):
    for i in lisEnemies:
        pygame.draw.rect(gameDisplay, red, [i[0], i[1], 20, 20])

# what to display when the game is over and the player loses
def gameOver():
  messageToScreen('YOU LOSE!, PLAY AGAIN? (Y/N)')
  # the for and if event in while loop takes an event from the player if he/she want's to continue or quit 
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


#messageToScreen is called with a string delimiter that contains the message that is supposed to be shown on screen
def messageToScreen(msg):
  message = font.render(msg,True, red)
  gameDisplay.blit(message,[display_height/4,display_width/2])
  pygame.display.update()

#displays the points in the left hand corner
def displayPoints(points):
  scoreboard = font.render("Score {0}".format(points) + " lvl: " + str(lvl), 1, (0,0,0))
  gameDisplay.blit(scoreboard, (5, 10))

# a function that is called when the points have been rased, lvls up and makes the game harder the longer it goes on
def raisePoints():
    global lvl
    global points
    global timer
    global lvl_up
    global shot_speed
    global enemy_speed
    points = points + 1
    #the if statements here are to make the enemies spawn quicker, from 1000ms to 900ms and so on 
    if points > lvl_up:
      lvl += 1
      if timer > 600:
        timer -= 200
      elif timer > 100:
        timer -=100
      else:
        timer = (int(timer/2))+1
      #when lvl 10 has been reached the enemy sped will reset to 2.5 but the enemie spawn timer will still be going, to keep the game fresh after lvl 10 
      if lvl == 10:
        enemy_speed =2.5
      lvl_up += 20
      shot_speed += 2
      enemy_speed += 1
      pygame.time.set_timer(spawn_enemy, timer)

mainMenu()
