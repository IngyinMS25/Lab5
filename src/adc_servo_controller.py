from hal import hal_adc as adc
from hal import hal_servo as servo
from time import sleep

def main():
    # Call the two init functions once at startup
    adc.init()
    servo.init()

    print("ADC Servo Controller initialized. Reading potentiometer on channel 1...")

    while True:
        # Read the potentiometer value from ADC channel 1
        adc_val = adc.get_adc_value(1)
        print(f"ADC Value = {adc_val}")

        # Calculate the servo angle based on Figure 3 (ADC 0 -> 180°, ADC 1023 -> 0°)
        angle = 180 - (adc_val * 180 / 1023)

        # Set the calculated angle to the servo motor
        servo.set_servo_position(angle)

        # Short sleep to stabilize readings and reduce CPU usage
        sleep(0.1)

if __name__ == "__main__":
    main()