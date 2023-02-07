from selenium import webdriver
import pandas as pd
import time
import random

driver = webdriver.Chrome('/Users/bilene/Downloads/chromedriver_mac64/chromedriver')

driver.get('https://forums.edmunds.com/discussion/2864/general')

userid_element = driver.find_element('xpath','//*[@id="Comment_1726631"]/div/div[2]/div[1]/span[1]')
userid = userid_element.text

user_date = driver.find_element('xpath','//*[@id="Comment_1726631"]/div/div[2]/div[2]/span/a/time')
date = user_date.get_attribute('title')

user_comment = driver.find_element('xpath','//*[@id="Comment_1726631"]/div/div[3]/div')
comment = user_comment.text

ids = driver.find_elements('xpath','//*[contains(@id, "Comment_")]')
# ids[0].get_attribute('id')

comment_ids = []
for i in ids:
	comment_ids.append(i.get_attribute('id'))

comment_ids