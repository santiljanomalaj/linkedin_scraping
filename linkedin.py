from selenium import webdriver
from lxml import html
from bs4 import BeautifulSoup as soup
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import requests
import time
import random
import re
import csv 
import urllib.request
import pymysql

# last_name = input("Enter last_name : ")

# define csv file
titles=['Profile Url', 'Name', 'Country', 'Experience', 'Language']
with open('linkedin_profile.csv', mode='a', encoding="utf8", newline='') as student_file:
    student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    student_writer.writerow(titles)

#Connection to MYSQL DB
# conn=pymysql.connect(host="localhost",user="root",password="",db="linkedin")
# c=conn.cursor()

# run chrome driver 
driver = webdriver.Chrome("chromedriver.exe")

driver.get("https://www.linkedin.com/uas/login?session_redirect=https%3A%2F%2Fwww%2Elinkedin%2Ecom%2Fsearch%2Fresults%2Fpeople%2F%3FfacetGeoRegion%3D%255B%2522dk%253A0%2522%255D%26keywords%3Dsap%2520and%2520bw%2520and%2520abap%26origin%3DFACETED_SEARCH&fromSignIn=true&trk=cold_join_sign_in")

# driver.delete_all_cookies()
time.sleep(3)
try:
  driver.find_element_by_xpath('/html/body/div/div/form[2]/section/p/a').click()
except NoSuchElementException:
  pass

access_mail="darkbomb1234@outlook.com"
password="125kgs&&%JHJ"

time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys(access_mail)
time.sleep(2)
driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
time.sleep(random.randint(2,5))

driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()

# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="username"]').send_keys(access_mail)
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
# time.sleep(random.randint(2,5))

# driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()


driver.execute_script("window.scrollTo(0, 200);")
time.sleep(2)
driver.execute_script("window.scrollTo(200, 400);")
time.sleep(2)
driver.execute_script("window.scrollTo(400, 600);")
time.sleep(2)
driver.execute_script("window.scrollTo(600, 800);")
time.sleep(2)
driver.execute_script("window.scrollTo(800, 1000);")
time.sleep(2)
driver.execute_script("window.scrollTo(1000, 1200);")
time.sleep(5)
profile_content_lists = soup(driver.page_source, 'html.parser')
profile_lists = profile_content_lists.findAll('li', {'class':'search-result search-result__occluded-item ember-view'})

for profile_list in profile_lists:
  profile_info = ['','','','','']

  profile_info[0] = "https://www.linkedin.com/" + profile_list.a['href']
  driver.get(profile_info[0])
  driver.execute_script("window.scrollTo(0, 500);")
  time.sleep(2)
  driver.execute_script("window.scrollTo(500, 1000);")
  time.sleep(2)
  driver.execute_script("window.scrollTo(1000, 1500);")
  time.sleep(2)
  driver.execute_script("window.scrollTo(1500, 2000);")
  time.sleep(2)
  driver.execute_script("window.scrollTo(2000, 2500);")
  time.sleep(2)


  profile_content = soup(driver.page_source, 'html.parser')
  # time.sleep(5)
  # if(profile_content.find('h2',{'class':'card-heading t-20 t-black t-normal fl'}) != None):
  #   time.sleep(5)
  #   language_button = driver.find_elements_by_xpath("//button[contains(@class, 'pv-accomplishments-block__expand artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--tertiary ember-view')]")
  #   print(language_button)
  #   time.sleep(5)
  #   for i in range(len(language_button)):
  #     language_button[i].click()
  #     time.sleep(5)
  #     if(driver.find_element_by_xpath('//*[@id="languages-expandable-content"]') != None):
  #       language_lists = driver.find_element_by_xpath('//*[@id="languages-expandable-content"]').text
  #       print(language_lists)
        # for language_list in language_lists:
        #   if (language_list.text.count('Natvie') > 0 or language_list.text.count('professional') > 0):
        #     language += language_list.text + "\n"
        #     print(language)

  time.sleep(5)

  profile_info[1] = re.sub('\s\s+', ' ', profile_content.find('li',{'class':'inline t-24 t-black t-normal break-words'}).text)

  profile_info[2] = re.sub('\s\s+', ' ',  profile_content.find('li', {'class':'t-16 t-black t-normal inline-block'}).text)
  if(profile_content.find(id = "experience-section") !=None):
    experience_section = profile_content.find(id = "experience-section").findAll('li')
    profile_info[3] = re.sub('\s\s+', ' ', experience_section[0].text)

  with open('linkedin_profile.csv', mode='a', encoding="utf8", newline='') as student_file:
    student_writer = csv.writer(student_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    student_writer.writerow(profile_info)