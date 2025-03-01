from periphery import PWM
import time

# Use PWM on Pin 33 (pwmchip0, channel 0)
pwm = PWM("/sys/class/pwm/pwmchip1", 0)

# Enable PWM
pwm.enable()

# Set frequency to 50Hz (20ms period for servos)
pwm.frequency = 50

# Function to set servo angle
def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (1ms - 2ms pulse width)
    duty_cycle = (1.0 + (angle / 180.0)) / 20.0  # Normalize for 20ms period
    pwm.duty_cycle = duty_cycle

# Move servo to 180 degrees
set_servo_angle(180)

# Wait for the servo to move
time.sleep(1)

# Move servo back to 0 degrees
set_servo_angle(0)

# Wait for the servo to move
time.sleep(1)

# Disable PWM output
pwm.disable()

# Close PWM
pwm.close()

