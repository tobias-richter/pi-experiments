from pynput import keyboard
import time

def onKeyRelease(key): #what to do on key-release
    print("key release {0}".format(key))
    ti1 = time.time() - t
    ti1 = str(ti1) #converting float value to string
    ti2 = ti1[0:5] #cutting the seconds ( time ) , without it , it will print like 0.233446546
    print("The key",key,"Pressed For",ti2,'seconds')
    return False #stop detecting more key-releases
def onKeyPress(key): #what to do on key-press
    print("key down {0}".format(key))
    return False #stop detecting more key-presses

with keyboard.Listener(on_press = onKeyPress) as keyPressListener: #setting code for listening key-press
    keyPressListener.join()

t = time.time()

with keyboard.Listener(on_release = onKeyRelease) as keyReleaseListener: #setting code for listening key-release
    keyReleaseListener.join()