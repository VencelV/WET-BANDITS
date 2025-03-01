from periphery import PWM
import time
#assuming pin 33 is associated with 0,1 (wtf?)
pwm=PWM(0,1)
#frequency yippe 
pwm.frequency= 50
pwm.enable()

def set_servo_angle(angle):
    # Convert angle (0-180) to duty cycle (1ms - 2ms pulse width)
    duty_cycle = (1.0 + (angle / 135.0)) / 50.0  # Normalize for 20ms period
    pwm.duty_cycle = duty_cycle

set_servo_angle(60)

time.sleep(1)
