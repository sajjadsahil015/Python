from pydantic import BaseModel

class Books(BaseModel):
    name: str
    author: str

class Library(BaseModel):
    name: str
    books: list[Books]

l = Library(name="Khoja library" ,books=[{"name":"Alice's Adventures in Wonderland","author":"Lewis Carroll."},{"name":"Don Quixote","author":" Miguel de Cervantes."}])

print(l.books[1].name)