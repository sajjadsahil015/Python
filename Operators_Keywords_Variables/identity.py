a : list = [1,2,3]
b : list = [1,2,3]
c = a

print(a is c)
print(b is c)
print(a == b)
print (a is not b)
print("\n ----- \n")

print(id(a))
print(id(b))
print(id(c))