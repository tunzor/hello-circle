from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(options=options)

if "HOST_URL" in os.environ:
    host_url = os.environ['HOST_URL']
else:
    host_url = "http://localhost:5000"

hello_text = "Hello CircleCI!"

print("Using URL:",host_url)
driver.get(host_url)
button = driver.find_element_by_id("clickbutton")
textarea = driver.find_element_by_id("put-text-in-here").text
# Test if text area is empty
print("\n<< TEST: Assert text not in text area >>")
assert not hello_text in textarea
print("PASS: No text found, continuing test...")

button.click()
textarea = driver.find_element_by_id("put-text-in-here").text
print("\n<< TEST: Assert text in text area >>")
# Test if text area contains the text
assert hello_text in textarea
print("PASS: Text found, continuing test...")

driver.close()
print("Test complete")