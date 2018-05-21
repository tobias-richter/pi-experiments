#import RPi.GPIO as GPIO


class Actor:
    """A simple gpio actor"""
    OFF = "off"
    ON = "on"
    _allowedStatus = [ON, OFF]
    _status = OFF
    _name = None
    _pinNumber = None

    def __init__(self,name,pinNumber):
        self._name = name
        self._pin = pinNumber

    def on(self):
        self._setStatus(Actor.ON)

    def off(self):
        self._setStatus(Actor.OFF)

    def toggle(self):
        if self.isOn():
            self._setStatus(Actor.OFF)
        elif self.isOff():
            self._setStatus(Actor.ON)
        else:
            raise ValueError("Invalid status: {0}".format(self._status))

    def isOn(self):
        return self._status == Actor.ON

    def isOff(self):
        return self._status == Actor.OFF

    def _setStatus(self, status):
        if status not in self._allowedStatus:
            raise ValueError("Invalid status: {0}".format(status))
        if status == Actor.ON and self.isOff():
            self._status = Actor.ON
            self._handleOn()
        elif status == Actor.OFF and self.isOn():
            self._status = Actor.OFF
            self._handleOff()

    def _handleOn(self):
        test = 1
        #print("{0} -> switched on".format(self))

    def _handleOff(self):
        test = 2
        #print("{0} -> switched off".format(self))

    def __str__(self):
        return '{0} (p: {1}) -> {2}'.format(self._name, self._pinNumber, self._status)

    def debug(self):
        print('name: {0}, pin: {1}, status: {2} '.format(self._name, self._pinNumber, self._status))