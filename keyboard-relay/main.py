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

FLOW_SENSOR = 21

global count
count = 0
global countsPer100Ml
countsPer100Ml = 570

global pourMl
pourMl = None

def countPulse(channel):
    global count
    count = count+1
    #print count


GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=countPulse)


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

        y+=2
        stdscr.addstr(y, 0, "'r' resets flow sensor and ml to pour, 'a' manual mode, 's'  pours 50ml, 'd' pours 100ml, 'f' pours 200ml",
                      curses.A_REVERSE)
        y+=1
        global count
        global pourMl
        pouredMl = count / float(countsPer100Ml) * 100
        stdscr.addstr(y, 0, "Flowsensor count {0}, ml : {1:.2f}".format(count,pouredMl))
        stdscr.clrtoeol()
        y+=1
        if pourMl is not None:
            stdscr.addstr(y, 0, "Pour ml: {0}".format(pourMl))
            stdscr.clrtoeol()
            if pouredMl >= pourMl:
                relais[0].off()
        else:
            stdscr.addstr(y, 0, "Manual pouring")
            stdscr.clrtoeol()


        # get keyboard input, returns -1 if none available
        key = stdscr.getch()
        if (key == ord('1')):
            if relais[0].isOff():
                count = 0
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
        if key == ord('r'):
            count = 0
        if key == ord('a'):
            pourMl = None
        if key == ord('s'):
            pourMl = 50
        if key == ord('d'):
            pourMl = 100
        if key == ord('f'):
            pourMl = 200
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