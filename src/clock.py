import time
from threading import Thread
from hal import hal_lcd as LCD

def clock_thread():
    lcd = LCD.lcd()
    colon_toggle = True  # Used to alternate between ':' and ' ' for REQ-02

    while True:
        # Get current system time and date
        local_time = time.localtime()
        
        # Format date as "dd:mm:yyyy" (REQ-01)
        date_string = time.strftime("%d:%m:%Y", local_time)
        
        # Format time components individually to allow blinking colons (REQ-02)
        hours = time.strftime("%H", local_time)
        minutes = time.strftime("%M", local_time)
        seconds = time.strftime("%S", local_time)
        
        if colon_toggle:
            time_string = f"{hours}:{minutes}:{seconds}"
        else:
            time_string = f"{hours} {minutes} {seconds}"  # Space instead of colon
            
        # Toggle the colon state for the next second
        colon_toggle = not colon_toggle

        # Update LCD display
        lcd.lcd_clear()
        lcd.lcd_display_string(time_string, 1)  # Line 1 = hh:mm:ss (with blinking colons)[cite: 2]
        lcd.lcd_display_string(date_string, 2)  # Line 2 = dd:mm:yyyy[cite: 2]

        # Wait for 1 second before updating again (REQ-01)
        time.sleep(1)

def main():
    # Initialize LCD
    lcd = LCD.lcd()
    lcd.lcd_clear()

    # Start the clock thread
    t1 = Thread(target=clock_thread)
    t1.start()

if __name__ == "__main__":
    main()