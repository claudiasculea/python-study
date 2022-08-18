#finding the cube root

x = int(input("What is your number? "))
ans = 0

while ans**3 < abs(x):
    ans = ans + 1
if ans**3 != abs(x):
    print(str(x) + " is not a perfect cube")
else:
    print("Cube root of " + str(x) + " is " + str(ans))

