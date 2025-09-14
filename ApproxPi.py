#ApproxPi.py
#Name: Grant Schaeffer
#Date: 9/14/25
#Assignment: Pi
import math
import time


#PLEASE NOTE - This is an optional, extra credit portion of the lab.

def main():
  realPi = math.pi

  #ask user for decimal percision (up to 10)
  decimal = input("How many decimals places would you like? ")
  decimal = int(decimal)
  start = time.time()
  #calculate pi using the approximation technique
  #Loop until the level of percision is reached

  end = time.time()

  elapsedTime = end - start
  print(elapsedTime)

if __name__ == '__main__':
  main()
