def greetings():
    greet = "Hello World"
    return greet
message = greetings()
print(message)

def val(x):
    return x
print(val(10))

def modify_lst(lst):
    lst.append(4)

lst = [1,2,3]
modify_lst(lst)
print(lst)

def person(name,age):
    print(f"{name} is {age} years old")
person(age =30, name = "ali")

#*unpacking iterables
def add(*num):
    return sum(num)
print(add(*[1,2,3,4]))

#Position only arguments

def avg(x,y,/,z):
    print((x+y+z)/2)
avg(1,2,z=4)

#kyword only argument
def even(*,x):
    if(x%2)==0:
        print("Even")
    else:
        print("Odd")
even(x = 4)

def sum(a,b):
    return a+b
print(sum(1,2))

def sum(a,b,c):
    return a+b+c
print(sum(1,2,3))

