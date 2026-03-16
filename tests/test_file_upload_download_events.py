from playwright.sync_api import Page, expect
import os

# File Upload Example
def test_file_upload(page:Page):
    page.goto("https://the-internet.herokuapp.com/upload")     # Navigate to the file upload demo page
    # page.hover("text=File Uploader")

    # Upload a file by setting the file input directly
    # Note: We cannot open the OS file explorer in automated tests, so we provide the file path from code
    page.set_input_files("#file-upload", "testData/credentials.csv") 
    # this step will open the file explorer window and 
    # we can pass the file to be selected as a parameter
    # we are using file from testdata folder becasue it cannot open the explorer window to select file
    # hence the files should be provided from the code itself

    page.click("#file-submit")      # Click the 'Upload' button to submit the file
    print("file uploaded successfully")     # Confirm in the console that the file upload step executed



# File Download Example
def test_file_download(page: Page):
    page.goto("https://the-internet.herokuapp.com/download")
    with page.expect_download() as download_info:  # Use 'expect_download' to wait for the download event triggered by clicking a file link
        page.click("text=some-file.txt")   # Click the file link to start download
    download = download_info.value      # Retrieve the download object
    print(download)   # Shows metadata about the downloaded file
    file_path = "Downloads_in_your_Playwright_project/" + download.suggested_filename   # Save the downloaded file to a local path inside the project folder
    download.save_as(file_path)
    assert os.path.exists(file_path)   # Verify that the file exists at the expected location
    print("file downloaded successfully at path: " + file_path)  # Confirm in the console that the download completed successfully


