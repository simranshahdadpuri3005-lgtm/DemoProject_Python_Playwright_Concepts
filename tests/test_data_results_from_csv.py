import csv
    
    #get data from csv file
def test_dataFromCSV():
    data =[]    #define an empty list to store data from csv file
    with open("testData\\credentials.csv") as csvFile:
        dataInCsv = csv.DictReader(csvFile)  #Read data inside csv file
        for row in dataInCsv:       # for reading data from csv file, we need to convert it into rows and then read it
            data.append(row)        #append will add each row into data list
    
    print("all the data of csv is ", data)
    print("first row data of csv is ", data[0])     
    print("username from first row is ", data[0]["username"])  #username is the key in csv file

def test_writintgIntoCSV():
        insert_data_to_csv()

def test_writingIntoCSVWithoutHeader():
    with open("testData\\newCredentials.csv", mode="a", newline='') as csvFile: # we are opening csv file in write mode
        writer = csv.DictWriter(csvFile, fieldnames=["username", "password", "age"])
        writer.writerow({"username": "abc444@gmail.com", 
                         "password": "Siabb34343@123", 
                         "age": "35"
                         })
        

    #insert data into csv file
def insert_data_to_csv():
    with open("testData\\newCredentials.csv", mode="w", newline='') as csvFile: # we are opening csv file in write mode
        #if the mode is 'w' then it will overwrite the existing data
        #if the mode is 'a' then it will append the data to existing data

        fieldnames = ["username", "password", "age"]  #header should be passed in form of list
        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)  
        
        writer.writeheader()   #writing the header row
        
        #writing data rows 
        #the values should be passed in form of dictionary

        writer.writerow({"username": "nice123@gmail.com", 
                         "password": "new@123", 
                         "age": "25"
                         })
        

    



    


