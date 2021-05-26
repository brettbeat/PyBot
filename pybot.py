from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

browser = webdriver.Safari()
browser.get('https://passportappointment.travel.state.gov/')

first_button = browser.find_element(By.ID, 'rb-home-list-new')
first_button.click()

next_button = browser.find_element(By.ID, 'btnHomeNext')
next_button.click()

WebDriverWait(browser, timeout=1000).until(lambda b: b.find_element(By.ID, 'InternationalTravel-yes'))
travel_plans = browser.find_element(By.ID, 'InternationalTravel-yes')
travel_plans.click()

calendar = browser.find_element(By.ID, 'DateTravel').send_keys('06/12/2021')

visa_button = browser.find_element(By.ID, 'VisaNeeded-no')
visa_button.click()

passport_button = browser.find_element_by_xpath('/html/body/div[3]/div[2]/section/form/div/div[2]/div/div[8]/div/button[1]')
passport_button.click()

captcha_button = browser.find_element_by_class_name('recaptcha-checkbox-checkmark')
captcha_button.click()

