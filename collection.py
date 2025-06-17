from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import csv

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/maps/search/laptop+shop+near+mirpur/@23.8139132,90.3332292,5684m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D")

time.sleep(5)

for _ in range(10):
    driver.execute_script("document.querySelector('div[role=\"main\"] div[aria-label]').scrollBy(0, 1500)")
    time.sleep(5)

listings = driver.find_elements(By.CSS_SELECTOR, '.Nv2PK')

print(f"Found {len(listings)} shop listings")

shop_data = []

for list in listings:
    try:
        shop_name = list.find_element(By.CSS_SELECTOR, '.qBF1Pd').text
    except:
        shop_name = None

    try:
        phone_number = list.find_element(By.CSS_SELECTOR, '.UsdlK').text
    except:
        phone_number = None

    shop_data.append({
        'Shop Name': shop_name,
        'Phone Number': phone_number,
    })

driver.quit()

with open("mirpur_laptop_shops.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Shop Name", "Phone Number"])
    writer.writeheader()
    writer.writerows(shop_data)

print("Data saved to 'mirpur_laptop_shops.csv'")
