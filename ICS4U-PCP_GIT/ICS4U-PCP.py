# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# https://gist.githubusercontent.com/sanchitgangwar/2158089/raw/5f3d0003801acfe1a29c4b24f2c8975efacf6f66/snake.py

#below code needs to be fixed
#from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time
import curses.panel
import threading


# -------------------------------------------------------
# Global Varibles
# -------------------------------------------------------

MAX_Y = 0            # current screen Y
MAX_X = 0            # current screen X
REQ_Y = 0            # required screen size Y
REQ_X = 0            # required screen size X
ENG_WORDS = []
ENG_WORDS_LEN = 0
PY_WORDS = []
PY_WORDS_LEN = 0
STDSCR = ""

class Word(object):
  """
  Representation of words
  """
  def __init__(self, diffc, ptype):
    """
    selects a word according to user difficulty
    :param diffc: str - difficulty selected by user
    :param ptype: str - game type selected by user
    :return: None
    """
    word = ""

    # Practice
    if ptype == "prac":
      # Easy or medium
      if diffc == "easy" or diffc == "medium":
        max_word_len = 0
        if diffc == "easy":
          min_word_len = 2
          max_word_len = 5
        elif diffc == "medium":
          min_word_len = 10
          max_word_len = 15

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
  """ (int) -> None
  """
  empty = " " * SCR_X_MAX
  stdscr.addstr(y, 1, empty)

def debug(msg, level):
  """ (str, int, int) -> None
  """
  y = SCR_Y_MAX - 10 + level
  clear_line(y)
  #win.addstr(y, 1, 'DEBUG: '+msg)

def create_work():
  word_len = 4
  word = ""
  for ch_num in range(word_len):
    ch = chr(randint(ord('a'), ord('z')))
    word += ch
  x = randint(0, SCR_X_MAX)
  y_x_word = [ 0, x, word ]
  #debug("new word: "+str(y_x_word), 2)
  return y_x_word

def create_word(screen, word):
  while 1:
    #screen.border(0)
    global test_val
    global ent

    if word:
      screen.addstr(12, 12, 'testval:'+str(test_val))
      #Word.move_down(screen, word)
      screen.refresh()

      if ent == word[2]:
        global curses
        curses.beep()
        word = None
        word = create_work()
    time.sleep(0.5)

stdscr = curses.initscr()
curses.noecho()
curses.curs_set(0)
stdscr.clear()
#stdscr.resize(50, 50)
stdscr.border(0)
stdscr.refresh()

#key = KEY_RIGHT                                                    # Initializing values
new_word = create_work()
#win.border(0)

clock = threading.Thread(target=create_word, args=(stdscr,new_word))
clock.daemon = True
clock.start()
saved =""

def mainGameScreen():
  STDSCR.clear()
  STDSCR.refresh()
  drawCoor()

  menu1 = "P: PLAY"
  menu2 = "S: USER STATS"
  menu3 = "X: EXIT"
  menu_win = curses.newwin(11, 30  , 30, 78)
  menu_win.addstr(1, 1, menu1)
  menu_win.addstr(2, 1, menu2)
  menu_win.addstr(3, 1, menu3)
  menu_panel = curses.panel.new_panel(menu_win)
  menu_panel.top();curses.panel.update_panels()
  menu_win.noutrefresh(); curses.doupdate()

  menu_pan = curses.panel.new_panel(menu_win)
  menu_pan.top()
  curses.panel.update_panels()
  menu_win.noutrefresh()
  curses.doupdate()

  while 1:
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
    #if event == ord("q"):
    if event == 27:
        break

def main(stdscr):

  stdscr.border(0)
  stdscr.refresh()

  stdscr_y = curses.LINES - 1
  stdscr_x = curses.COLS - 1
  global STDSCR
  STDSCR = stdscr
  drawCoor()

  mainGameScreen()

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

curses.endwin()
curses.wrapper(main)

