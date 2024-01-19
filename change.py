# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2c Write a program that asks the user for a (integer) number of cents.
cents = int(input('Please enter an amount in cents less than a dollar.'))
ct = cents
quarters = cents // 25
cents -= (quarters * 25)
dimes = cents // 10
cents -= (dimes * 10)
nickels = cents // 5
cents -= (nickels * 5)
pennies = cents // 1
cents -= (pennies * 1)
print('Your change will be: ')
print("With " + str(ct) + " cents you can have " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(
    nickels) + "nickels," + str(pennies) + " pennies.")
