import sys
import curses
import curses.panel
import threading
from random import randint

# ------------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------------
IS_DEBUG = False
WORD_START_PAUSE = 0.2   # Initial word speed. Lower is Faster
DATA_FILE = "data.dat"
ENG_FILE = "words.dat"
PY_FILE = "python.dat"
GO_NEXT = False
LEVEL = 1
USER_ENT = ""
ENTER_Y_OFFSET = 5
EXIT_GAME = False
WORDS_GOALS = 1

EXC_Y = 20
GOOD_Y = 30
AVG_Y = 40
MISS_Y = 0

EXC_COUNT = 0
GOOD_COUNT = 0
AVG_COUNT = 0
MISS_COUNT = 0

ACCU_SCORE = 0   # overall score
BEST_SCORE_PER_ROUND = 0
BEST_COMBO_PER_ROUND = 0
HIT_PER_ROUND = 0
MISS_PER_ROUND = 0
ACCU_HIT_PER_ROUND = 0
ACCU_MISS_PER_ROUND = 0

MAX_Y = 0            # current screen Y
MAX_X = 0            # current screen X
REQ_Y = 40           # required screen size Y
REQ_X = 40          # required screen size X

STDSCR = ""

THREAD_OBJ = ""
is_word_down_thread_stop = False    # True: Stop falling words.
                                    # False: Start falling words

NEW_WORD_FREQ = 10  # lower, sooner
ENG_WORDS = []
ENG_WORDS_LEN = 0
PY_WORDS = []
PY_WORDS_LEN = 0

# ------------------------------------------------------------------------------
# class Word
# ------------------------------------------------------------------------------
# Create a word object placed in a panel

class Word(object):
  """
  Representation of words
  """
  def __init__(self, diffc="hard", ptype="coding"):
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
          min_word_len = 3
          max_word_len = 4
        elif diffc == "medium":
          min_word_len = 5
          max_word_len = 20

        # Create a word
        word = ENG_WORDS[randint(0, ENG_WORDS_LEN - 1)].strip()
        while len(word) > max_word_len or len(word) < min_word_len :
          word = ENG_WORDS[randint(0, ENG_WORDS_LEN-1)].strip()
      # Hard
      else:
        max_word_len = 7
        for dummy in range(max_word_len):
          ch = chr(randint(ord('!'), ord('~')))
          word += ch
    # Coding
    else:
      max_word_len = 0
      # Easy or medium
      if diffc == "easy":
        min_word_len = 3
        max_word_len = 5
      elif diffc == "medium":
        min_word_len = 5
        max_word_len = 10
      # Hard
      else:
        min_word_len = 5
        max_word_len = 30

      # Create a word
      word = PY_WORDS[randint(0, PY_WORDS_LEN-1)].strip()
      while len(word) > max_word_len  or  len(word) < min_word_len :
        word = PY_WORDS[randint(0, PY_WORDS_LEN-1)].strip()

    x_offset_left = 10
    x = randint(x_offset_left, MAX_X - len(word)- 5)
    y = 6
                      # H  L   Y, X
    win = curses.newwin(2, len(word), y, x)
    win.addstr(0, 0, word, curses.color_pair(randint(1, 6)))

    self.word = word
    self.x = x
    self.y = y
    self.win = win
    self.panel = curses.panel.new_panel(win)
    self.panel.bottom()


  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def moveDown(self):
    # y, x
    self.panel.move(self.y, self.x)
    curses.panel.update_panels()
    self.win.noutrefresh(); curses.doupdate()
    self.y += 1

  def delWord(self):
    self.panel.hide()
    curses.panel.update_panels(); STDSCR.refresh()

