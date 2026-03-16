from playwright.sync_api import sync_playwright 
from utils.readingJson import readJsonData

def test_getApi(playwright: sync_playwright):
    # browser = playwright.chromium.launch()
    # context = browser.new_context()
    # page = context.new_page()

    # we need above 3 lines to open a browser
    # for api, we just need context (context is similar to incognito mode)

    context = playwright.request.new_context()
    # now we can use context to all api methods

    # Send GET request to fetch products
    response = context.get("https://dummyjson.com/products")
    print(response)
    # Print basic response details
    print("response headers",response.headers)
    print("response status is", response.status)
    print("response body in json format", response.json())
    print("response body in bytecode format", response.body())


    # Extract JSON response
    resp_json = response.json()
    print("printing only products from response")
    print(resp_json['products'])
    print("printing only title of products")

    # Print only product titles
    for product in resp_json['products']:
        print(product['title'])

def test_selectiveGetValues(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get("https://dummyjson.com/products/1")
    print("response body in json format", response.json())
    resp_json = response.json()
    print("title is", resp_json['title'])
    print("price is", resp_json['price'])
    print("description is", resp_json['description'])
    assert response.status == 200
    assert resp_json['title'] == "Essence Mascara Lash Princess"

def test_get_with_params(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get("https://gorest.co.in/public/v2/users", params={"id":8333154})
    print("test_get_with_params is", response.json())

def test_postApi(playwright: sync_playwright):
    context = playwright.request.new_context()
    payload = {
                "title": "Gaming Chair",
                "price": 330.98,
                "brand": "test brand"
    }
    response = context.post("https://dummyjson.com/products/add", data=payload, headers={"Content-Type":"application/json", "Authorization": "Bearer 123456789"})
    print("response body in json format", response.json())
    resp_json = response.json()
    print("new data is", resp_json)
    print("title is", resp_json['title'])
    assert response.status == 201
    assert resp_json['title'] == "Gaming Chair"


def test_postApi_usingJsonFileData(playwright: sync_playwright):
    context = playwright.request.new_context()
    payload = readJsonData("testData\Data_for_api.json")
    #in the above line we are using the fucntion to read data from our json file
    response = context.post("https://dummyjson.com/products/add", data=payload, headers={"Content-Type":"application/json", "Authorization": "Bearer 123456789"})
    print("response body in json format", response.json())
    resp_json = response.json()
    print("new data is", resp_json)
    print("title is", resp_json['title'])
    assert response.status == 201
    assert resp_json['title'] == "Gaming Chair from json file"

def test_putApi(playwright: sync_playwright):
    context = playwright.request.new_context()
    payload = {
                "title": "Office Chair",
                "price": 250.00,
                "brand": "updated brand"
    }
    response = context.put("https://dummyjson.com/products/1", data=payload, headers={"Content-Type":"application/json", "Authorization": "Bearer 123456789"})
    print("response body in json format", response.json())
    resp_json = response.json()
    print("updated data is", resp_json)
    print("title is", resp_json['title'])
    assert response.status == 200
    assert resp_json['title'] == "Office Chair"

def test_patchApi(playwright: sync_playwright):
    context = playwright.request.new_context()
    payload = {
                "price": 199.99
    }
    response = context.patch("https://dummyjson.com/products/1", data=payload, headers={"Content-Type":"application/json", "Authorization": "Bearer 123456789"})
    print("response body in json format", response.json())
    resp_json = response.json()
    print("patched data is", resp_json)
    print("price is", resp_json['price'])
    assert response.status == 200
    assert resp_json['price'] == 199.99





