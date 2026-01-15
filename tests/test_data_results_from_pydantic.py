from utils.pydanticUsage import User
from utils.readingJson import readJsonData


def test_pydantic_validation_normalInput():
    data = {
        "username": "testuser",
        "password": "securepassword",
        "age": 30
    }
    user_variable = User(**data)
    print(user_variable)
    # user is a pydantic class
    #data is passed with ** to accept the data

# def test_pydantic_validation_ErrorInput():
#     data = {
#         "username": "testuser",
#         "password": "securepassword",
#         "age": "string and not integer"
#     }
#     user_variable = User(**data)
#     print(user_variable)
#     we will get error for this test case
# def test_pydantic_validation_normalInput():
#         data = {
#             "username": "testuser",
#             "password": "securepassword",
#             "age": "string and not integer"
#         }
# >       user_variable = User(**data)
#                         ^^^^^^^^^^^^
# E       pydantic_core._pydantic_core.ValidationError: 1 validation error for User
# E       age
# E         Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='string and not integer', input_type=str]
# E           For further information visit https://errors.pydantic.dev/2.12/v/int_parsing

# tests\test_data_results_from_pydantic.py:11: ValidationError
# ============================================================ short test summary info ============================================================= 
# FAILED tests/test_data_results_from_pydantic.py::test_pydantic_validation_normalInput - pydantic_core._pydantic_core.ValidationError: 1 validation error for User
# ==================
        
    
# def test_pydanticValidation_Json():
#     data = readJsonData("testData\credentials.json")
#     user = user(**data)

# def test_pydanticValidation_Csv():
#     data = readJsonData("testData\credentials.csv")
#     user = user(**data)