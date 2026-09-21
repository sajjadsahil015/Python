from pydantic import BaseModel,Field

class User(BaseModel):
    name : str = Field(...,alias="full_name")
    age : int = Field(...,alias="Age")

    model_config= {
        "populate_by_name":True
    }

c = User(full_name="Ali Abbas",Age=54)
print(c.full_name)
print(c.model_dump(by_alias=True))

user = User(name="Bob", age=30)

user_json = user.model_dump_json()
print(user_json)

new_user = User.model_validate_json('{"name":"Charlie","age":40}')
print(new_user.name) 
print(type(new_user)) 