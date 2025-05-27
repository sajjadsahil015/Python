tup : tuple = (["Maths","Physics","Urdu"])
num : tuple = (1,2,3,4)
mix : tuple = (1,"all",True)

print(tup)
print(num)
print(mix)

print(tup[1])
print(num[0:3])
print(len(mix))

for i in tup:
    print(i)
print(3 in num)
print(num * 2)
print(num+mix)

a,b,c = mix
print("\n",a,"\n",b,"\n",c)

print(num.count(1))
print(num.index(3))