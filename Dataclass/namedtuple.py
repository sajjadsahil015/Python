from typing import NamedTuple

class NT(NamedTuple):
    name: str
    age : int

nt = NT("Ali",45)
print (nt.name)