"""
Chrome tarayıcısına işler yaptırmaya çalışıyorum. 19.01.2022 Yorgunum
"""
import time

import settings
from selenium import webdriver
surucu = webdriver.Chrome(settings.driver_path)
#bir adrese git
surucu.get("https://istanbulakademi.meb.gov.tr/")
print(surucu.current_url)
print(surucu.title)

time.sleep(2)
surucu.get("http://www.milliyet.com/")
print(surucu.current_url)
print(surucu.title)
time.sleep(2)
surucu.back()
print(surucu.current_url)
print(surucu.title)
time.sleep(2)
surucu.forward()
print(surucu.title)
print(surucu.current_url)
time.sleep(2)

surucu.close()


