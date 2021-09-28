
import time
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URLS_PATH = "./data/urls_transferwise.csv"
CHROMEDRIVER_PATH = "./drivers/chromedriver"

# connect to chrome webdriver
options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(CHROMEDRIVER_PATH, options=options)

# read list of URLs to scrape
urls = pd.read_csv(URLS_PATH)

# init df to capture results
df = pd.DataFrame(columns = ['url', 'loaded_url', "source", "target", "method", 'fixed', "varaible", "match"])

for url in urls.url[:10]:
    # navigate to ...
    driver.get(url)
    time.sleep(1.5)
    
    loaded_url = driver.current_url
    try:
        source = loaded_url.split('=')[1].split('&')[0]
        target = loaded_url.split('=')[2].split('&')[0]
        method = loaded_url.split('=')[3].split('&')[0]
    except:
        source = "Fail"
        target = "Fail"
        method = "Fail"
    
    fixed = driver.find_elements_by_class_name('fee-digits')[0].text.split(" ")[0]
    variable = driver.find_elements_by_class_name('fee-digits')[2].text.replace("(","").replace(")","")

    df = df.append(
        pd.Series([url, loaded_url, source, target, method, fixed, variable, "test"], index = df.columns), 
        ignore_index=True
    )

df.to_csv('./data/scraped_transferwise.csv', index=False)