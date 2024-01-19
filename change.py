# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2c Write a program that asks the user for a (integer) number of cents.
cents = int(input('Please enter an amount in cents less than a dollar: '))
quarters = cents // 25
cents = cents % 25
dimes = cents // 10
nickels = (cents % 10) // 5
pennies = (cents % 10) % 5
print('Your change will be: \nQ:', quarters, '\nD:', dimes, '\nN:', nickels, '\nP:', pennies)