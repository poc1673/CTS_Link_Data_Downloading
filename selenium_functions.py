# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 08:36:02 2019

@author: USER
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(  executable_path = "C:/Users/USER/Documents/chromedriver.exe")
driver.get("https://www.ctslink.com")
#%%
username_pw = driver.find_element_by_id("user_id")
username_pw.send_keys("POCaya")

login_pw = driver.find_element_by_id("password")
login_pw.send_keys("Etcetera13")

button = driver.find_element_by_id("loginButton")
button.click()

#%%


def login_with_selenium():
    driver = webdriver.Chrome(  executable_path = "C:/Users/USER/Documents/chromedriver.exe")
    driver.get("https://www.ctslink.com")
    username_pw = driver.find_element_by_id("user_id")
    username_pw.send_keys("POCaya")
    login_pw = driver.find_element_by_id("password")
    login_pw.send_keys("Etcetera13")
    button = driver.find_element_by_id("loginButton")
    button.click()
    return(driver)
    
a = login_with_selenium()
#%%
a.get("https://www.ctslink.com/a/seriesdocs.html?shelfId=ACE&seriesId=2007ASAP1&tab=IMPORTDATA")
#%%
hold = a.page_source
#%%
html_data_formatted = BeautifulSoup(hold , 'html.parser')
href_data = np.array([str(x) for x in html_data_formatted.find_all("a",href = True) ] )
key_BOOL = np.array([True if (x.find("key")>0)&(x.find("CSV")>0) else False for x in href_data] )
href_selected = href_data[key_BOOL]


def get_csv(x):
    s1 = re.sub('^.*="/a/','/a/',href_selected[0])
    s2 = re.sub('">\n<.*>\n<.*','',s1  )
    return(s2)

get_csv(href_selected[0])


#%%

a.find_element_by_tag_name("a")
#%%


