from openpyxl import load_workbook
from utils.handlingExcel import read_excel_by_rows, read_excel_by_cols, addData_excel, append_to_excel



def test_printExcelbyRows():
    filePath="testData\\searchProduct.xlsx"
    sheetName="PhoneConfigs"
    excelData = read_excel_by_rows(filePath, sheetName)
    print("data from excel in PhoneConfigs tab by rows is ", excelData)

def test_printExcelbyCols():
    filePath="testData\\searchProduct.xlsx"
    sheetName="PhoneConfigs"
    excelData = read_excel_by_cols(filePath, sheetName)
    print("data from excel in PhoneConfigs tab by cols is ", excelData)


def test_updateExcelValues():
    workbook = load_workbook("testData\\searchProduct.xlsx")
    sheet = workbook["MixerDetails"]
    print("from mixerdetails tab, the cell value is ", sheet.cell(row=3, column=1).value)
    #updating the cell value in excel
    sheet.cell(row=3, column=1,value = "NewDrinkMixerModelX")
    workbook.save("testData\\searchProduct.xlsx")
    print("updated value is ", sheet.cell(row=3, column=1).value)

def test_appendDataToExcel():
    filePath="testData\\searchProduct.xlsx"
    sheetName="MixerDetails"
    headers = ["Model", "Power", "Voltage"]
    rows = [
        ("MixerModelY", "500W", "220V"),
        ("MixerMoabccccccdelY", "100500W", "22440V")
        ]
    append_to_excel(filePath, sheetName, headers, rows)
    print("data appended to excel successfully")