from random import randint
import curses.panel
import time
from time import sleep
import sys
#import threading

# -------------------------------------------------------
# Global Varibles
# -------------------------------------------------------

IS_DEBUG = True
WORD_START_PAUSE = 0.2   # Initial word speed. Lower is Faster
ENTER_Y_OFFSET = 5
GO_NEXT = False
is_word_down_thread_stop = False
ENG_FILE = "words.dat"
PY_FILE = "python.dat"

MAX_Y = 0            # current screen Y
MAX_X = 0            # current screen X
REQ_Y = 55/2         # required screen size Y
REQ_X = 200/2        # required screen size X

ENG_WORDS = ["apple","hi","hello","aaron",""]
ENG_WORDS_LEN = 0
NEW_WORD_FREQ = 10  # lower, sooner
PY_WORDS = []
PY_WORDS_LEN = 0
STDSCR = ""
MIN_WORD_LEN = 0
MAX_WORD_LEN = 0
WORD = ""
word_down_thread = ""
is_demo = False

# ------------------------------------------------------------------------------
# class Word
# ------------------------------------------------------------------------------
# Create a word object placed in a panel


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

    y = 6
    x_offset_left = 10
    x = randint(x_offset_left, MAX_X - len(word)- 5)
    self.word = word
    self.x = x
    self.y = y

  def move_down(self,screen, word):
   self.panel.move(self.y, self.x)
   curses.panel.update_panels();
   self.win.noutrefresh(); curses.doupdate()
   self.y += 1

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
        #global test_val
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

  def getPanel(self):
    return self.panel

  def _eq__(self,other):
    return self.word == other.word

  def __str__(self):
    return self.word

  def delWord(self):
    self.panel.hide()
    curses.panel.update_panels(); STDSCR.refresh()

  # Debug
  def display(self):
    # y, x
    curses.panel.update_panels(); STDSCR.refresh()

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
  y = SCR_Y_MAX - 10 + level
  clear_line(y)
                                                 # Initializing value
saved =""


#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------

def main(stdscr):
  """
  set up for the game to start and runs by calling the main page
  :param stdscr: window - standard window screen
  :return: None
  """
  # make colors
  curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
  curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
  curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
  curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
  curses.init_pair(6,curses.COLOR_CYAN,curses.COLOR_BLACK)
  curses.init_pair(7,curses.COLOR_BLUE,curses.COLOR_BLACK)

  global EXIT_GAME
  global is_word_down_thread_stop

  # mouse cursor set - none
  curses.curs_set(0)

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
#------------------------------------------------------------------------------
# main Game screen
#------------------------------------------------------------------------------
def mainGameScreen():
  """
  makes the main screen of the game
  :return: int - assigned number of the each screen
  """
  STDSCR.clear()
  STDSCR.refresh()

  global word_down_thread, is_word_down_thread_stop
  global EXIT_NOW
  is_word_down_thread_stop = False
  # debug
  if IS_DEBUG:
    drawCoor()

  # Draw Title
  title1 = r'TTTTTT\ EEEEE\  X   X\ TTTTT\      BBBB\  L\       A    SSSSS\ TTTTT\ EEEEE\ RRRR   '
  title2 = r'\\T\\\  E\\\\\   X X\  \\T\\\      B\\\B\ L\      A\A   S\\\\\ \\T\\\ E\\\\\ R\\\R\ '
  title3 = r'  T\    EEEEE\    X\     T\        BBBB\\ L\     AAAAA  SSSSS\   T\   EEEEE\ RRRR\\ '
  title4 = r'  T\    E\\\\\   X\X     T\        B\\\B\ L\     A\  A\ \\\\S\   T\   E\\\\\ R\ R\  '
  title5 = r'  T\    EEEEE\  X\  X\   T\        BBBB\\ LLLLL\ A\  A\ SSSSS\   T\   EEEEE\ R\  R\ '
  title6 = r'  \\    \\\\\\  \\  \\   \\        \\\\\  \\\\\\ \\  \\ \\\\\\   \\   \\\\\\ \\  \\ '

  #                         h      l           y             x
  title_win = curses.newwin(9, len(title1)+4, 5, int(MAX_X/2 - len(title1)/2))
  title_win.addstr(0+1, 1+1, title1, curses.color_pair(1)|curses.A_BLINK)
  title_win.addstr(1+1, 1+1, title2, curses.color_pair(2)|curses.A_BLINK)
  title_win.addstr(2+1, 1+1, title3, curses.color_pair(3)|curses.A_BLINK)
  title_win.addstr(3+1, 1+1, title4, curses.color_pair(4)|curses.A_BLINK)
  title_win.addstr(4+1, 1+1, title5, curses.color_pair(5)|curses.A_BLINK)
  title_win.addstr(5+1, 1+1, title6, curses.color_pair(6)|curses.A_BLINK)

  title_panel = curses.panel.new_panel(title_win)
  title_panel.top();curses.panel.update_panels()

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
      title_panel.hide()
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

          title_panel.hide()
          menu_panel.hide()
          play1_panel.hide()
          play2_panel.hide()

          # Start the game
          if event_lower == 'e':
              diffc = "easy"
              start_fall_word(False)
          elif event_lower == 'm':
              diffc = "medium"
          elif event_lower == 'h':
              diffc = "hard"

          main_rc = 1
          gameScreen(WORD_START_PAUSE, diffc, ptype)
          break

        # reset
        elif event_lower.lower() == 'r':
          main_rc = 4
          break

    #  stat/startGame(1) or reset(4) -> go to main screen
    if main_rc == 1 or main_rc == 4:
      break

  return main_rc

