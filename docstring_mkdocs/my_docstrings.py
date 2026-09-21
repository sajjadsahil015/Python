def hello():
    """prints hello"""
    print("Hello")

hello()
print(hello.__doc__)

def add(a,b):
    """takes two numbers and returns their sum"""
    return a+b

print(add(3,4))
print(add.__doc__)