# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# https://gist.githubusercontent.com/sanchitgangwar/2158089/raw/5f3d0003801acfe1a29c4b24f2c8975efacf6f66/snake.py

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from curses.textpad import Textbox, rectangle
from random import randint
import time
import threading

ent = ""
test_val = 1
SCR_Y_MAX = 40
SCR_X_MAX = 60

# color setting
#

#0:black, 1:red, 2:green, 3:yellow, 4:blue, 5:magenta, 6:cyan, and 7:white. The curses module defines named constants for each of these colors: curses.COLOR_BLACK, curses.COLOR_RED, and so forth.
#                         f             b

#stdscr = curses.initscr()

def drawCoor(scr):
  scr_y = curses.LINES - 1
  scr_x = curses.COLS - 1
  for x in range(scr_x):
    scr.addstr(3,x, str(x%10))
    if (x % 10 == 0):
      scr.addstr(2,x, str(x//10))

  x = 0
  for y in range(scr_y):
    scr.addstr(y,2, str(y%10))
    if (y % 10 == 0):
      scr.addstr(y,1, str(y//10))




def main(stdscr):

  curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLUE )

  #curses.noecho()
  #curses.curs_set(0)
  #stdscr.clear()
  #stdscr.resize(50, 50)
  #stdscr.border(0)
  #x=input("...waiting..")
  #curses.endwin()

  stdscr.border(0)
  stdscr.refresh()

  stdscr_y = curses.LINES - 1
  stdscr_x = curses.COLS - 1

  drawCoor(stdscr)

  pad = curses.newpad(20, 20)
  pad2 = curses.newpad(20, 20)


  for y in range(0, 19):
    for x in range(0, 19):
      pad.addch(y,x, ord('a') + (x*x+y*y) % 26)

  for y in range(0, 19):
    for x in range(0, 19):
      pad2.addch(y,x, ord('-'))

  pad.border(0)
  pad2.border(0)

  pad2.refresh(0,0, 15,5, 65,30)
  pad.refresh(0,0, 5,15, 30,40)
  stdscr.refresh()

  stdscr.addstr(15, 50,"Pretty text", curses.color_pair(2))
  stdscr.addstr(10, 50, "Current mode: Typing mode", curses.A_REVERSE)
  stdscr.addstr(10, 50, "HELLO")
  stdscr.refresh()


  stdscr.addstr(50, 50, "Enter IM message: (hit Ctrl-G to send)")


  rectangle(stdscr, 40,80, 60, 100)
  stdscr.refresh()

  ## Let the user edit until Ctrl-G is struck.
  editwin = curses.newwin(10,10, 50,90) # height, width, begin_y, begin_x
  stdscr.refresh()
  box = Textbox(editwin)
  box.edit()


curses.wrapper(main)
