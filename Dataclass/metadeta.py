from dataclasses import dataclass,field
from datetime import date

def validate_required_info(instance):
    for field in instance.__dataclass_fields__.values():
        if field.metadata.get("required") and getattr(instance,field.name) is None:
            raise ValueError("Name is required!")
        
@dataclass
class Person:
    name:str = field(metadata={"required": True})
    age: int = field(metadata ={"required":False})

u = Person(name="Ali",age=15)
print(u)

validate_required_info(u)
# birth_date = date(2000,3,5)
# today = date.today()
# print(today.year-birth_date.year-((today.month,today.day)<(birth_date.month,birth_date.day)))