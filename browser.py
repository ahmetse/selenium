"""
Chrome tarayıcısına işler yaptırmaya çalışıyorum. 19.01.2022 Yorgunum
"""
import settings
from selenium import webdriver
surucu = webdriver.Chrome(executable_path=settings.driver_path)
#bir adrese git
surucu.get("https://istanbulakademi.meb.gov.tr/")
surucu.close()


