x = float(input("Enter a decimal: "))
p = 0

while ((2**p) * x)%1 != 0:
    p += 1
num = int(x*(2**p))
result = ""
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = "0" + result

result = result[0:-p] + "." + result[-p:]

print("The binary representation of your decimal is" , result)