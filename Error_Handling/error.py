try:
    x = int(input("Enter first number to be divide: "))
    y = int(input("Enter  second number to be divide: "))
except ValueError:
    print("please enter a number")
def add(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Can't divide by zero")
    except Exception as e:
        print(e)
    else:
        print(f"Division successful, result = {a/b}")
    finally:
        print("this will always execute")

try:
    add(x,y)
except NameError:
    pass