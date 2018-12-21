#!/usr/bin/python3

import time
import lcd_i2c
import board
import busio
import adafruit_bme280
#from datetime import datetime


def main():
    # Main program block

    # Initialise display
    lcd_init()

    while True:
        temp = bme280.temperature
        humidity = bme280.humidity

        # Send to LCD
        lcd_string("Temperature: "+temp+" C", LCD_LINE_1)
        lcd_string("Humidity: "+humidity+" %", LCD_LINE_2)

        time.sleep(3)

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    lcd_byte(0x01, LCD_CMD)

