#For Loop

lst = [1,2,3,4]
for n in lst:
    print(n)
print("_"*30)
word : str = "Hello"
for i in word:
    print(i)
else:
    print("Loop Completed succesfully")

num : list = [1,2,3,4,5]
for n in num:
    print(n)
    if n == 6:
        print("Number FOund")
        break
else:
    print("Number not found")

for i in range(5):
    print("Hello world")

#While Loop
count = 1
while count<=5:
    print("Hello")
    count+=1

#Controlling Loop
for i in range(10):
    print(i)
    if i == 5:
        break
for i in range(5):
    if i == 3:
        continue
    print(i)

#Nested Loop
for i in range(1,5):
    for n in range(1,11):
        print(f"{i}*{n}={i*n}")
    print("\n")