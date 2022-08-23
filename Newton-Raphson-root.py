y = float(input("Your number: "))
epsilon  = 0.01
guess = y/2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses +=1
    guess = guess - (((guess**2) - y)/(2*guess))
print(numGuesses)
print("Square root of", y, "is about", guess)