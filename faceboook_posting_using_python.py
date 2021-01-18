# Auto Posting on Facebook
 
 
from selenium import webdriver
import time

email = 'Put your email here'

pwd = 'put your password here'

msg = 'Post Here' 
#Example First Automated post using python
 
driver = webdriver.Chrome('chromedriver.exe')
 
driver.get('https://www.facebook.com/')
 
user =  driver.find_element_by_id('email')
user.send_keys(email)
 
 
password = driver.find_element_by_id('pass')
password.send_keys(pwd)
 
 
button = driver.find_element_by_id('u_0_b')
button.submit()
 
time.sleep(10)
 
 
body =  driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
body.click()
 
time.sleep(3)
 
message = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[2]/div[1]/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div/div')
message.send_keys(msg)
 
time.sleep(5)
 
post = driver.find_element_by_xpath('html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div/div[1]')
post.click()
 
#driver.close()