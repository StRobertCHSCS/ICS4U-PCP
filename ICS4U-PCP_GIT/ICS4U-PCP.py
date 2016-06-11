

# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# https://gist.githubusercontent.com/sanchitgangwar/2158089/raw/5f3d0003801acfe1a29c4b24f2c8975efacf6f66/snake.py

#below code needs to be fixed
#from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time
import curses.panel
#import threading
import sys

# -------------------------------------------------------
# Global Varibles
# -------------------------------------------------------
IS_DEBUG = False

MAX_Y = 0            # current screen Y
MAX_X = 0            # current screen X
REQ_Y = 0            # required screen size Y
REQ_X = 0            # required screen size X
ENG_WORDS = ["apple","hi","hello","aaron",""]
ENG_WORDS_LEN = 0
PY_WORDS = []
PY_WORDS_LEN = 0
STDSCR = ""
MIN_WORD_LEN = 0
MAX_WORD_LEN = 0
WORD = ""

class Word(object):
  """
  Representation of words
  """
  def __init__(self, diff,  ptype):
    """
    selects a word according to user difficulty
    :param diffc: str - difficulty selected by user
    :param ptype: str - game type selected by user
    :return: str -
    """
    word = ""

    #add more difficulties
    if ptype == "prac":
      if diff == "easy" or diff == "medium":
        global MIN_WORD_LEN,MAX_WORD_LEN,WORD
        MIN_WORD_LEN = 0
        MAX_WORD_LEN = 3
        for idx in range(len(ENG_WORDS)):
          if len(ENG_WORDS[idx]) > MIN_WORD_LEN and len(ENG_WORDS[idx]) <= MAX_WORD_LEN:
            Word = ENG_WORDS[idx]

  def move_down(screen, word):
   word = WORD
   empty = " " * len(word[2])
   screen.addstr(word[0], word[1], empty)
   word[0] += 1
   screen.addstr(word[0], word[1], word[2])

  def create_word(screen, word):
    while 1:
      word_len = 4
      word = ""
      for ch_num in range(word_len):
        ch = chr(randint(ord('a'), ord('z')))
        word += ch
        x = randint(0, SCR_X_MAX)
        y_x_word = [ 0, x, word ]
        #debug("new word: "+str(y_x_word), 2)
        return y_x_word
        #screen.border(0)
        global test_val
        global ent

      if word:
        screen.addstr(12, 12, 'testval:'+str(test_val))
        screen.refresh()

        if ent == word[2]:
          global curses
          curses.beep()
          word = None

      time.sleep(0.5)

  def getX(self):

    return self.x

  def getY(self):

    return self.y
ent = ""
test_val = 1
SCR_Y_MAX = 40
SCR_X_MAX = 60

