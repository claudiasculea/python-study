alphabet = "aefhilmnorsxAEFHILMNORSX"

word = input("Let's cheer for: ")
i = 0

while i < len(word):
    char = word[i]
    if char in alphabet:
        print("Give me an", char, "!", char)
    else:
        print("Give me a ", char, "!", char)
    i +=1
print("What does that spell?", word, "!!!")