#------------------------------------------------------------------------------
# game screen
#------------------------------------------------------------------------------
def gameScreen(pauseSec, diffc, ptype):
  """
  makes game screen on the user screen to run the game
  :param pauseSec: int - amount of pause seconds
  :param diffc: str - difficulty of the game
  :param ptype: str - user selected game type
  :return: None
  """
  while True:
    # 1 = every 1 sec, words are falling down
    STDSCR.clear()
    STDSCR.refresh()
    if IS_DEBUG:
      drawCoor()

    global EXIT_GAME
    saved = ""

    y_entered = MAX_Y - ENTER_Y_OFFSET
    x_entered = 10
    enter_win = curses.newwin(1, 80, y_entered, x_entered)  # l, w, y, x
    enter_panel = curses.panel.new_panel(enter_win)
    enter_panel.top()
    # Take an input from a user
    msg = ""
    while 1:
      STDSCR.timeout(100)
      event = STDSCR.getch()
      if event == -1:
        # EXIT_GAME is True when the life comes 0
        if EXIT_GAME or GO_NEXT:
          STDSCR.timeout(-1)
          # Go back to main screen
          break

      else:
        if event != 10 and event != 263:  # enter and backspace
          saved += chr(event)

        if event == 263:  # backspace
          saved = saved[:-1]

        msg = " " * len(msg)
        enter_win.addstr(0,0,msg)

        msg = "> " + str(saved)
        enter_win.addstr(0,0,msg)
        enter_win.noutrefresh()
        curses.doupdate()

        # enter
        if event == 10:
          global USER_ENT
          USER_ENT = saved
          saved = ""
          msg = " " * len(msg)
          enter_win.addstr(0,0,msg)
          enter_win.noutrefresh()
          curses.doupdate()

        if event == 9: #tab to exit
          STDSCR.timeout(-1)
          EXIT_GAME = True

        if event == 27: #esc
          #wait for input
          STDSCR.timeout(-1)
          break

    if GO_NEXT:
      STDSCR.addstr(5,20,"****** Completed ********")
      pauseSec = pauseSec /2

      #speed
      global NEW_WORD_FREQ
      NEW_WORD_FREQ = NEW_WORD_FREQ - 1
      if NEW_WORD_FREQ < 8:
        NEW_WORD_FREQ = 8

    if EXIT_GAME:
      break

