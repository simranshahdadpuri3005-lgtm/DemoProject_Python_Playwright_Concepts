from playwright.sync_api import Page, expect
import os

def test_file_upload(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")
    # page.hover("text=File Uploader")
    page.set_input_files("#file-upload", "testData/credentials.csv") 
    # this step will open the file explorer window and 
    # we can pass the file to be selected as a parameter
    # we are using file from testdata folder becasue it cannot open the explorer window to select file
    # hence the files should be provided from the code itself
    page.click("#file-submit")  # clicking on upload button
    print("file uploaded successfully")


def test_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:
        page.click("text=some-file.txt")
    download = download_info.value
    print(download)
    file_path = "Downloads_in_your_Playwright_project/" + download.suggested_filename
    download.save_as(file_path)
    assert os.path.exists(file_path)
    print("file downloaded successfully at path: " + file_path)


