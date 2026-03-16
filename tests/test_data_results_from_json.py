import json
# Importing Python's built-in json library.
# This library helps us read and work with data stored in JSON files.

from utils.readingJson import readJsonData
# Importing a custom function called readJsonData from another file.
# This function is used to read data from a JSON file.

searchData = "testData\searchData.json" # Path of the JSON file that contains sample test data

# Reading the JSON file and storing its content in the variable "testData"
testData = readJsonData(searchData)
# After this line runs, "testData" will contain the data from the JSON file


# This function demonstrates how to access and update values
# from the JSON data that was read earlier.
def test_serachDataValues():
    print("testdata is",testData)     # Displays the entire JSON data in the console.
    
    print("Before update the value of testdata3-subdata1 is ",testData["testData3"]["subData1"]) 
    # Accesses a specific value inside the JSON data and prints it.
    # In this case, it shows the value stored inside: testData3 → subData1
    
    testData["testData3"]["subData1"] = "updatedValue_subData1"   #updating the json file values
    # Updating the value of "subData1" inside "testData3".
    # This change is done only in the program memory (not directly in the file).

    print("after update the value of above is ",testData["testData3"]["subData1"])
    # Printing the value again to confirm that it was updated successfully.


# Another example showing how to read data directly from a JSON file
# using Python's built-in json library.

def test_dataFromFile():
    # Opening the credentials.json file.
    # The "with" statement ensures the file is properly closed after reading.
    with open("testData\\credentials.json") as f:
          data =  json.load(f)  

        # json.load() reads the content of the JSON file
        # and converts it into a Python dictionary that we can use in code

        # In short, data in json can be easily read by loading it using json.load() method

    print("all the data of json is ", data)
       # This prints the entire contents of the credentials.json file.


