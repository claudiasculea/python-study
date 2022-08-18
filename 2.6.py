n = int(input("which number to square? "))
result = 0
variable = n
while variable != 0:
    result +=n
    variable -=1
print(str(n) + "*" + str(n) + "=" + str(result))