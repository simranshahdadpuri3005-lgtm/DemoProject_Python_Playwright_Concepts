from utils.pydanticUsage import User
# Importing the "User" class which is defined using Pydantic.
# Pydantic helps validate (check) that the data provided matches the expected format.

from utils.readingJson import readJsonData
# Importing a custom function used to read data from a JSON file.


def test_pydantic_validation_normalInput():
     # This test demonstrates how Pydantic validates correct input data.

    data = {
        "username": "testuser",
        "password": "securepassword",
        "age": 30
    }
     # Creating a dictionary containing sample user data.

    user_variable = User(**data)
    # Creating an object of the User class using the data dictionary.
    # The ** operator unpacks the dictionary so that each key-value pair is passed as an argument to the User class.
    # user is a pydantic class
    # data is passed with ** to accept the data

    print(user_variable)
    # Printing the validated user object.


    # "User" is a Pydantic model (class) which validates the data types.
    # If the data types match the expected format, the object will be created successfully.


# Example of INVALID input data (kept commented to avoid test failure)

def test_pydantic_validation_ErrorInput():
    # This test demonstrates what happens when invalid data is provided.

    data = {
        "username": "testuser",
        "password": "securepassword",
        "age": "string and not integer"
    }
    # In this case, "age" is provided as a string instead of an integer.

    user_variable = User(**data)
    print(user_variable)
    
#     # This test case will fail
#     # Since the User model expects age to be an integer,
#     # Pydantic will raise a validation error.such as 
#     # pydantic_core._pydantic_core.ValidationError: 1 validation error for User
#     # This means the data does not match the required format.
#     # The error message will indicate that the input for "age" is invalid and cannot be parsed as an integer.        



def test_pydanticValidation_Json():
    data = readJsonData("testData\\credentials.json")
    user = User(**data)
    print(user)
    # test_pydanticValidation_Json – Missing age field in JSON - hence the error is expected for this testcase
    # to make it pass test case , either we can add age field in json 
    # or make it optional in pydantic model by using age: int = None
    
    # updated code should be like below in pydanticUsage.py file
        # from typing import Optional
        # class User(BaseModel):
        #     username: str
        #     password: str
        #     age: Optional[int] = None

import csv

def test_pydanticValidation_Csv():
    with open(r"testData\credentials.csv") as csvFile:
        reader = csv.DictReader(csvFile)

        for row in reader:
            user = User(**row)
            print(user)

# this test case will fail  becasue Pydantic did not receive the password field.
# Python is case-sensitive, so Password ≠ password
# after fixing the header in credentials.csv file to "password" instead of "Password", the test case will pass successfully.
