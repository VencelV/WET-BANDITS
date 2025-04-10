from periphery import PWM
import time

# Assuming Pin 33 is on chip 0, channel 1 (you can confirm this from your pinout or hardware docs)
pwm = PWM(0, 1)  # chip 0, line 1
pwm.frequency = 100  # Set frequency to 50Hz (20ms period)
pwm.enable()

def set_servo_angle(angle):
    """
    Map servo angle (0-270) to a duty cycle (pulse width in range of 0.5ms to 2.5ms).
    """
    # Ensure the angle is between 0 and 270 degrees
    if angle < 0:
        angle = 0
    elif angle > 270:
        angle = 270

    # Calculate pulse width: 0.5ms for 0°, 2.5ms for 270°
    # (angle / 270) gives us a normalized value from 0 to 1, which we scale to 0.5ms to 2.5ms
    pulse_width_us = (angle / 270.0) * (2500 - 500) + 500  # Pulse width in microseconds

    # Convert pulse width in microseconds to duty cycle for PWM
    # For 50Hz, the period is 20ms (20000 microseconds)
    duty_cycle = pulse_width_us / 20000.0

    pwm.duty_cycle = duty_cycle

set_servo_angle(0)

time.sleep(1)


# Test by setting the servo to 60 degrees
set_servo_angle(60)

time.sleep(1)

set_servo_angle(0)

time.sleep(2.5)
# Move the servo to 0 degrees (extreme position)
set_servo_angle(60)

time.sleep(2.5)

# Move the servo to 135 degrees (mid-range)
set_servo_angle(0)

time.sleep(2.5)

set_servo_angle(120)


time.sleep(2.5)
set_servo_angle(0)
time.sleep(2.5)
set_servo_angle(120)
time.sleep(2.5)
set_servo_angle(0)
time.sleep(2.5)
set_servo_angle(180)
time.sleep(2.5)
set_servo_angle(180)
#Move the servo to 270 degrees (extreme position)

# Disable PWM output after test
pwm.disable()

# Close PWM to free resources
pwm.close()
