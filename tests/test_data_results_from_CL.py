import os
from dotenv import load_dotenv
#load_dotenv()  reads the .env file and loads the environment variables

#one way to get data from command line is by using os.getenv
def test_getDataFromCommanLine():
    userName = os.getenv("userName")
    #using os.getenv, we are passing the username while execution 
    print("username passed from terminal is ", userName)
    password = os.getenv("password")
    print("password passed from terminal is ", password)


# To run this test, use the command:
# $env:userName="simran@test.com"; pytest -s

#to pass two values
# $env:userName="simran@gmail.com"
# $env:password="MySecretPassword"
# pytest -s

# or
# $env:userName="simran@gmail.com"; $env:password="MySecretPassword"; pytest -s

#we need to install pip install python-dotenv
#another way to get data from command line using dotenv module

def test_getDataFromEnvFile():
    env_var = os.getenv("env")  #getting the env file name from command line
   # env_var = os.getenv("env", "QAEnv")  #here QAEnv is default value if no value is passed from command line
   
    load_dotenv(f".env.{env_var}")   #loading the .env file
    userName = os.getenv("Amazon_username") #varaible name should be same as passed in the env file
    password = os.getenv("Amazon_password")
    print("username passed from env file is ", userName)
    print("password passed from env file is ", password)
   

# you can call the above using the command

# $env:userName="simran@test.com"; 
# $env:password="MySecretPassword";
# $env:env="dev"; `
# pytest -s

