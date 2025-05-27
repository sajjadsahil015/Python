student : dict = {
    "Name": "ALi",
    "Roll No" : 24,
    "Subjects" : ["Maths","Physics","Urdu"]
}
print(student)

#Another way to make dictionary
#student = dict(Name="Ali",Age = 15)

#Accessing values
print(student["Name"])
print(student.get("Roll No","Not Found")) #if roll no is not found it will print Not Found

#Modifying A dictionary
student["Section"] = "A"
student["Roll No"] = 3
print(student)

#Deleting Items
student.pop("Subjects")
print(student)
del student["Section"]
print(student)

#Dictionary Methods
print(student.keys())
print(student.values())
print(student.items())
student.update({"Age":23,"Player":True})
print(student)

#Iterating Over a Dictionary
for keys,values in student.items():
    print(keys,":",values)

#DIctionary Comprehension

celsius = [0,5,10,15]
fahrenheit = {str(c)+"c" : str((c*9/5)+32)+"F" for c in celsius}
print(fahrenheit)