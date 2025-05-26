#Example: 01
count = 0
for i in range(1,101):
    count += i 
print("Sum of first 100 whole numbers: ",count)

# Example #02
num = 30
even = []
for i in range(1,16):
    if num % i == 0:
        even.append(i)
print(even)