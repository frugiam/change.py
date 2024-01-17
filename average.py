# Project 2a
print("Please enter five numbers.")
result = 0
for x in range(5):
    result += eval(input())
print("The average of those numbers is:")
print("%.1f"%(result/5))