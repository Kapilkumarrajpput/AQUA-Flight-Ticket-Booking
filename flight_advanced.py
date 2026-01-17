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
wait = WebDriverWait(driver, 30)

# Open Google Flights
driver.get("https://www.google.com/travel/flights")

# FROM
from_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where from?']")))
from_box.click()
time.sleep(1)
from_box.send_keys("Delhi")
time.sleep(2)
from_box.send_keys(Keys.ENTER)

# TO
to_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='Where to?']")))
to_box.click()
time.sleep(1)
to_box.send_keys("pune")
time.sleep(2)
to_box.send_keys(Keys.ENTER)

print(" Route Selected: Delhi → pune")

# DATE CLICK
date_box = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Departure date']")))
date_box.click()
time.sleep(2)

# Select next available date
next_date = wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@role='gridcell'])[10]")))
next_date.click()

done_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[text()='Done']")))
done_btn.click()

print("✅ Date Selected")

# Wait for results
time.sleep(10)

# Get cheapest price
try:
    price = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[contains(text(),'₹')])[1]")))
    cheapest = price.text

    print("🔥 Cheapest Price:", cheapest)

    # Save to file
    with open("flight_price.txt", "w") as f:
        f.write(f"Delhi to pune Cheapest Flight: {cheapest}")

    print(" Price saved to flight_price.txt")

except:
    print("❌ Price could not be fetched")

time.sleep(15)
driver.quit()
