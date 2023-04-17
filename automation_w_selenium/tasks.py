from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base.models import InstagramModel
from celery import shared_task
from automation_w_selenium.celery import app
from automation_w_selenium import celery
import re
@shared_task
def login_to_instagram(username, password):
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/accounts/login/')
    username_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(('name', 'username')))
    username_input.send_keys(username)
    password_input = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(('name', 'password'))
    )
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 3).until(
        EC.url_changes('https://www.instagram.com/accounts/login/')
    )
  
    return driver


def find_counts(username):
  driver = webdriver.Chrome()
  profile_url = 'https://www.instagram.com/' + username + '/'
  driver.get(profile_url)
  ul= WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, 'ul'))
    )
  items=ul.find_elements(By.TAG_NAME, 'li')
  instagram_model = InstagramModel()
  
  for index, li in enumerate(items, 1):
    count_text = li.text.lower() 
    count = 0  
    if "k" in count_text:
        count = int(re.findall(r'(\d+)k', count_text)[0]) * 1000
    elif "m" in count_text:
        count = int(re.findall(r'(\d+)m', count_text)[0]) * 1000000
    else:
        count = int(re.sub(r'[^\d,]', '', count_text).replace(',', ''))
    if index == 2:
        instagram_model.follower = count 
    elif index == 3:
        instagram_model.following = count  
      
  instagram_model.username=username
  instagram_model.save() 
  print(instagram_model.following)
  return driver