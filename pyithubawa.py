from pydoc import cli
from xml.dom import NotFoundErr
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

def click_wall_post():
    
    posts = driver.find_element(By.CLASS_NAME, "fairy-content-area")
    articles = posts.find_elements(By.TAG_NAME, "article")
    
    urls = []
    for article in articles:
        # wait for link to appear
        url = WebDriverWait(article, 30).until(
            EC.presence_of_element_located((By.TAG_NAME, "a"))
        )
        urls.append(url.get_attribute("href"))

    for url in urls:
        print(url)
        driver.get(url)
        
        # scrolling slowly
        scroll(500, 15)


# open webpage
driver.get("https://pyithubawa.com")
driver.maximize_window()
print(driver.title)

# consent privacy data
try:
    button = driver.find_element(By.LINK_TEXT, "Agree & Close")
    button.click()
except:
    NotFoundErr

# get total pages
navigation = driver.find_element(By.CLASS_NAME, "nav-links")
pages = navigation.find_elements(By.TAG_NAME, "a")
total_pages = 0
for p in pages:
    if p.text != "Next":
        total_pages = p.text
    
total_pages = int(total_pages)

print(f"Total Pages: {total_pages}")

try:
    for page in range(1, total_pages+1):
        site = ("https://pyithubawa.com" if page == 1 else f"https://pyithubawa.com/page/{page}")
    
        # open webpage
        driver.get(site)
        
        # wait for main page to appear
        title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "site-title"))
        )

        # in case another privacy consent appear
        try:
            pc = driver.find_element(By.CLASS_NAME, "qc-cmp2-summary-buttons")
            btn = pc.find_element(By.LINK_TEXT, "AGREE")
            btn.click()
        except:
            NotFoundErr

        click_wall_post()

finally:
    driver.quit()