def fib(x):
    """assumes x an int >= 0
    returns Fibonacci of x
    formula: fib(x) = fib(x-1)+ fib(x-2)"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(6))

#using dictionaries

def fib_efficient(n, d): #n is the number and d is the dictionary
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))