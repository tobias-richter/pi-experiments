import curses
from elements import Actor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 0, "Keyboard controlled relais (hit 'q' to exit)",
              curses.A_REVERSE)
stdscr.refresh()

relais1 = Actor('relay1', 17)
relais2 = Actor('relay2', 27)
relais3 = Actor('relay3', 22)
relais4 = Actor('relay4', 10)
relais5 = Actor('relay5', 9)
relais6 = Actor('relay6', 5)
relais7 = Actor('relay7', 6)
relais8 = Actor('relay8', 13)

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
            relais[0].toggle()
        if (key == ord('2')):
            relais[1].toggle()
        if (key == ord('3')):
            relais[2].toggle()
        if (key == ord('4')):
            relais[3].toggle()
        if (key == ord('5')):
            relais[4].toggle()
        if (key == ord('6')):
            relais[5].toggle()
        if (key == ord('7')):
            relais[6].toggle()
        if (key == ord('8')):
            relais[7].toggle()
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


for singleRelais in relais:
    singleRelais.off()

GPIO.cleanup()
print("exit")