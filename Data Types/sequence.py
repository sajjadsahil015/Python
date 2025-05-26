# String
x : str = "Ali"

y : str = 'Ahmed'

z : str = """Naveed"""

print(f"{x}\n{y}\n{z}")
print(type(x),type(y),type(z))

#List
my_list : list = [1,2,3,"Ali",4]

print(my_list,type(my_list))

#Tuple
my_tuple : tuple = (1,2,3,"Ali",True, 3 + 2j)

print(my_tuple,type(my_tuple))

#Range
my_range : range = range(1, 10, 2)
for i in range (1,11,3):
    print(i)
print(type(my_range))
