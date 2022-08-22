cube = int(input("Enter a number:"))
epsilon = 0.001 #helps us move through guesses 
guess = 0.0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("guesses: ", num_guesses)

if abs(guess**3 - cube) >= epsilon:
    print("Failed on cube root of", cube)
else:
    print(guess, "is closer to the cube root of", cube)
    