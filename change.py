# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2c Write a program that asks the user for a (integer) number of cents.
def calculate_change(cents):
    quarters = cents // 25
    cents -= quarters * 25
    dimes = cents // 10
    cents -= dimes * 10
    nickels = cents // 5
    pennies = cents - nickels * 5
    return quarters, dimes, nickels, pennies

def main():
    print("Please enter an amount in cents less than a dollar.")
    cents = int(input())

    if cents < 0 or cents > 99:
        print("Invalid input. Please enter a number between 0 and 99.")
        return

    quarters, dimes, nickels, pennies = calculate_change(cents)

    print("Your change will be:")
    print(f"Q: {quarters}")
    print(f"D: {dimes}")
    print(f"N: {nickels}")
    print(f"P: {pennies}")