#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main(stdscr):
  """
  set up for the game to start and runs by calling the main page
  :param stdscr: window - standard window screen
  :return: None
  """

  #make colours
  curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
  curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
  curses.init_pair(3,curses.COLOR_YELLOW,curses.COLOR_BLACK)
  curses.init_pair(4,curses.COLOR_WHITE,curses.COLOR_BLACK)
  curses.init_pair(5,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
  curses.init_pair(6,curses.COLOR_CYAN,curses.COLOR_BLACK)
  curses.init_pair(7,curses.COLOR_BLUE,curses.COLOR_BLACK)

  global EXIT_GAME

  #mouse cursor
  curses.curs_set(0)

  # Set up for debug
  global STDSCR
  STDSCR = stdscr

  # Check the required window size
  checkReq()

  # clear and draw coordinates
  if IS_DEBUG:
    drawCoor()

  # read word files
  readPhyWord()
  readEngWord()

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
  # debug
  if IS_DEBUG:
    drawCoor()

  # Draw Title
  title1 = r'TTTTT\ EEEEE\ X   X\ TTTTT\      BBBB\  L\       A    SSSSS\ TTTTT\ EEEEE\ RRRR   '
  title2 = r'\\T\\\ E\\\\\  X X\  \\T\\\      B\\\B\ L\      A\A   S\\\\\ \\T\\\ E\\\\\ R\\\R\ '
  title3 = r'  T\   EEEEE\   X\     T\        BBBB\\ L\     AAAAA  SSSSS\   T\   EEEEE\ RRRR\\ '
  title4 = r'  T\   E\\\\\  X\X     T\        B\\\B\ L\     A\  A\ \\\\S\   T\   E\\\\\ R\ R\  '
  title5 = r'  T\   EEEEE\ X\  X\   T\        BBBB\\ LLLLL\ A\  A\ SSSSS\   T\   EEEEE\ R\  R\ '
  title6 = r'  \\   \\\\\\ \\  \\   \\        \\\\\  \\\\\\ \\  \\ \\\\\\   \\   \\\\\\ \\  \\ '

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

  # word falling down in the background
  global THREAD_OBJ
  global is_word_down_thread_stop

  is_word_down_thread_stop = False
  THREAD_OBJ = threading.Thread(target=start_fall_word, args=[0.06, True, "hard", "coding"])
  THREAD_OBJ.daemon = True
  THREAD_OBJ.start()

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
      #statsScreen
      main_rc = 1
      statScreen()

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

          stop_thread()
          title_panel.hide()
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
          gameScreen(WORD_START_PAUSE, diffc, ptype)
          break

        # reset
        elif event_lower.lower() == 'r':
          stop_thread()
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

    global THREAD_OBJ, is_word_down_thread_stop
    global EXIT_GAME
    is_word_down_thread_stop = False
    #make another thread
    THREAD_OBJ = threading.Thread(target=start_fall_word, args=[pauseSec, False, diffc, ptype])
    #exit whenever i want
    THREAD_OBJ.daemon = True
    THREAD_OBJ.start()
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
          stop_thread()
          # Go back to main screen
          break

      else:
        if event != 10 and event != 263:  # enter and backspace
          saved += chr(event)

        if event == 263:  # backspace
          saved = saved[:-1]

        msg = " " * len(msg)
        enter_win.addstr(0,0,msg)
        STDSCR.addstr(4,135,"Press tab to exit and ESC to reset")

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
          stop_thread()
          EXIT_GAME = True

        if event == 27: #esc
          #wait for input
          STDSCR.timeout(-1)
          stop_thread()
          break

    if GO_NEXT:
      STDSCR.addstr(5,20,"****** Completed ********")
      showCurrentScoreScreen()
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

def statScreen():
  stop_thread()
  ofile = open(DATA_FILE, "r")

  length = 75
  stat_win = curses.newwin(30, length, 10, MAX_X/2 - length/2)
  score_formatline = {}
  for line in ofile:

    # remove white spaces
    line = line.strip()
    # remove [ ]
    line = line.lstrip('[')
    line = line.rstrip(']')

    user = ""
    level = ""
    score = ""
    hit = ""
    miss = ""
    acc = ""

    #1    2       3      4     5    6
    #split by comma
    user, level, score, hit, miss, acc = line.split(',')
    user = user.strip("'")
    level = level.strip()
    score = score.strip()
    hit = hit.strip()
    miss = miss.strip()
    acc = acc.strip()

    formatline = '{0:20} {1:5} {2:8} {3:8} {4:8} {5:8}'.format(
                    user,level,score,hit,miss,acc+"%")

    if int(score) in score_formatline:
      score_formatline[int(score)].append(formatline)
    else:
      score_formatline[int(score)] = [ formatline ]

  rank = 1
  # display only top 10
  scores = list(score_formatline.keys())
  scores.sort()
  scores.reverse()

  formatline = 'Best Top 10 users'
  stat_win.addstr(rank -1-1-1-1 + 10 ,5,formatline,curses.A_BOLD)

  formatline = '{0:20} {1:5} {2:8} {3:8} {4:8} {5:8}'.format(
                  "Name","Level","Score","Hit","Miss","Accuracy")
  stat_win.addstr(rank -1-1 + 10 ,5,formatline)
  formatline = '{0:20} {1:5} {2:8} {3:8} {4:8} {5:8}'.format(
                "-"*20,"-"*5,"-"*8,"-"*8,"-"*8,"-"*8)
  stat_win.addstr(rank -1 + 10 ,5,formatline,curses.A_BOLD)

  for score in scores:
  # top comes first
    for line in score_formatline[score]:
      if rank >= 11:
        break
      stat_win.addstr(rank + 10 ,5,line,curses.A_BOLD)
      rank += 1

    if rank >= 11:
      break

  ofile.close()
  test_pan = curses.panel.new_panel(stat_win)
  test_pan.top()
  curses.panel.update_panels()
  STDSCR.noutrefresh(); curses.doupdate()


#------------------------------------------------------------------------------
# Show Current Score screen
#  - show after each game
#------------------------------------------------------------------------------

def showCurrentScoreScreen():
  STDSCR.clear()
  STDSCR.refresh()
  if IS_DEBUG:
    drawCoor()
  global LEVEL

  l = 20
  w = 50
  x = 3
  y = 3

  if (HIT_PER_ROUND + MISS_PER_ROUND)  == 0:
    accuracy = 0
  else:
    accuracy = (float(HIT_PER_ROUND)/ (HIT_PER_ROUND + MISS_PER_ROUND)) * 100

  accuracy = float("{0:.2f}".format(accuracy))
  goal_win = curses.newwin(l, w, y, x)
  goal_win.addstr(1,1, "LEVEL: " +  str(LEVEL))
  goal_win.addstr(2,1, "SCORE: " +  str(ACCU_SCORE))
  goal_win.addstr(3,1, "HIT: "   +  str(HIT_PER_ROUND))
  goal_win.addstr(4,1, "MISS: "  +  str(MISS_PER_ROUND))
  goal_win.addstr(5,1, "Accuracy: "  +  str(accuracy) + "%")
  goal_win.addstr(6,1, "Excellent "  +  str(EXC_COUNT))
  goal_win.addstr(7,1, "Good:     "  +  str(GOOD_COUNT))
  goal_win.addstr(8,1, "Average:  "  +  str(AVG_COUNT))

  goal_pan = curses.panel.new_panel(goal_win)
  curses.panel.update_panels()
  goal_win.noutrefresh();curses.doupdate()
  goal_pan.hide()
  LEVEL += 1

  accuracy = float("{0:.2f}".format(accuracy))

  win1 = curses.newwin(30,30, 5, 5)
  win1.addstr(1,1,"Game over")
  win1.addstr(2,1, "BEST LEVEL: " +  str(LEVEL))
  win1.addstr(3,1, "TOTAL SCORE: " +  str(ACCU_SCORE))
  win1.addstr(4,1, "HIT: " + str(ACCU_HIT_PER_ROUND))
  win1.addstr(5,1, "MISS: " + str(ACCU_MISS_PER_ROUND))
  win1.addstr(6,1, "OVERALL Accuracy: " + str(accuracy) + "%")

  win1.noutrefresh(); curses.doupdate()
  goal_pan = curses.panel.new_panel(win1)

  curses.echo()
  msg = "Enter your name: "
  STDSCR.addstr(19, 20,msg)
  STDSCR.addstr(19, 20 + len(msg),"__________________")
  uinput = STDSCR.getstr(19, 20 + len(msg), 20)
  # save to the file
  if uinput != "":
    to_save = []
    to_save.append(str(uinput.decode('ascii')))
    to_save.append(LEVEL)
    to_save.append(ACCU_SCORE)
    to_save.append(ACCU_HIT_PER_ROUND)
    to_save.append(ACCU_MISS_PER_ROUND)
    to_save.append(accuracy)
    mfile = open(DATA_FILE,"a")
    mfile.write(str(to_save)+"\n")
    mfile.close()

  curses.noecho()

# ------------------------------------------------------------------------------
# Draw goal
# ------------------------------------------------------------------------------
def drawGoal(current, goal):
  goal_win = curses.newwin(3,18, 3, 90)
  goal_win.addstr(1,2,"CURRENT: " + str(current) + "/" +str(goal))
  goal_win.box()

  goal_pan = curses.panel.new_panel(goal_win)
  curses.panel.update_panels()
  goal_win.noutrefresh();curses.doupdate()
  return goal_pan

# ------------------------------------------------------------------------------
# Draw life bar
# ------------------------------------------------------------------------------

def drawLife(lose):
  left = True

  life_win = curses.newwin(MAX_Y-3 ,3, 3, 3)

  lose_weight = 1
  if lose_weight * lose > MAX_Y-3:
    left = False
  for y in range(lose_weight * lose, MAX_Y-3):
    life_win.addch(y, 1, ord('='))
  life_win.box()

  life_pan = curses.panel.new_panel(life_win)
  life_pan.top()
  curses.panel.update_panels()
  life_win.noutrefresh();curses.doupdate()

  return life_pan, left

#------------------------------------------------------------------------------
# Draw score
#------------------------------------------------------------------------------
def drawScore(score = 0):

  # Create a score window/panel
  l = 3
  w = 50
  score_win = curses.newwin(l,w,3,10)
  score_win.addstr(1,2,"SCORE: " + str(score) + " TOTAL: " +str(ACCU_SCORE))
  score_win.box()
  score_pan = curses.panel.new_panel(score_win)
  curses.panel.update_panels()
  score_win.noutrefresh();curses.doupdate()
  return score_pan

#------------------------------------------------------------------------------
# Draw combos
#------------------------------------------------------------------------------
def drawCombo(combo , score ):
  """
  draws combo panel on the screen
  to show combo score of the user
  :param combo: int - amount of combos
  :param score: int - score of the user
  :return: panel - the panel that contains the combo scores
  """
  # Create a combo window/panel
  l = 3
  w = 22
  combo_win = curses.newwin(l, w,3,61)
  combo_win.addstr(1,2, "COMBO: " + str(combo) + " ( +"+ str(score) + ")")
  combo_win.box()
  combo_pan = curses.panel.new_panel(combo_win)
  combo_pan.top()
  curses.panel.update_panels()
  combo_win.noutrefresh();curses.doupdate()
  return combo_pan


###############################################################################
#
# MISC.
#
###############################################################################
# -------------------------------------------------------------------
# start fall word
# -------------------------------------------------------------------
def start_fall_word(pauseSec, is_demo, diffc, ptype):
  # Create a combo window/panel
  combo_win = curses.newwin(10,10,5,5)
  combo_pan = curses.panel.new_panel(combo_win)
  combo_pan.hide()

  #  init
  global ACCU_SCORE
  global EXIT_GAME
  global GO_NEXT
  global HIT_PER_ROUND, MISS_PER_ROUND, LEVEL, ACCU_HIT_PER_ROUND, ACCU_MISS_PER_ROUND
  global EXC_COUNT, GOOD_COUNT, AVG_COUNT, MISS_COUNT
  EXC_COUNT = 0
  GOOD_COUNT = 0
  AVG_COUNT = 0
  MISS_COUNT = 0
  MISS_PER_ROUND = 0
  HIT_PER_ROUND = 0
  GO_NEXT = False
  comboTimerCount = 1
  showCombo = False
  new_word_interval = 0
  combo_count = 0
  lastSaved = ""
  lose_count = 0
  score_count = 0
  dummyCombo = ""
  word_wordObj = {}
  count_worddown = 0
  words_current = 0

  # Score and line
  if not is_demo:
    STDSCR.hline(EXC_Y, 0,'-',MAX_X)
    STDSCR.hline(GOOD_Y,0,'-',MAX_X)
    STDSCR.hline(AVG_Y, 0,'-',MAX_X)
    STDSCR.hline(MISS_Y,0,'-',MAX_X)

    STDSCR.addstr(EXC_Y, 6, " Excellent ")
    STDSCR.addstr(GOOD_Y,6, " Good ")
    STDSCR.addstr(AVG_Y, 6, " Average ")
    STDSCR.addstr(MISS_Y,6, " Miss ")

    dummyScore = drawScore(0)
    dummy,is_life_left = drawLife(lose_count)
    dummyGoal = drawGoal(words_current, WORDS_GOALS)

  while not is_word_down_thread_stop:
    #
    # Words falling down
    #
    if getPauseSec(count_worddown, pauseSec):
      # how often create a new word?
      if new_word_interval % NEW_WORD_FREQ  == 0:
        wordObj = Word(diffc, ptype)
        word_wordObj[wordObj.word] = wordObj
        new_word_interval = 0

      # move down each words
      words = word_wordObj.copy()
      for word in words:
        wordObj = word_wordObj[word]

        # Y boundary
        if wordObj.getY() >= MISS_Y:
          MISS_COUNT += 1
          del word_wordObj[word]
          wordObj.delWord()
          lose_count += 1
          #draw life bar
          if not is_demo:
            dummy,is_life_left = drawLife(lose_count)
            #exit if there's no life
            if not is_life_left:
              EXIT_GAME = True
        else:
          wordObj.moveDown()

      new_word_interval += 1
      count_worddown = 0

    if not is_demo:
      #
      # Check what a user types
      #
      if lastSaved != USER_ENT:
        # Score!
        if word_wordObj.get(USER_ENT):
          #word_wordObj - dictionary type
          # value - object made through Word class
          # key - word str
          wordObj = word_wordObj[USER_ENT]
          if wordObj.getY() < EXC_Y:
            EXC_COUNT += 1
          elif wordObj.getY() < GOOD_Y:
            GOOD_COUNT += 1
          else:
            AVG_COUNT += 1

          combo_count += 1
          score_count += 1
          wordObj.delWord()
          words_current += 1
          HIT_PER_ROUND += 1
          ACCU_HIT_PER_ROUND += 1

          dummyGoal = drawGoal(words_current, WORDS_GOALS)
          # completed the goal. Go to the next level
          if words_current >= WORDS_GOALS:
            GO_NEXT = True

          del word_wordObj[USER_ENT]

          # show combo and score
          bonus = 13 * combo_count
          cu_score = 300 * score_count  + bonus

          ACCU_SCORE += cu_score

          if showCombo:
            dummyCombo.hide()
          dummyScore = drawScore(cu_score)
          dummyCombo = drawCombo(combo_count, bonus)
          comboTimerCount = 0
          showCombo = True

        # Incorrect!
        else:
          MISS_PER_ROUND += 1
          ACCU_MISS_PER_ROUND += 1
          combo_count = 0

        lastSaved = USER_ENT


      # Duration of combo box

      if showCombo:
        comboTimerCount += 1
        STDSCR.addstr(40,5,str(comboTimerCount))
        if getPauseSec(comboTimerCount, 0.3):
          STDSCR.refresh()
          dummyCombo.hide()
          comboTimerCount = 0
          showCombo = False

    count_worddown += 1

#------------------------------------------------------------------------------
# stop thread
#------------------------------------------------------------------------------
def stop_thread():
  """
  stops thread on the screen
  :return: None
  """
  global is_word_down_thread_stop
  is_word_down_thread_stop = True
  # wait untill THREAD_OBJ stops
  while THREAD_OBJ.isAlive():
    pass
  is_word_down_thread_stop = False


#------------------------------------------------------------------------------
# get pause sec
#------------------------------------------------------------------------------
def getPauseSec(count, sec):
  """
  divide count by sec and check if the remainder is 0
  :param count: int - count
  :param sec: int - sec
  :return: boolean - remainder is 0
  """

  if count < 1:
    count = 1

  weight = 5000000
  msum = count % (weight * sec)
  return msum == 0

def slow():
  for i in range(1,999999/2):
    pass
  for i in range(1,999999):
    pass


# ------------------------------------------------------------------------------
# Draw coordinates
# ------------------------------------------------------------------------------
def drawCoor():
  STDSCR.clear()
  #draw line 0 - off 1 - on
  STDSCR.border(0)
  STDSCR.refresh()
  for x in range(MAX_X):
    STDSCR.addstr(2,x, str(x%10))
    if x % 10 == 0:
      STDSCR.addstr(1,x, str(x//10))

  for y in range(MAX_Y):
    STDSCR.addstr(y,2, str(y%10))
    if (y % 10 == 0):
      STDSCR.addstr(y,1, str(y//10))

  STDSCR.refresh()

# ------------------------------------------------------------------------------
# Read English words
# ------------------------------------------------------------------------------
def readEngWord():
  global ENG_WORDS
  global ENG_WORDS_LEN
  mfile = open(ENG_FILE,"r")
  ENG_WORDS = mfile.readlines()
  ENG_WORDS_LEN = len(ENG_WORDS)

# ------------------------------------------------------------------------------
# Read Python commands
# ------------------------------------------------------------------------------
def readPhyWord():
  global PY_WORDS
  global PY_WORDS_LEN
  #read files
  mfile = open(PY_FILE,"r")
  PY_WORDS = mfile.readlines()
  PY_WORDS_LEN = len(PY_WORDS)

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
# START
###############################################################################
curses.wrapper(main)
