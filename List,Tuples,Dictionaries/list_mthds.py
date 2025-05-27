# Adding Elements
subjects : list = ["Maths","Physics","Chemistry"]
subjects.append("Computer")
print(subjects)

subjects.extend(["Urdu","Pst"]) #add multiple elements
print(subjects)

# Removing Elements
subjects.remove("Pst")
print(subjects)
subjects.pop(3)
print(subjects)

#Sorting A List
num : list = [1,3,2,5,4,6,1,8,7]
num.reverse()
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)

print(subjects)
subjects.sort(key=len)
print(subjects)
subjects.sort(key=lambda word:word[0])
print(subjects)

#Iterating Over List
num1 :list = [1,2,3,4,5]
for i in num1:
    print(i*2)

comprehension = [x * 3 for x in [1,2,3,4] if x > 1]
print(comprehension)