from machine import Pin, PWM, time_pulse_us
from time import sleep_us, sleep
from servo import Servo

#PIN
TRIGGER_PIN = 
ECHO_PIN = 
SPEED = 0.0343
servo_pin = Pin()
my_servo = Servo(servo_pin)
SPEAKER_PIN = 

# Initialize Pin
trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)
buzzer = Pin(SPEAKER_PIN, Pin.OUT)
buz = PWM(buzzer)

#Distance Set
setdistance = 

#Beep
C6 = 1047

while True:
  trigger.value(0)
  sleep_us(5) 

  trigger.value(1)
  sleep_us(10)
  trigger.value(0)
  pulse_time = time_pulse_us(echo, 1)

  distance = (SPEED * pulse_time) / 2

  if (distance < setdistance):
    print('distance:', distance)
    
    buz.freq(C6)
    buz.duty(10)
    
    my_servo.write_angle(165)
        
    buz.duty(0)
    
    
    
