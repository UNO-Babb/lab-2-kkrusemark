#FutureTime.py
#Name: Kylie Krusemark
#Date: 9/4/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 5) % 24
  currentMinute = now.minute

  #print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  hours = int(input("How many hours in the future would you like? (#) "))

  #Ask user for minutes
  minutes = int(input("How many minutes in the future would you like? (#) "))

  #Calculate the time after the user-supplied time has passed.
  futureMins = (currentMinute + minutes) % 60
  extraHour = (currentMinute + minutes) // 60
  futureHour = (currentHour + hours + extraHour) % 24
  futureHour12 = ((futureHour - 1) % 12) + 1 

  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print("The future time will be", futureHour12, ":", futureMins, "!")

if __name__ == '__main__':
  main()