# ------------------------------------------------------------------------------
# Stat Screen
# ------------------------------------------------------------------------------
def userstats():
  stat_win = curses.newwin(30, 10, 10, 15)
  stat_win.addstr(5,6,"This is userstats window")
  stat_win.box()
  score_formatline = []

  stat_win.addstr(6,6,"user name: ")
  stat_win.addstr(7,6,"level#: ")
  stat_win.addstr(8,6,"score#: ")


def start_fall_word(is_demo):
  count_worddown = 0
  word_wordObj = {}

  comboTimerCount = 1
  showCombo = False

  # Create a combo window/panel
  combo_win = curses.newwin(10,10,5,5)
  combo_pan = curses.panel.new_panel(combo_win)
  combo_pan.hide()

  #
  new_word_interval = 0
  combo_count = 0
  lastSaved = ""
  lose_count = 0
  score_count = 0

  dummyCombo = ""
  # Score
  if not is_demo:
    dummyScore = 0
    dummy = drawLife(lose_count)

  while not is_word_down_thread_stop:
    #
    # Words falling down
    if new_word_interval % NEW_WORD_FREQ  == 0:
      wordObj = Word("easy", "prac")
      word_wordObj[wordObj.word] = wordObj
      new_word_interval = 0

    # move down each words
    words = word_wordObj.copy()
    for word in words:
      wordObj = word_wordObj[word]

    # Y boundary
    if wordObj.getY() >= MAX_Y-3:
     del word_wordObj[word]
    wordObj.delWord("easy","prac")
    lose_count += 1
    if not is_demo:
      dummy = drawLife(lose_count)

    else:
      wordObj.moveDown()
      new_word_interval += 1
      count_worddown = 0

    if not is_demo:
      # Check what a user types
      if lastSaved != ent:
        if word_wordObj.get(ent):
          combo_count += 1
          score_count += 10
          word_wordObj[ent].remove_same(ent)
          del word_wordObj[ent]

          # show combo and score
          each_score = 300
          bonus = 13 * (combo_count)
          cu_score = 300 * score_count  + bonus

          showCombo = True
        # Miss!
        else:
          combo_count = 0

        lastSaved = ent


def eng_word():
  global ENG_WORDS
                     # OPEN FILE
  eng_file  = open(ENG_FILE,"r")
  ENG_WORDS = eng_file.readlines()


def py_word():
  global PY_WORDS
  py_file = open(PY_FILE,"r")
  PY_WORDS = py_file.readlines()

# ------------------------------------------------------------------------------
# Check requirements
# ------------------------------------------------------------------------------
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

# ------------------------------------------------------------------------------
# Print error message
# ------------------------------------------------------------------------------
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
#
# Draws
#
###############################################################################

# ------------------------------------------------------------------------------
# Draw life bar
# ------------------------------------------------------------------------------
def drawLife(lose):
  global EXIT_NOW

  life_win = curses.newwin(MAX_Y-3 ,3, 3, 3)

  if 1 * lose > MAX_Y-3:
    EXIT_NOW =True
  for y in range(1 * lose, MAX_Y-3):
    life_win.addch(y, 1, ord('='))
  life_win.box()

  life_pan = curses.panel.new_panel(life_win)
  life_pan.top();
  curses.panel.update_panels();
  life_win.noutrefresh();curses.doupdate()
  return life_pan

#------------------------------------------------------------------------------
# Draw combos
#------------------------------------------------------------------------------
def drawCombo(combo = 0, score = 0):
  # Create a combo window/panel
  l = 3
  w = 40
  #if LAST_COMBO != "":
  #  LAST_COMBO.hide()
  combo_win = curses.newwin(l, w,3,60)
  combo_win.addstr(1,2, "COMBO: " + str(combo) + " ( +"+ str(score) + ")")
  combo_win.box()
  combo_pan = curses.panel.new_panel(combo_win)
  combo_pan.top()
  curses.panel.update_panels();
  combo_win.noutrefresh();curses.doupdate()
  return combo_pan

###############################################################################
# START
###############################################################################
curses.wrapper(main)
