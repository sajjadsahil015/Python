from pydantic import BaseModel,field_validator,model_validator
from typing import Optional

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

class User(BaseModel):
    name:str
    age:int

#converts string in integer
u = User(name="Ali",age="23")
print(u)

class Product(BaseModel):
    title: str
    description: Optional[str] = "No description available"

p = Product(title="Laptop",description="dell core i5 6th generation")
print(p)

class Person(BaseModel):
    name:str
    age:int 

    @field_validator("name","age")
    @classmethod
    def if_not_alph(cls,value):
        if not value.isalpha():
            raise ValueError("Name must contain alphabets only")
        return value

try:    
    person = Person(name="Ali")
except Exception as e:
    print(e)

class Employee(BaseModel):
    name: str
    age: int

    @model_validator(mode="after")
    def validate_all(cls, values):
        if not values.name.isalpha():
            raise ValueError("Name mein sirf alphabets hone chahiye")
        if not 0 <= values.age <= 120:
            raise ValueError("Age 0 se 120 ke darmiyan honi chahiye")
        return values