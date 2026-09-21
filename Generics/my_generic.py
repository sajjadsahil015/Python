from typing import Generic,TypeVar
from dataclasses import dataclass

T = TypeVar('T',bound= int | str)

def first_item(a:list[T]):
    return a[0]

print(first_item([1,2,3]))
print(first_item(['a','b','c']))
# print(first_item([3.4,45,3]))

def swap[T : str | int](a:T,b:T):
    return b,a

print(swap("x",4))

def get_value[K, V](d: dict[K, V], key: K) -> V:
    return d[key]

person = {"name": "Alice", "age": 30}
print(get_value(person, "name")) 


class Person:
    def __init__(self, name: str):
        self.name = name

def greet(p: Person) -> None:
    print("Hello", p.name)

greet(Person("Ali"))

from typing import overload

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...

def double(x:T) -> T:
    return x * 2

print(double(5.3))
print(double([34,4])) 