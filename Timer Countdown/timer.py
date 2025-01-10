print("TIMER COUNTDOWN")

import time


def countdown(user_time_input):
   while user_time_input >= 0:
       mins, secs = divmod(user_time_input, 60)
       timer = '{:02d}:{:02d}'.format(mins, secs)
       print(timer, end='\r')
       time.sleep(1)
       user_time_input -= 1
   print('Lift off')


if __name__ == '__main__':
   user_time_input = int(input("Enter the time you want to start a countdown for (in seconds): "))
   countdown(user_time_input)