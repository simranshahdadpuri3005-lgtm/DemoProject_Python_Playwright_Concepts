import json


def readJsonData(jsonPath):
    #code to handle the json file
    with open(jsonPath) as f:
        testData = json.load(f)
        return testData
    