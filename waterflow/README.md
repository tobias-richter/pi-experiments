# Waterflow Sensor

## Hardware:
* Raspberry PI 3B+
* Waterflow Sensor YF-S401

## Connections

* 5V DC (red) to PIN 02
* GND (black) to PIN 6
* SIGNAL (yellow) over 1K resistor to GPIO 27 (PIN 13)

## Run

```
sudo pyhton waterflow.py
```

Output will be a increasing number which are the "ticks" from the the hall sensor.