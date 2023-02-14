from periphery import PWM

from time import sleep
import subprocess
import datetime

fan = PWM(0, 0)

fan.frequency = 100
fan.duty_cycle = 0.0

min_temp = 50.000
max_temp = 70.000

temp_interval = max_temp - min_temp

max_pwm = 1.000

sleep_time = 5

fan.enable()

while True:
  sensors_output = subprocess.check_output(["sensors", "-u"], universal_newlines=True)
  current_hour = datetime.datetime.today().hour 
  if 9 <= current_hour < 21:
    max_pwm = 1.000
    sleep_time = 5
  else:
    max_pwm = 0.000
    sleep_time = 3600
  for line in sensors_output.split('\n'):
    if 'temp1_input' in line:
      current_temp_line = line
  for word in current_temp_line.split(' '):
    if '.' in word:
      current_temp_word = word
  current_temp = float(current_temp_word)
  pwm_value = max_pwm
  if current_temp <= min_temp:
    pwm_value = 0.000
  if min_temp < current_temp < max_temp:
    pwm_value = round(max_pwm*(current_temp-min_temp)/(temp_interval),5)
  fan.duty_cycle = pwm_value
  sleep(sleep_time)
  
pwm.close()






