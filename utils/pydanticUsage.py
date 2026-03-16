# pip install pydantic - This command installs the Pydantic library.

# Pydantic is used in Python to validate and manage structured data.

from pydantic import BaseModel, ValidationError
# BaseModel is the main class used to create data models in Pydantic.
# ValidationError is the error that appears when data does not match the expected format.

# pydantic is used for data validation and settings management using python type annotations
# basically to make sure about the data format of the variables used

# Pydantic is used for data validation using Python type hints.
# This means we can define what type of data each field should contain
# (for example: text, numbers, etc.), and Pydantic will automatically
# check if the provided data follows that format.

# Creating a data model called "User".
# This model defines the structure and data types for user information.

class User(BaseModel):
    username: str    # The username field must contain text (string).
    password: str    # The password field must also contain text (string).
    age: int 
    #  age: int = None  -  Optional field with default value None
    
    # The age field must contain a number (integer).
    # If a different type of value (like text) is provided,
    # Pydantic will raise a validation error.

    # age: int = None
    # Example of making the field optional.
    # In this case, age is allowed to be empty and its default value will be None.



