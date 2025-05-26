#If Statement
x : int = 5 
if x > 3:
    print(x)
#Else statement
if x > 5:
    print("number is greater than 5")
else:
    print("Number is less than or equal to 5")

#Elif Statement

if x > 5:
    print("Number is greater than 5")
elif x == 5:
    print("Number is 5")
else:
    print("Number is less than 5")

#Nested if Statement
if x >= 0:
    if x % 2 == 0:
        print("Number is even")
    else:
        print("number is odd")
else:
    print("Sorry number is negative")