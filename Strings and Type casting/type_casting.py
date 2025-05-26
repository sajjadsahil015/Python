#Integer Conversion
num : float = 5.6
num_int = int(num)
print(num_int,type(num_int))

num1 : bool = False
num1_int = int(num1)
print(num1_int)

#Float Conversion
a : int = 5
b = float(a)
print(b,type(b))

a: str = "43"
b = float(a)
print(b, type(b)) 

#String Conversion

a : int = 45
b = str(a)
print(b, type(b))

a : bool = True
b = str(a)
print(b,type(b))

#Boolian Conversion
a : int = 5
b = bool(a)
print(b,type(b))

a : str = ""
b = bool(a)
print(b,type(b))

#List,Tuples and Set Conversion
tup = (1,2,3,"st")
lst = list(tup)
print(lst,type(lst))

lst = [1,2,3,3,4,45,3,4,"d"]
st = set(lst)
print(st,type(st))

#Dictionary Conversion
lst = [("name","Ali"),("Age",45)]
dic = dict(lst)
print(dic,type(dic))

#Complex Number Conversion
num : int = 5
com = complex(num)
print(com,type(com))