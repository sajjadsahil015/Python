def calculator():
    while True:
        user = input("Enter the following operation: +,-,/,*,%,//,** or q for quit: ")
        if user.lower() == "q":
            break
        if user not in('+','-','/','*','%','//','**'):
            print("Please Enter the correct operation")
            continue
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter Second number: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        if user == '+':
            result = num1 + num2
        elif user == '-':
            result = num1-num2
        elif user == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Can't divide by zero")
                continue
        elif user == '*':
            result = num1 * num2
        elif user == '%':
            if num2 != 0:
                result = num1 % num2
            else:
                print("Can't divide by zero")
                continue
        elif user == '**':
            result = num1 ** num2
        else:
            if num2 != 0:
                result = num1 // num2
            else:
                print("Can't divide by zero")
                continue
        print("Result: ",result)
calculator()