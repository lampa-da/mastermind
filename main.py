#Please check out README.md for the rules of Mastermind game
import random, pygame, sys
from screen import SQUARE_SIZE, WHITE, NUM_OF_PEGS, ATTEMPTS,COLORED_PEGS, game_setup, Img, hight, width, draw_color_peg, draw_bw_peg, screen, open_screen, bg_sound
from pygame.locals import *
from pygame import mixer


 
open_screen()
game_setup()
#Background sound
bg_sound()

is_sound_on = True

RESPONSE_PEGS = {
  "black": 'assets/black_button_46x46.png',
  "white": 'assets/white_button_46x46.png'
}

def creating_codemaker_row():
  i = 0
  codemaker_row = []
  while i < 4:
    list_of_colors = list(COLORED_PEGS.keys())
    codemaker_row.append(random.choice(list_of_colors))
    i +=1
  print(f"The hidden row is: {codemaker_row}")
  return codemaker_row

def reload(a, b, c, d, event):
  # event.pos[0]  x of the button in a range (a, b)
  # event.pos[1]  y of the button in a range (c, d)
  if a < event.pos[0] < b and c < event.pos[1]< d:
    ATTEMPTS = 10
    game_setup()
    game(ATTEMPTS)



def sound_off_on(a, b, c, d, event):
  # event.pos[0]  x of the button in a range (a, b)
  # event.pos[1]  y of the button in a range (c, d)
  global is_sound_on
  is_sound_on = not is_sound_on
  if a < event.pos[0] < b and c < event.pos[1]< d:
    if is_sound_on  == False:
      pygame.mixer.pause()
    elif is_sound_on == True:
      pygame.mixer.unpause()



def show_hidden_row(codemaker_row):
  for idx, val in enumerate(codemaker_row):
    PegImg = pygame.image.load(COLORED_PEGS[val])
    draw_color_peg(PegImg, idx, 0)

def game_over_screen(codemaker_row):
    show_hidden_row(codemaker_row)
    EndImg = pygame.image.load('assets/game_over.png')
    Img(EndImg, 0, 0)
    pygame.display.update()

def game(ATTEMPTS):
  
  #Creating codemaker row
  codemaker_row = creating_codemaker_row()
  game_is_on = True
  #Game Loop
  while True:
    #Sidebar panel
    while game_is_on == True: 
      codebreaker_row = [] 
      i = 0
      while i < NUM_OF_PEGS and ATTEMPTS > 0:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            #Quiting the game
            pygame.quit()
            sys.exit()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            #Color pegs
            if 400 < event.pos[0] < 450 and event.pos[1]>250:
              if 500 < event.pos[1] < 550:
                selected_color = "r"
              elif 450 < event.pos[1] < 500:
                selected_color = "o"
              elif 400 < event.pos[1] < 450:
                selected_color = "y"
              elif 350 < event.pos[1] < 400:
                selected_color = "g"
              elif 300 < event.pos[1] < 350:
                selected_color = "b"
              elif 250 < event.pos[1] < 300:
                selected_color = "p"
              codebreaker_row.append(selected_color)
              PegImg = pygame.image.load(COLORED_PEGS[selected_color])
              draw_color_peg(PegImg, i, ATTEMPTS)
              i +=1
            # Reload button
            reload(400, 450, 0, 50, event)  
            # Sound button
            sound_off_on(400, 450, 50, 100, event) 
         

      codemaker_row_copy = codemaker_row[:]
      codebreaker_row_copy = codebreaker_row[:]
      codemaker_response = []

      #Computer response
      for idx1, val1 in enumerate(codebreaker_row_copy):
        for idx2, val2 in enumerate(codemaker_row_copy):
          if idx1 == idx2 and val1 == val2:
            codemaker_response.append("black")
            codemaker_row_copy[idx2] = None
            codebreaker_row_copy[idx1] = None
      for idx1, val1 in enumerate(codebreaker_row_copy):
        for idx2, val2 in enumerate(codemaker_row_copy):
          if val2 == val1 and idx1 != idx2 and val1 != None:
            codemaker_response.append("white")
            codemaker_row_copy[idx2] = None 
            codebreaker_row_copy[idx1] = None
            break

      #Computer response - visual part
      for idx, val in enumerate(codemaker_response):
        PegImg = pygame.image.load(RESPONSE_PEGS[val])
        draw_bw_peg(PegImg, idx, ATTEMPTS)


      print(f"Codemaker response is:\n{codemaker_response}")
      
      ATTEMPTS = ATTEMPTS - 1

      # Win/lose check
      if ATTEMPTS >= 0 and codemaker_response == ["black", "black", "black", "black"]:
        WinImg = pygame.image.load('assets/you_win.png')
        Img(WinImg, 200, 0)
        print ("you win!")
        game_over_screen(codemaker_row) 
        game_is_on = False 
        break
      elif ATTEMPTS < 0 and codemaker_response != ["black", "black", "black", "black"]:
        LoseImg = pygame.image.load('assets/you_lose.png')
        Img(LoseImg, 200, 0)
        print ("Sorry! You lose!")
        game_over_screen(codemaker_row)
        game_is_on = False 
        break

      print (f"You have {ATTEMPTS} attempts")
    
    #Reload the game
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        reload(100, 350, 250, 300, event)
  
game(ATTEMPTS)
