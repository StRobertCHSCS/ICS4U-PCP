import curses
from random import randint
from curses import wrapper
import time

stdscr = curses.initscr()
stdscr.clear()
stdscr.border(0)
stdscr.refresh()
print "hello"

def optimize_screen():
  """
  Check user's screen and send error mesage
  :return: bool
  """
  # get user's screen
  stdscr.refresh()
 # width = curses.COLS -1
 # length = curses.LINES -1

  length,width = stdscr.getmaxyx()

  # check the screen size,
  # if width or length is less than the rquired size, send error message

  REQ_W = 112
  REQ_L = 46

  if width < REQ_W or length < REQ_L:
    #debug
    stdscr.addstr(9,3,str(stdscr.getmaxyx()))
    stdscr.addstr(10,3,str(width) + " " + str(length))
    stdscr.addstr(20,45,"Please make your screen size"+str(REQ_W)+"x"
                  +str(REQ_L))
    stdscr.addstr(21,45,"Press spacebar to continue")

    test = stdscr.getch()


    return False

  return True


def coordinates(stdscr):
  first_point = 0
  end_point = curses.COLS -1
  tenth_coord = 0

  while first_point < end_point:
    if first_point % 10 == 0:
        stdscr.addstr(1,first_point,str(tenth_coord))
        tenth_coord += 1

    stdscr.addstr(2,first_point,str(first_point%10))
    first_point += 1

  first_point_2 = 0
  vertical_end_point = curses.LINES -1
  tenth_coord_2 = 0

  while first_point_2 < vertical_end_point:
    if first_point_2 % 10 == 0:
      stdscr.addstr(first_point_2,1,str(tenth_coord_2))
      tenth_coord_2 += 1


    stdscr.addstr(first_point_2,2,str(first_point_2%10))
    first_point_2 += 1


def main(stdscr):
  # check user's screen size
  is_small_screen = True
  while is_small_screen:
    #test
    is_small_screen =not optimize_screen()
    stdscr.addstr(7,2,str(is_small_screen))
    stdscr.getch()

  # make screen
  stdscr.clear()

  # debug only
  coordinates(stdscr)
  # load first page

  stdscr.getch()

  """
  while 1:
    event = stdscr.getch()
    stdscr.addstr(10,10,str(event))
    stdscr.addstr(12,10,chr(int(event)))
    stdscr.addstr(5,10,str("Press spacebar to continue!"))
    if event == 27:
      break

    coordinates(stdscr)
  """

  """
  if event == 32:
      first_screen(stdscr)
  """


def first_screen(stdscr):
  begin_x = 20; begin_y = 7
  height = 5; width = 40
  win = curses.newwin(height,width,begin_x,begin_y)
  stdscr.clear()
  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  stdscr.addstr("Pretty text", curses.color_pair(1))
  stdscr.refresh()
curses.endwin()


wrapper(main)
