import periphery

import time


pwm = PWM(0, 33)  # PWM chip 0, channel 33

pwm.enable()

# Set PWM period (20ms typical for servos)
pwm.frequency = 50  # 50Hz (20ms period)

# Function to set duty cycle for the servo
def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (1ms - 2ms pulse width)
    duty_cycle = (1.0 + (angle / 180.0)) / 20.0  # Normalized for 20ms period
    pwm.duty_cycle = duty_cycle

# Move servo to 180 degrees
set_servo_angle(180)

# Wait for servo to move
time.sleep(1)

# Disable PWM output
pwm.disable()

# Close PWM
pwm.close()