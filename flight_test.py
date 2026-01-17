from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Open Google Flights
driver.get("https://www.google.com/travel/flights")

wait = WebDriverWait(driver, 20)

# Click "From" field
from_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']")))
from_box.click()
time.sleep(1)
from_box.send_keys("Delhi")
time.sleep(2)
from_box.send_keys(Keys.ENTER)

# Click "To" field
to_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']")))
to_box.click()
time.sleep(1)
to_box.send_keys("Mumbai")
time.sleep(2)
to_box.send_keys(Keys.ENTER)

print("✅ From: Delhi | To: Mumbai selected successfully")

time.sleep(20)
driver.quit()

