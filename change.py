# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2c Write a program that asks the user for a (integer) number of cents.
print('Please enter an amount in cents less than a dollar.')
def change(num_cents):
    quarters = num_cents // 25
    num_cents %= 25
    dimes = num_cents // 10
    num_cents %= 10
    nickels = num_cents // 5
    num_cents %= 5
    pennies = num_cents

    return quarters, dimes, nickels, pennies

num_cents = int(input("Enter the number of cents from 0 to 99: "))
quarters, dimes, nickels, pennies = change(num_cents)
print(f"The fewest number of coins to represent {num_cents} cents is: ")
print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")