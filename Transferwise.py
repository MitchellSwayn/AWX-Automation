import pandas as pd
import numpy as np
import time

from selenium import webdriver
PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)

urls = pd.read_csv("urls_transferwise.csv")

for i in url[270:]:
    driver.get(i)
    time.sleep(1.5)
    url = i
    
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
    to_append = pd.Series([url, loaded_url, source, target, method, fixed, variable, "test"], index = data.columns)
    data = data.append(to_append, ignore_index=True)

    data.to_csv('./data.csv', index=False)