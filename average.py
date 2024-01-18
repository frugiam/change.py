# Author: Michelle Frugia
# GitHub username: frugiam
# Date: 01/18/2024
# Description: Project 2a Write a program that asks the user for five numbers and then prints out the average of those numbers.
print("Please enter five numbers.")
result = 0
for x in range(5):
    result += eval(input())
average = result/5
rounded_average = round(average, 1)
print("The average of those numbers is:")
print("%.1f" % rounded_average)