from threading import Thread
from hal import hal_keypad as keypad
from hal import hal_lcd as LCD
import led_control # this is added



lcd = LCD.lcd()
lcd.lcd_clear()

#Call back function invoked when any key on keypad is pressed
def key_pressed(key):
    k = key

    if k == 1:
        # REQ-02: LED blinks every 1 second and LCD updates
        led_control.delay = 1
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1) # Line 1
        lcd.lcd_display_string("Blink LED", 2) # Line 2

    elif k == 0:
        # REQ-03: LED turns OFF, stops blinking, and LCD updates
        led_control.delay = 0
        lcd.lcd_clear()
        lcd.lcd_display_string("LED Control", 1) #Line 1
        lcd.lcd_display_string("OFF LED", 2) # LIne 2
    else:
        # REQ-04: Any other key does not change LED or LCD
        pass

  


def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Display something on LCD
    #REQ-01
    lcd.lcd_display_string("LED Control", 1) # Line 1
    lcd.lcd_display_string("0:Off 1:Blink", 2) # Line 2

    # Initialize the HAL keypad driver
    keypad.init(key_pressed)

    # Start the keypad scanning which will run forever in an infinite while(True) loop in a new Thread "keypad_thread"
    keypad_thread = Thread(target=keypad.get_key)
    keypad_thread.start()
    led_control.led_control_init() #this is added btw


# Main entry point
if __name__ == "__main__":
    main()