def drawCoor():

  STDSCR.clear()
  STDSCR.border(0)
  STDSCR.refresh()
  for x in range(MAX_X):
    STDSCR.addstr(2,x, str(x%10))
    if (x % 10 == 0):
      STDSCR.addstr(1,x, str(x//10))

  for y in range(MAX_Y):
    STDSCR.addstr(y,2, str(y%10))
    if (y % 10 == 0):
      STDSCR.addstr(y,1, str(y//10))

  STDSCR.refresh()

def my_raw_input(stdscr, r, c, prompt_string):
    curses.echo()
    stdscr.addstr(r, c, prompt_string)
    stdscr.refresh()
    input = stdscr.getstr(r + 1, c, 20)
    return input  #       ^^^^  reading input at next line

def clear_line(y):
  empty = " " * SCR_X_MAX
  STDSCR.addstr(y, 1, empty)

def debug(msg, level):
  """
  """
  y = SCR_Y_MAX - 10 + level
  clear_line(y)


                                               # Initializing values


saved =""

def GamePlay():

  while True:
    stdscr = STDSCR
    STDSCR.clear()
    STDSCR.refresh()

    saved =""
    y_entered = MAX_Y
    x_entered = 10

    enter_win = curses.newwin(1, 70, y_entered, x_entered)  # l, w, y, x
    enter_panel = curses.panel.new_panel(enter_win)
    enter_panel.top()
    while True:

      event = STDSCR.getch()

      global test_val
      test_val += 1
      event = stdscr.getch()
      if event != 10:
        saved += chr(event)
      if event == 8:
        stdscr.addstr(15,10, 'backspace')
        saved = saved[:-2]
      stdscr.addstr(10,10, '                                                          ')
      stdscr.addstr(10,10, 'saved:['+str(saved) + '] event: ' +str(event))
      if event == 10:
        global ent
        ent = saved
        saved = ""
        stdscr.addstr(10,10, 'saved:['+str(saved) + '] event: ' +str(event))

      if event == 27:
        break

      #stats screen
      if chr(event) == 's' or 'S':
        enter_panel.hide()
        userstats()

      if event != 10 and event !=263:  # enter and backspace
        # saved += chr(event)
        if event == 263:  # backspace
          saved = saved[:-1]
          enter_win.noutrefresh()
        curses.doupdate()

        # enter
        if event == 10:
          global USER_ENT
          USER_ENT = saved
          saved = ""

          enter_win.addstr(0,0,saved)
          enter_win.noutrefresh()
          curses.doupdate()

        if event == 9: #tab to exit
          EXIT_GAME = True

        if event == 27: #esc
          break

    if EXIT_GAME:
      break


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main(stdscr):
  #colors
  curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
  curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
  curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
  curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
  curses.init_pair(6,curses.COLOR_CYAN,curses.COLOR_BLACK)
  curses.init_pair(7,curses.COLOR_BLUE,curses.COLOR_BLACK)

  global EXIT_GAME

  # Set up for debug
  global STDSCR
  STDSCR = stdscr

  # Check the required window size
  checkReq()

  # clear and draw coordinates
  if IS_DEBUG:
    drawCoor()

  #define this after the window's created.
  #horizontal line decides whether user missed or not.
  global MISS_Y
  MISS_Y = MAX_Y - 3

  while 1:
    # re-initialize
    EXIT_GAME = False

    # main game screen
    rc = mainGameScreen()

    # reset
    if rc == 4:
      STDSCR.clear(); STDSCR.refresh()

    # exit
    if rc == 0:
      break

  curses.endwin()

###############################################################################
#
# Screens
#
###############################################################################

def mainGameScreen():
  """
  makes the main screen of the game
  :return: int - assigned number of the each screen
  """
  STDSCR.clear()
  STDSCR.refresh()
  # debug
  if IS_DEBUG:
    drawCoor()

  # Draw menu
  menu1 = "[P] PLAY"
  menu2 = "[S] Statistics"
  menu3 = "[X] EXIT"
  menu_win = curses.newwin(11, len(menu2) + 4 , 30, 78)  # h, l, y, x
  menu_win.addstr(1, 1, menu1,curses.A_BOLD)
  menu_win.addstr(2+3, 1, menu2,curses.A_BOLD)
  menu_win.addstr(3+6, 1, menu3,curses.A_BOLD)
  menu_panel = curses.panel.new_panel(menu_win)
  menu_panel.top();curses.panel.update_panels()
  menu_win.noutrefresh(); curses.doupdate()

  #initialize
  main_rc = 0

  while 1:
    # Get an input from a user
    event = STDSCR.getch()
    if event == 263:
      continue
    #exit
    if chr(event) == 'x':
      main_rc = 0
      break

    #stats screen
    elif chr(event) == 's':
      #title_panel.hide()
      menu_panel.hide()
      main_rc = 1

    #Play
    elif chr(event) == 'p':
      play1 = "[P] Practice - English words"
      play2 = "[C] Coding - Python related words"
      play_win = curses.newwin(6, len(play2) + 4, 32, 83) #h,l,y,x
      play_win.box()
      play_win.addstr(1+1, 1, play1,curses.A_BOLD)
      play_win.addstr(2+1, 1, play2,curses.A_BOLD)
      play1_panel = curses.panel.new_panel(play_win)
      play1_panel.top()
      curses.panel.update_panels()
      STDSCR.noutrefresh()
      curses.doupdate()

      event = STDSCR.getch()

      while event == 263:
        event = STDSCR.getch()

      event_lower = chr(event).lower()

      while event_lower != "p" and event_lower != "c":
        event = STDSCR.getch()
        event_lower = chr(event).lower()

      ptype = ""
      if event_lower == "p":
        ptype = "prac"
      else:
        ptype = "coding"

      while 1:
        if ptype == "prac":
          play1 = "[E] Easy - words length of 3 - 4"
          play2 = "[M] Medium - words length of 5 and more"
          play3 = "[H] Hard - random char and symbols"
          play4 = "[R] reset"
        else:
          play1 = "[E] Easy - words length of 3 - 5"
          play2 = "[M] Medium - words lenght of 5 - 10"
          play3 = "[H] Hard - words length of 5 and more"
          play4 = "[R] reset"

        play2_win = curses.newwin(9, len(play2) + 4, 34, 90)
        play2_win.box()
        play2_win.addstr(1 + 1, 1, play1,curses.A_BOLD)
        play2_win.addstr(2 + 1, 1, play2,curses.A_BOLD)
        play2_win.addstr(3 + 1, 1, play3,curses.A_BOLD)
        play2_win.addstr(4 + 1, 1, play4,curses.A_BOLD)
        play2_panel = curses.panel.new_panel(play2_win)
        play2_panel.top()
        curses.panel.update_panels()
        STDSCR.noutrefresh(); curses.doupdate()

        event = STDSCR.getch()
        while event == 263:
          event = STDSCR.getch()
        event_lower = chr(event).lower()

        if event_lower == 'e' or event_lower == 'm' or event_lower == 'h':

          #title_panel.hide()
          menu_panel.hide()
          play1_panel.hide()
          play2_panel.hide()

          # Start the game
          if event_lower == 'e':
              diffc = "easy"
          elif event_lower == 'm':
              diffc = "medium"
          elif event_lower == 'h':
              diffc = "hard"

          main_rc = 1
          break

        # reset
        elif event_lower.lower() == 'r':
          main_rc = 4
          break

    #  stat/startGame(1) or reset(4) -> go to main screen
    if main_rc == 1 or main_rc == 4:
      break

  return main_rc


def userstats():
  stat_win = curses.newwin(30, 10, 10, 15)
  stat_win.addstr(5,6,"This is userstats window")
  stat_win.box()
  score_formatline = []

  stat_win.addstr(6,6,"user name: ")
  stat_win.addstr(7,6,"level#: ")
  stat_win.addstr(8,6,"score#: ")

def checkReq():
  """
  checks whether the game screen fits the user screen size
  If user screen is smaller than required size, print error message until they
  meet the requirments
  :return: None
  """
  global MAX_Y, MAX_X
  MAX_Y = curses.LINES - 1
  MAX_X = curses.COLS - 1
  if MAX_Y < REQ_Y:
    printError("Resize your window. " +
               "Current: " + str(MAX_X) + " X " + str(MAX_Y) + ". "
               "Required: " + str(REQ_X) + " X " + str(REQ_Y) )


def printError(msg):
  """
  prints the given error message
  on the user screen
  :param msg: str - The error message that is given to the function
  :return: None
  """
  errMsg_x = 3
  errMsg_y = 1
  STDSCR.addstr(errMsg_y, errMsg_x, "ERROR:" + msg + "\n\n...Terminating...press Enter...")
  STDSCR.refresh()
  STDSCR.getch()
  curses.endwin()
  #exit program
  sys.exit()


###############################################################################
# START
###############################################################################
curses.wrapper(main)
