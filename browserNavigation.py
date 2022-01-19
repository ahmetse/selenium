"""
Gezinme işlemleri
"""
import settings
from selenium import webdriver
surucu = webdriver.Chrome(settings.driver_path)
print(surucu.current_url)