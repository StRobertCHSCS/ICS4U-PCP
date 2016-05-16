# SNAKES GAME
# Use ARROW KEYS to play, SPACE BAR for pausing/resuming and Esc Key for exiting
# https://gist.githubusercontent.com/sanchitgangwar/2158089/raw/5f3d0003801acfe1a29c4b24f2c8975efacf6f66/snake.py

import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
import time
import threading

ent = ""
test_val = 1
SCR_Y_MAX = 40
SCR_X_MAX = 60

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
  win.addstr(y, 1, empty)

def debug(msg, level):
  """ (str, int, int) -> None
  """
  y = SCR_Y_MAX - 10 + level
  clear_line(y)
  #win.addstr(y, 1, 'DEBUG: '+msg)

def move_down(screen, word):
  if word == None:
    return
  empty = " " * len(word[2])
  screen.addstr(word[0], word[1], empty)
  word[0] += 1
  screen.addstr(word[0], word[1], word[2])

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
      screen.addstr(12, 12, 'testval:'+str(test_val));
      move_down(screen, word)
      #screen.addstr(12, 12, time.strftime("%a, %d %b %Y %H:%M:%S"))
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
#choice = my_raw_input(stdscr, 2, 3, "cool or hot?").lower()
#print("CHOICE: " +str(choice))
#choice = my_raw_input(stdscr, 2, 3, "cool or hot?").lower()

#win = curses.newwin(SCR_Y_MAX, SCR_X_MAX, 0, 0)

#win.keypad(1)
#curses.noecho()
#curses.curs_set(0)
#win.border(0)


#key = KEY_RIGHT                                                    # Initializing values
#curses.delay_output(1000)
#curses.echo()

new_word = create_work()
#win.border(0)

#---------------------------------------
#win = curses.newwin(10,10,0,0)
#win.border(0)
#win.addstr(0,0,'hELLo')
#win.refresh()
#---------------------------------------


# pad ----------------------------------------
#pad = curses.newpad(100, 100)
##  These loops fill the pad with letters; this is
## explained in the next section
#for y in range(0, 100):
#    for x in range(0, 100):
#        try:
#            pad.addch(y,x, ord('a') + (x*x+y*y) % 26)
#        except curses.error:
#            pass

#  Displays a section of the pad in the middle of the screen
#pad.refresh(0,0, 5,5, 20,75)
#win.getch()

#win2 = curses.newwin(5,5,41,00)
#
#while key != 27:
#    win2.border(0)
#    win2.refresh()
#
#    win.border(0)
#    win.refresh()
#    #win.timeout(500)
#    #prevKey = key
#    #win.getch()
#
#    ## no key is pressed
#    #if event == -1:
#    #    key = key
#    #else:
#    #    key = event
#
#    #debug('key: ' + str(key) + ' ' +
#    #      'chr(' + str(key) + '): ' + str(chr(key)), 1)
#    move_down(new_word)
#    time.sleep(0.5)
#    #choice = my_raw_input(stdscr, 2, 3, "cool or hot?").lower()
#    #print("CHOICE: " +str(choice))

clock = threading.Thread(target=create_word, args=(stdscr,new_word))
clock.daemon = True
clock.start()
saved =""
while 1:
    #time.sleep(1)
    #new_word = create_work()
    #clock2 = threading.Thread(target=create_word, args=(stdscr,new_word))
    #clock2.daemon = True
    #clock2.start()

    #time.sleep(1)
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



curses.endwin()
#print("\nScore - " + str(score))
print("http://bitemelater.in\n")
