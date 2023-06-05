from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proxy_rotation import ProxyRotation
import random

# Configure the proxy rotation
proxy_rotation = ProxyRotation(proxy_list=['proxy1:port1', 'proxy2:port2', 'proxy3:port3'])
proxy_rotation.set_current_proxy()  # Set the initial proxy

# Configure the WebDriver with proxy settings
chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={proxy_rotation.current_proxy()}')
driver = webdriver.Chrome(options=chrome_options)  # You may need to install the appropriate WebDriver for your browser (e.g., ChromeDriver)

# Load the website URL
driver.get('https://example.com')  # Replace with the URL of the website you want to interact with

# Define the number of random button clicks
num_clicks = 10

# Loop to perform random button clicks
for i in range(num_clicks):
    # Find all clickable elements on the page
    clickable_elements = driver.find_elements(By.XPATH, "//button | //a")

    # Choose a random element to click
    random_element = random.choice(clickable_elements)
    random_element.click()

    # Wait for the page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//body")))

    # Change the proxy
    proxy_rotation.rotate_proxy()
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy_rotation.current_proxy()}')
    driver.quit()  # Close the current browser instance
    driver = webdriver.Chrome(options=chrome_options)  # Open a new browser instance with the updated proxy

# Close the browser
driver.quit()
