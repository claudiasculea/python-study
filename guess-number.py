
def guessnb(a, b):
    guess = round((a+b)/2)
    m = input(f"Is {guess} your number? Y/N ")
    if m == "Y":
        return guess
    else:
        m_1 = input("Is your number greater? Y/N ")
        if m_1 == "Y":
            a = guess
        else:
            b = guess
        return guessnb(a, b)

print(guessnb(0, 100))


