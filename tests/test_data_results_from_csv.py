import csv
# Importing Python's built-in csv library.
# This library allows us to read data from CSV files and also write data into them.


# Read data from a CSV file
def test_dataFromCSV():
    data =[]    #define an empty list to store data from csv file
    with open("testData\\credentials.csv") as csvFile:         # Opening the CSV file that contains user credential data.
        dataInCsv = csv.DictReader(csvFile)  
        # DictReader reads each row of the CSV file # and converts it into a dictionary (key-value format).
        # The column names in the CSV file become the keys.

         # Looping through each row of the CSV file.
        for row in dataInCsv:       # for reading data from csv file, we need to convert it into rows and then read it
            data.append(row)        # append will add each row into data list
    
    print("all the data of csv is ", data)  # Prints the entire data from the CSV file.
    print("first row data of csv is ", data[0])        # Prints only the first row of the CSV file.
    print("username from first row is ", data[0]["username"]) 
    # Accessing the value of "username" from the first row.
    # "username" is the column name (header) in the CSV file.


# This test calls another function that writes data into CSV
def test_writintgIntoCSV():
        insert_data_to_csv() 
        # Calls the function below that inserts data into a CSV file.


# Writing data into a CSV file WITHOUT writing the header
def test_writingIntoCSVWithoutHeader():
    with open("testData\\newCredentials.csv", mode="a", newline='') as csvFile: 
        # Opening the CSV file in append mode ("a").
        # Append mode adds new data at the end of the file
        # without deleting the existing data.

        writer = csv.DictWriter(csvFile, fieldnames=["username", "password", "age"])
        # DictWriter helps write dictionary data into the CSV file.
        # "fieldnames" defines the column names.

        writer.writerow({"username": "abjj@gmail.com", 
                         "password": "Siabb34343@123", 
                         "age": "35"
                         })
        # Writing one row of data into the CSV file.
        # The data is provided in dictionary format.


# Function to insert data into a CSV file

def insert_data_to_csv():
    with open("testData\\newCredentials.csv", mode="w", newline='') as csvFile: 
        # Opening the CSV file in write mode ("w").

        # If the mode is "w":
        # → It will delete any existing data in the file and write fresh data.

        # If the mode is "a":
        # → It will add new data without removing the existing data.


        fieldnames = ["username", "password", "age"]  
        # Defining the column names (headers) of the CSV file.
        # Headers should be provided as a list.

        writer = csv.DictWriter(csvFile, fieldnames=fieldnames)  
        # Creating a writer object to write dictionary data into the CSV file.
        
        writer.writeheader()       # Writing the header row (column names) into the CSV file.

        
        # Writing data rows : Values must be provided in dictionary format where keys match the header names.
        writer.writerow({"username": "nice123@gmail.com", 
                         "password": "new@123", 
                         "age": "25"
                         })
        
        # This inserts one row of user data into the CSV file.
    



    


