import curses
from elements import Actor

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 0, "Keyboard controlled relais (hit 'q' to exit)",
              curses.A_REVERSE)
stdscr.refresh()

relais1 = Actor('relay1', 1)
relais2 = Actor('relay2', 1)
relais3 = Actor('relay3', 1)
relais4 = Actor('relay4', 1)
relais5 = Actor('relay5', 1)
relais6 = Actor('relay6', 1)
relais7 = Actor('relay7', 1)
relais8 = Actor('relay8', 1)

relais = [
    relais1,
    relais2,
    relais3,
    relais4,
    relais5,
    relais6,
    relais7,
    relais8
]

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)

    stdscr.refresh()

    while True:

        y = 2
        for singleRelais in relais:
            stdscr.addstr(y, 0, "{0}".format(singleRelais))
            y+=1
            stdscr.clrtoeol()


        # get keyboard input, returns -1 if none available
        key = stdscr.getch()
        if (key == ord('1')):
            relais1.toggle()
        if (key == ord('2')):
            relais2.toggle()
        if (key == ord('3')):
            relais3.toggle()
        if (key == ord('4')):
            relais4.toggle()
        if (key == ord('5')):
            relais5.toggle()
        if (key == ord('6')):
            relais6.toggle()
        if (key == ord('7')):
            relais7.toggle()
        if (key == ord('8')):
            relais8.toggle()
        if key == ord('q'):
            break
        #if c != -1:
            # print numeric value
         #   stdscr.addstr(str(c) + ' ')
          #  stdscr.refresh()
            # return curser to start position
           # stdscr.move(0, 0)

if __name__ == '__main__':
    curses.wrapper(main)