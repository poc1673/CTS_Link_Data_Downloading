# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 04:58:48 2019

@author: USER
"""

#%%
from bs4 import BeautifulSoup

import requests
#    https://www.ctslink.com/a/shelflist.html?shelfType=MBS/serieslist.html?shelfId=MSRRT
url = 'https://www.ctslink.com/a/shelflist.html?shelfType=MBS'
values = {'username': 'POCaya',
          'password': 'Paradox13'}


def log_in_and_start_WF():
    url = 'https://www.ctslink.com/a/shelflist.html?shelfType=MBS'
    values = {'username': 'POCaya',
          'password': 'Paradox13'}
    r = requests.post(url, data=values)
    soup = BeautifulSoup(r.content, 'html.parser') 
    return(soup)

def get_html(url):
    values = {'username': 'POCaya',
          'password': 'Paradox13'}
    data=values
    r = requests.post(url,data=values)
    soup = BeautifulSoup(r.content, 'html.parser') 
    return(soup)

r = requests.post(url, data=values)
soup = BeautifulSoup(r.content, 'html.parser') 
print(soup.prettify())

def get_link(x):
    values = {'username': 'POCaya',
          'password': 'Paradox13'}
    data=values
    html_data = requests.post(x, data=values)
    html_data_formatted = BeautifulSoup(html_data.content, 'html.parser') 
    return(html_data_formatted)


def generate_series_links(soup_output):
    get_series_reports = soup_output.find_all('a', href=True)
    a = [str(x) for x in get_series_reports]
    b = [x.find("series")>0 for x in a]
    links = []
    for i in range(0,len(a)):
        if b[i]==True:
            links.append(a[i])
    return(links)


def get_series_id(x):
    s1 = re.sub('^.*>/a','/a',x)
    s2 = re.sub('\">.*$','',s1)    
    series_ID = re.sub("^&amp;seriesID","series",s2)
    series_ID = re.sub("&amp;.*$","",series_ID)
    return(series_ID)


def check_restricted(driver):
    page = driver.page_source
    check_page = page.find("Restricted Reports")
    return(check_page > 0)

#<input type="hidden" name="form.validation.token" value="67e4e0d6212a13d298a1691ac5b9893f95ba3e26dfac15596f6e535e2c7c734c9918fd093edfc811b37cbd7305850f86af58422eaa2a6523972aaae9a2e4f32a"/>
#page = requests.get("https://en.wikipedia.org/wiki/House_of_Schaumburg")
#page
#%%
import re
get_series_reports = soup.find_all(  "td")


#for i in range(0,len(a)):
 #   if b[i]==True:
  #      links.append(a[i])


def generate_raw_links(soup_output):
    get_series_reports = soup_output.find_all(  "td")
    a = [str(x) for x in get_series_reports]
    b = [x.find("series")>0 for x in a]
    links = []
    for i in range(0,len(a)):
        if b[i]==True:
            links.append(a[i])
    return(links)




def string_function(x):
    s1= re.sub('\\">Series Reports.*',"",x)
    s2= re.sub('\n',"",s1)
    s3= re.sub('<td>',"",s2)
    s4= re.sub('</a>',"",s3)
    s5= re.sub('<a',"",s4)
    s6= re.sub('</td>',"",s5)
    s7= re.sub(' href=\\"',"",s6)
    return(s7)

def second_string_function(x):
    s1 = re.sub('^.*>/a','/a',x)
    s2 = re.sub('\">.*$','',s1)    
    return(s2)


   
# WF_link_generator
# Function to generate the main table of different data sources from CTS link's
# website.

def WF_link_generator(soup_object,main_web_link = "https://www.ctslink.com"):
    link_list = generate_raw_links(soup)
    formatted_links = [string_function(x) for x in link_list]
    final_links = [main_web_link+x for x in formatted_links]
    return(final_links)


def includes_import(x):
    parsed_html = get_html(x)
    string_x = str(parsed_html)
    if string_x.find("IMPORTDATA")>0:
        return(True)
    else:
        return(False)



def series_link_formatter(link_list):
    s1 = [string_function(x) for x in link_list]
    s2 = [second_string_function(x) for x in s1]
    s3= [ re.sub("^.*;","",x  ) for x in s2 ] 
    return(s3)


#%%
# First two steps:
#   [1] Generate the table of different data providers for the website.
#   [2] Format the links for access.    
import numpy as np
soup = log_in_and_start_WF()
table_list = WF_link_generator(soup)
table_list = np.array(WF_link_generator(soup))
table_list_import_BOOL = np.array([includes_import(x) for x in table_list])
one_series = table_list[table_list_import_BOOL]
not_one_series = table_list[np.array(np.invert(table_list_import_BOOL))]

series_links = []


for i in not_one_series:
    print(i)
    issuer_html = get_html(i)
    link_list_ = generate_series_links(issuer_html)
    full_link = [i +"&"+x for x in series_link_formatter(link_list_ )]    
    final_series_list = [re.sub("serieslist","seriesdocs",x) for x in full_link  ]    
    series_links.extend(final_series_list)
#%%

table_list = np.array(WF_link_generator(soup))
table_list_import_BOOL = np.array([includes_import(x) for x in table_list])
one_series = table_list[table_list_import_BOOL] 
not_one_series = table_list[np.array(np.invert(table_list_import_BOOL))]
series_links = []

not_one_series = list(not_one_series)
for i in not_one_series:
    print( str(not_one_series.index(i)) + " of "+str(len(not_one_series))+".")
    issuer_html = get_html(i)
    link_list_ = generate_series_links(issuer_html)
    full_link = [i +"&"+x for x in series_link_formatter(link_list_ )]    
    final_series_list = [re.sub("serieslist","seriesdocs",x) for x in full_link  ]    
    series_links.extend(final_series_list)


#series_links = np.array(series_links)
#series_links_importable_BOOL = np.array([includes_import(x) for x in series_links])
#series_links  = series_links[series_links_importable_BOOL ]
#series_links.tofile("series_links2.csv",sep = ",")
#series_links
all_series = list(one_series)
all_series.extend(series_links)

#%%
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def login_with_selenium():
    driver = webdriver.Chrome(  executable_path = "C:/Users/USER/Documents/chromedriver.exe")
    driver.get("https://www.ctslink.com")
    username_pw = driver.find_element_by_id("user_id")
    username_pw.send_keys("POCaya")
    login_pw = driver.find_element_by_id("password")
    login_pw.send_keys("Paradox13")
    button = driver.find_element_by_id("loginButton")
    button.click()
    return(driver)    
    
    
a = login_with_selenium()
time.sleep(3)
missing_links = []


a.get(all_series[1])

#%%
a = login_with_selenium()
time.sleep(3)
missing_links = []



all_series= list(all_series)

def check_restricted(driver):
    page = driver.page_source
    check_page = page.find("Restricted Reports")
    return(check_page > 0)

for i in all_series[6453:len(all_series)]:
    print( str(all_series.index(i)) + " of "+str(len(all_series))+".")
    try:
        a.get(i)
        a.get(a.current_url+"&tab=IMPORTDATA")
        if includes_import(a.current_url)==True:
            if check_restricted(a)== False:
                hold = a.find_element_by_id("documentChkBx")
                hold.click()
                hold = a.find_element_by_id("zip")
                hold.click()
    except Exception:
        a.close()
        missing_links.append(i)
        a = login_with_selenium()
        time.sleep(5)


#%%
