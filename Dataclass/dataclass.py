from dataclasses import dataclass
from typing import Optional,Final

# @dataclass(frozen=True)
# class Person:
#     name:str
#     age:int


# person = Person("Ali",22)
# person1 = Person("Ali",22)
# person.name = "Asif"
# print(person.age)
# print(person==person1)


@dataclass
class Person:
    """A person with a name and age."""
    name: str
    age: int
    occupation: Optional[str] = None
    # occupation: str | None = None

    VERSION: Final[str] = '1.0.0'

    @staticmethod
    def get_version() -> str:
        """Get the Person class version"""
        return Person.VERSION

# Create an instance of Person
person = Person("John Doe", 30, "Software Engineer")
print(person.get_version())  # 1.0


# Create instances of Person
person1 = Person("John Doe", 30, "Software Engineer")
person2 = Person("Jane Doe", 25, "Doctor")

print(Person.get_version())


