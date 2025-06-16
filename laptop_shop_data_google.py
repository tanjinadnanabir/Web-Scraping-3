# //*[@id="input"]

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# driver = webdriver.Chrome()
chrome_options = Options()

chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
driver = webdriver.Chrome(options=chrome_options)

# driver.get('https://www.google.com')

# driver.maximize_window()
# time.sleep(10)
# google_input = driver.find_element(By.NAME,'q')
# google_input.send_keys("Laptop Shop Near Mirpur")
# google_input.send_keys(Keys.RETURN)

# time.sleep(10)

driver.get('https://www.google.com/maps/search/laptop+shop+near+mirpur/@23.8139169,90.343716,5684m/data=!3m2!1e3!4b1?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D')
height = driver.execute_script('return document.body.scrollHeight')

# recaptcha_checkbox = driver.find_element(By.CLASS_NAME, "g-recaptcha")
# from selenium.webdriver.common.action_chains import ActionChains

# action = ActionChains(driver)
# action.move_to_element(recaptcha_checkbox).click().perform()

time.sleep(10)