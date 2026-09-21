from pydantic import BaseModel

class School(BaseModel):
    name:str
    city: str

class Student(BaseModel):
    name: str
    age: int
    school : School

s = Student(name="Ali",age=15,school={"name":"Public School and College","city":"Skardu"})

print(s.school.name)
