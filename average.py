# Project 2a
print("Please enter five numbers.")
result = 0
for x in range(5):
    result += eval(input())
average = result/5
rounded_average = round(average, 1)
print("The average of those numbers is:")
print("%.15f" % rounded_average)