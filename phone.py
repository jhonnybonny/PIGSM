import RPi.GPIO as GPIO

import time

# Установка режима нумерации GPIO
GPIO.setmode(GPIO.BCM)

# Установка пина GPIO 21 в режим OUTPUT
led_pin = 21
GPIO.setup(led_pin, GPIO.OUT)

try:
    # Выключение светодиода на 5 секунд
    GPIO.output(led_pin, GPIO.LOW)
    print("Power button clicked")
    time.sleep(1)
    GPIO.cleanup()

except KeyboardInterrupt:
    # Выход из программы при нажатии Ctrl+C
    pass

finally:
    # Сброс состояния пина GPIO
    GPIO.cleanup()
    print("GPIO cleanup")
    print("Exiting...")