
import pygame, sys
from pygame import mixer

SQUARE_SIZE = 50

WHITE = (194, 188, 187)

ATTEMPTS = 10
NUM_OF_PEGS = 4

def bg_sound():
  pygame.mixer.init() 
  bg_sound_1 = pygame.mixer.Sound("assets/sound.wav")
  pygame.mixer.Sound.play(bg_sound_1)
  bg_sound_1.play(-1)
  

def open_sound():
  pygame.mixer.init() 
  pygame.mixer.Sound.play(pygame.mixer.Sound("assets/open_sound.wav"))
  # mixer.music.Sound.play(-1)

 
#Creating a window
width = SQUARE_SIZE * NUM_OF_PEGS * 2 + SQUARE_SIZE
hight = SQUARE_SIZE * ATTEMPTS + SQUARE_SIZE
screen = pygame.display.set_mode((width, hight))
background = pygame.image.load('assets/bg_game.png')


COLORED_PEGS = {
  "r": 'assets/red_button_46x46.png',
  "o": 'assets/orange_button_46x46.png',
  "y": 'assets/yellow_button_46x46.png',
  "g": 'assets/green_button_46x46.png',
  "b": 'assets/blue_button_46x46.png',
  "p": 'assets/purple_button_46x46.png'
}

def open_screen():
  open_sound()
  screen = pygame.display.set_mode( ( width, hight) )
  OpenImg = pygame.image.load("assets/mastermind_logo.png")
  ClockOpenImg = pygame.time.Clock()
  imageX= 0 # x coordnate of image
  imageY= 0 # y coordinate of image
  while imageY > -380:
      imageY -= 2.4 ;
      screen.blit(background, (0, 0))# clear screen 
      screen.blit(OpenImg , (imageX, imageY) ) # paint to screen
      pygame.display.update()
      ClockOpenImg.tick(30)


def Img(Img, x, y):
  #drawing pegs or images on the specific coordinates
  screen.blit(Img, (x, y))

def game_setup():
  #Initiailize the pygame
  pygame.init() 

  #Title and Icon
  pygame.display.set_caption("MasterMind")
  icon = pygame.image.load(COLORED_PEGS["p"])
  pygame.display.set_icon(icon)

  #Screen background
  screen.blit(background, (0, 0))

  def draw_grid1():
    #draw grid for the codebreacker input and codemaker output 
    #c - column, r - row
    for c in range(NUM_OF_PEGS):
      for r in range(ATTEMPTS):
        rect = pygame.Rect(c * SQUARE_SIZE + 5, (r+1) * SQUARE_SIZE, SQUARE_SIZE - 5, SQUARE_SIZE - 5)
        pygame.draw.rect(screen, WHITE,rect,1)
        pygame.draw.circle(screen, WHITE,((c + NUM_OF_PEGS +1/2) * SQUARE_SIZE, (r+1.5) * SQUARE_SIZE), (SQUARE_SIZE - 20)/2,2)
  draw_grid1()

  def draw_grid2():
    #draw grid for the hidden row
    for c in range(NUM_OF_PEGS):
      rect = pygame.Rect(c * SQUARE_SIZE + 5, 0, SQUARE_SIZE - 5, SQUARE_SIZE - 5)
      pygame.draw.rect(screen, WHITE,rect,3)
  draw_grid2()

  # Draw the side bar
  RedPegImg = pygame.image.load(COLORED_PEGS["r"])
  RedPeg_choiceX = (width - SQUARE_SIZE)
  RedPeg_choiceY = (hight - SQUARE_SIZE)

  OrangePegImg = pygame.image.load(COLORED_PEGS["o"])
  OrangePeg_choiceX = (width - SQUARE_SIZE)
  OrangePeg_choiceY = (hight - SQUARE_SIZE * 2)

  YellowPegImg = pygame.image.load(COLORED_PEGS["y"])
  YellowPeg_choiceX = (width - SQUARE_SIZE)
  YellowPeg_choiceY = (hight - SQUARE_SIZE * 3)

  GreenPegImg = pygame.image.load(COLORED_PEGS["g"])
  GreenPeg_choiceX = (width - SQUARE_SIZE)
  GreenPeg_choiceY = (hight - SQUARE_SIZE * 4)

  BluePegImg = pygame.image.load(COLORED_PEGS["b"])
  BluePeg_choiceX = (width - SQUARE_SIZE)
  BluePeg_choiceY = (hight - SQUARE_SIZE * 5)

  PurplePegImg = pygame.image.load(COLORED_PEGS["p"])
  PurplePeg_choiceX = (width - SQUARE_SIZE)
  PurplePeg_choiceY = (hight - SQUARE_SIZE * 6)

  ReloadImg = pygame.image.load('assets/reload.png')
  ReloadX = (8 * SQUARE_SIZE)
  ReloadY = 0

  SoundImg = pygame.image.load('assets/sound_button.png')
  SoundX = (8 * SQUARE_SIZE)
  SoundY = SQUARE_SIZE

  Img(RedPegImg, RedPeg_choiceX, RedPeg_choiceY)
  Img(OrangePegImg, OrangePeg_choiceX, OrangePeg_choiceY)
  Img(YellowPegImg, YellowPeg_choiceX, YellowPeg_choiceY)
  Img(GreenPegImg, GreenPeg_choiceX, GreenPeg_choiceY)
  Img(BluePegImg, BluePeg_choiceX, BluePeg_choiceY)
  Img(PurplePegImg, PurplePeg_choiceX, PurplePeg_choiceY)
  Img(ReloadImg, ReloadX, ReloadY)
  Img(SoundImg, SoundX, SoundY)
  pygame.display.update()


def draw_color_peg(PegImg, i, row):
  choiceX = (i*SQUARE_SIZE+5)
  choiceY = (hight - (11-row)*SQUARE_SIZE)
  Img(PegImg, choiceX, choiceY)
  pygame.display.update()

def draw_bw_peg(PegImg, i, row):
  respondX = ((4+i)*SQUARE_SIZE)
  respondY = (hight - (11-row)*SQUARE_SIZE)
  Img(PegImg, respondX, respondY)
  pygame.display.update()
