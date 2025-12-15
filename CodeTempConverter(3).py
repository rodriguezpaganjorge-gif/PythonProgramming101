# Author: Jorge Rodriguez Pagan
# Purpose: Temperature Converter
# Class: Python Programming

UserName= input("What is your name?")
print("Welcome to your Temperature Converter", UserName, ":)")

fTemperature= float(input("Enter a temperature: "))
Temperature_scale= input("Is the temp F for Fahrenheit or C for Celsius?")
fTemperature3= ((9.0/5.0) * fTemperature)

if Temperature_scale == "F":
    if fTemperature > 212:
        print ("Temperature can not be greater than 212! :( ")

    else:
        fTemperature2= (5.0 / 9) * (fTemperature - 32)
        print("Your temperature in Celcius is: ", fTemperature2, "C")

elif Temperature_scale == "C":
    if fTemperature > 100:
        print ("Temperature can not be greater than 100! :(")

    else:
        fTemperature3= ((9.0/5.0) * fTemperature) + 32
        print ("Your temperature in Celcius is: ", fTemperature3, "F")

else:
    print("Enter F or C:")
