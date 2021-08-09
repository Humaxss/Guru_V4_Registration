from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pandas as pd
import lxml

driver=webdriver.Chrome('C:\Python\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)

#User_id
User_id = driver.find_element_by_name("uid")
User_id.click()
User_id.send_keys("mngr346602")
time.sleep(1)

#password
password = driver.find_element_by_name("password")
password.click()
password.send_keys("YgupEze")
time.sleep(1)

#login
login = driver.find_element_by_name("btnLogin")
login.click()
time.sleep(1)

#new_customer
new_customer = driver.find_element_by_xpath("//li[a='New Customer']")
new_customer.click()
time.sleep(1)

#customer_name
customer_name = driver.find_element_by_xpath("//input[@name='name']")
customer_name.click()
customer_name.send_keys("Erik")

#gender
gender = driver.find_element_by_xpath("//input[@value='m']")
gender.click()
time.sleep(3)

#date_of_birth / pozn. Nejde rozkliknúť štvrček, nemá id/class
date_of_birth = driver.find_element_by_xpath("//input[@id='dob']")
date_of_birth.send_keys("24_10_1996")

#adress
adress = driver.find_element_by_xpath("//textarea[@name='addr']")
adress.send_keys("Mala Calomija")

#city
city = driver.find_element_by_xpath("//input[@name='city']")
city.send_keys("Mala Calomija")

#state
state = driver.find_element_by_xpath("//input[@name='state']")
state.send_keys("Slovakia")

#pin
pin = driver.find_element_by_xpath("//input[@name='pinno']")
pin.send_keys("9988998899")

#mobile_number
mobil_number = driver.find_element_by_xpath("//input[@name='telephoneno']")
mobil_number.send_keys("989875568742")

#e_mail
e_mail = driver.find_element_by_xpath("//input[@name='emailid']")
e_mail.send_keys("masiar.etraeuýfaed@gmail.com")

#password
password = driver.find_element_by_xpath("//input[@name='password']")
password.send_keys("ArOw24nb")

#submit
submit = driver.find_element_by_xpath("//input[@name='sub']")
submit.click()
time.sleep(4)

#continue_1
continue_1 = driver.find_element_by_xpath("//a[text()='Continue']")
continue_1.click()
time.sleep(3)

driver.close()

#------------------------f
