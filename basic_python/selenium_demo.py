# from selenium import webdriver

# # Set up Chrome WebDriver
# driver_path = 'basic_python/chromedriver_mac64/chromedriver'  # Replace with the actual path
# driver = webdriver.Chrome(executable_path=driver_path)

# # Open a website
# driver.get('https://www.example.com')

# # Find an element by its ID and print its text
# element = driver.find_element_by_id('some_id')
# print(element.text)

# # Close the browser
# driver.quit()

from seleniumwire import webdriver  # Import the webdriver from seleniumwire

# Set up the browser options
options = webdriver.ChromeOptions()

# Start the browser with the options
driver = webdriver.Chrome(options=options)

# Open a website
driver.get('https://www.example.com')

# Access the requests made by the browser
for request in driver.requests:
    if request.response:
        print(
            "URL:", request.url,
            "Status code:", request.response.status_code,
            "Content type:", request.response.headers['Content-Type']
        )

# Close the browser
driver.quit()

