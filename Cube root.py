cube = int(input("Give me a number "))
for guess in range(cube+1):
    if guess**3 == cube:
        print("cube root of", cube, "is", guess)