from pydantic import BaseModel,ConfigDict
from pydantic_settings import BaseSettings

# class User(BaseModel):
#     name:str 
#     model_config= ConfigDict(
#         extra="forbid",
#         frozen=True,
#     )

# u = User(name="Ali",age = 4)
# print(u)

class Config(BaseModel):
    api_key: str

    model_config = {
        "frozen": True,
        "str_strip_whitespaces": True,
    }

c = Config(api_key=" secret code ")
# c.api_key = "allowed"
print(c)

class Settings(BaseSettings):
    api_key: str 
    debug: bool = False

    class Config:
        env_file = ".env"

api = Settings()
print(api.api_key)