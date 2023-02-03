import Jetson.GPIO as GPIO
import time

# Pin Definitons:
led_pin = 12  # BOARD pin 12

def main():
    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    GPIO.setup(led_pin, GPIO.OUT)  # LED pin set as output
    
    print("Starting demo now! Press CTRL+C to exit")
    curr_value = GPIO.HIGH
    try:
        while True:
            time.sleep(1)
            # Toggle the output every second
            print("Outputting {} to pin {}".format(curr_value, led_pin))
            GPIO.output(led_pin, curr_value)
            curr_value ^= GPIO.HIGH
    finally:
        GPIO.cleanup()  # cleanup all GPIO

if __name__ == '__main__':
    main()