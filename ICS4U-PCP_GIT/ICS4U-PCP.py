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


class_test = Word.create_word                                                 # Initializing values
new_word = class_test(STDSCR,ENG_WORDS[randint(0,len(ENG_WORDS)-1)])

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

def mainScreen():
  STDSCR.clear()
  STDSCR.refresh()
  drawCoor()

  #Draw menu
  menu1 = "[P] PLAY"
  menu2 = "[S] USER STATS"
  menu3 = "[X] EXIT"
  menu_win = curses.newwin(11, 30  , 30, 78)
  menu_win.addstr(1, 1, menu1)
  menu_win.addstr(3, 1, menu2)
  menu_win.addstr(5, 1, menu3)
  menu_win.box()

  menu_panel = curses.panel.new_panel(menu_win)
  menu_panel.top();curses.panel.update_panels()
  menu_win.noutrefresh(); curses.doupdate()
  menu_pan = curses.panel.new_panel(menu_win)
  menu_pan.top()
  curses.panel.update_panels()
  menu_win.noutrefresh()
  curses.doupdate()

  #initialize
  main_screen_num = 0

  while True:
    event = STDSCR.getch()
    #event_low = event.lowwer()

    if event == 263:
      continue

    if chr(event) == "e":
      main_screen_num = 0
      break


def main(stdscr):
  stdscr.border(0)
  stdscr.refresh()

  global STDSCR
  STDSCR = stdscr
  drawCoor()
  #mainGameScreen()
  mainScreen()
  GamePlay()
  pad = curses.newpad(20, 20)
  pad2 = curses.newpad(20, 20)
  # These loops fill the pad with letters; addch() is
  # explained in the next section
  for y in range(0, 19):
    for x in range(0, 19):
      pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

  for y in range(0, 19):
    for x in range(0, 19):
      pad2.addch(y,x, ord('-'))

  pad.border(0)
  pad2.border(0)

  pad2.refresh(0,0, 15,5, 25,10)
  pad.refresh(0,0, 5,5, 10,10)

  stdscr.refresh()
  curses.noecho()

#curses.endwin()

def userstats():
  stat_win = curses.newwin(30, 10, 10, 15)
  stat_win.addstr(5,6,"This is userstats window")
  stat_win.box()
  score_formatline = []

  stat_win.addstr(6,6,"user name: ")
  stat_win.addstr(7,6,"level#: ")
  stat_win.addstr(8,6,"score#: ")



def printError(msg):
  errMsg_x = 3
  errMsg_y = 1
  STDSCR.addstr(errMsg_y, errMsg_x, "ERROR:" + msg)
  STDSCR.refresh()
  STDSCR.getch()
  curses.endwin()
  sys.exit()


###############################################################################
# START
###############################################################################
curses.wrapper(main)