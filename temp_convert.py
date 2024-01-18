# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2b Write a program that converts Celsius temperatures to Fahrenheit temperatures.
def convert_temp(celsius):
    return(9/5)*celsius + 32
    celsius = float(input("Please enter a Celsius temperature"))
    fahrenheit = convert_temp(celsius)
    print(fahrenheit)