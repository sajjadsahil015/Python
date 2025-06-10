sum = lambda x,y: x+y
print(sum(50,43))

my_dict = {"x" : 1,"y":4, "z":3}
sorting = dict(sorted(my_dict.items(),key=lambda item : item[1]))
print(sorting)