# lambda is generally used for small functions and is not suitable for large code files.
# However, for demonstration, we will create a simple lambda function that adds two numbers.
# we use it mostly when there is a single return statement.

# def add(a,b):
#     return a + b
# this is a generic way of defining a function

#here we are using lambda to define the same function in a single line
from conftest import page


add = lambda a,b: a + b

print(add(5,3))  # Output: 8

# In this example, we define a lambda function that takes two arguments a and b, and returns their sum.
# The lambda function is then called with the arguments 5 and 3, and it returns 8.

#another example

# loc =page.locator("//span[contains (text(),'value1')]")
# loc2 =page.locator("//span[contains (text(),'value2')]")
# loc3 =page.locator("//span[contains (text(),'none')]")

# by using lambda we can create small functions for repetitive tasks
# loc = lambda variable_for_value:page.locator(f"//span[contains (text(),'variable_for_value')]")


# def validateLocatorVisibility(variable_for_value):
#     expect(loc("variable_for_value")).to_be_visible()
