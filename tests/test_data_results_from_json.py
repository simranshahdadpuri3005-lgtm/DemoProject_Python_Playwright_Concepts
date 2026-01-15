import json
from utils.readingJson import readJsonData

searchData = "testData\searchData.json"
testData = readJsonData(searchData)

def test_serachDataValues():
    print("testdata is",testData)
    print("before update the value of testdata3-subdata1 is ",testData["testData3"]["subData1"]) 
    testData["testData3"]["subData1"] = "updatedValue_subData1"   #updating the json file values
    print("after update the value of above is ",testData["testData3"]["subData1"])


# another way to read json file 

def test_dataFromFile():
    with open("testData\\credentials.json") as f:
          data =  json.load(f)  #read data inside json file
          
          #data in json can be easily read by loading it using json.load() method
    print("all the data of json is ", data)


