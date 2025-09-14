#TempConvert.py
#Name: Grant Schaeffer
#Date: 9/14/25
#Assignment: Temperature Converter


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = input("What is the temperature in Fahrenheit? ")
  tempF= float(tempF)
  tempC = (((tempF - 32) * 5 ) / 9)
  tempC = round(tempC,2)
  print(tempF, "is ", tempC, "degrees celsius.")
if __name__ == '__main__':
  main()
