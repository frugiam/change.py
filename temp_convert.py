# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2b Write a program that converts Celsius temperatures to Fahrenheit temperatures.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit:", fahrenheit)