def fibonacci(n):
    if n == 0:
        return 0  # Base case 1
    elif n == 1:
        return 1  # Base case 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)  # Recursive call

print(fibonacci(4))

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(2))