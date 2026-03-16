import os
from dotenv import load_dotenv
# load_dotenv()  reads the .env file and loads the environment variables

#one way to get data from command line is by using os.getenv
def test_getDataFromCommanLine():
    # Fetch username passed from the terminal using environment variables.
    userName = os.getenv("userName")
    # using os.getenv, we are passing the username while execution 
    print("username passed from terminal is ", userName)

    # Fetch password passed from the terminal
    password = os.getenv("password")
    print("password passed from terminal is ", password)


# To run this test, use the command in PowerShell:
# $env:userName="simran@test.com"; pytest -s

# To pass two values:
# $env:userName="simran@gmail.com"
# $env:password="MySecretPassword"
# pytest -s

# Or in a single command:
# $env:userName="simran@gmail.com"; $env:password="MySecretPassword"; pytest -s

# ---------------------------------------------------------
# Another way to get data from the command line is by using
# environment files with the python-dotenv module.
# Install the module using:
# pip install python-dotenv
# ---------------------------------------------------------


def test_getDataFromEnvFile():
    # Get the environment name from the command line
    # Example: dev, qa, prod
    env_var = os.getenv("env")  # getting the env file name from command line
    
    # Optional: set a default environment if none is provided
    # env_var = os.getenv("env", "QAEnv")
  
    # Load the corresponding .env file
    # Example: .env.dev, .env.qa, .env.prod
    load_dotenv(f".env.{env_var}")   #loading the .env file

    # Variable names must match the keys defined inside the .env file
    userName = os.getenv("Amazon_username") 
    password = os.getenv("Amazon_password")
    print("username passed from env file is ", userName)
    print("password passed from env file is ", password)
   

# To run this test, use the command:
# $env:userName="simran@test.com"; $env:password="MySecretPassword"; $env:env="dev";pytest -s tests\test_data_results_from_CL.py
