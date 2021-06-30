def factorial(n: int):
    fact = n
    if n == 1:
        return 1
    else:
        fact = fact*factorial(n-1)
    return fact


print(factorial(8))