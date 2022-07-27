from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scroll(height, duration = 1):
    h = height
    for timer in range(0,duration):
        driver.execute_script("window.scrollTo(0, "+str(h)+")")
        h += height  
        time.sleep(1)

# set driver
PATH = "./drivers/chromedriver.exe"
driver = webdriver.Chrome(PATH)

# open webpage
driver.get("https://click2donatemm.com")
driver.maximize_window()
print(driver.title)

try: 
    # wait for main page to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )

    articles = driver.find_elements(By.CLASS_NAME, "post-title")
    for article in articles:

        # read url from href
        link = article.find_element(By.TAG_NAME, "a").get_attribute("href")
        driver.get(link)
        
        # scrolling slowly
        scroll(500, 15)

        driver.back()
        time.sleep(3)

finally:
    driver.quit()

