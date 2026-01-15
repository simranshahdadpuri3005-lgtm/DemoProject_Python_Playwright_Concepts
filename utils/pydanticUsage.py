#pip install pydantic

from pydantic import BaseModel, ValidationError

#pydantic is used for data validation and settings management using python type annotations
# basically to make sure the data format of the variables used


class User(BaseModel):
    username: str
    password: str
    age: int 
    #  age: int = None  -  Optional field with default value None



