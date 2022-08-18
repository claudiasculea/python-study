cube = int(input("Give me a number "))
for guess in range(abs(cube+1)):
    if guess**3 >= abs(cube):
        break

if guess**3 != abs(cube):
    print(cube, "is not a perfect cube")
else:
    print("cube root of", cube, "is", guess)

