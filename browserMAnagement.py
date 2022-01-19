import time

import settings
from selenium import webdriver
surucu = webdriver.Chrome(settings.driver_path)
surucu.get("https://istanbulakademi.meb.gov.tr/")
time.sleep(2)
size=surucu.get_window_size()
w=size.get('width')
h=size.get('hight')
print("Tarayıcı genişşiği {} px, yüksekliği {} px'dir.".format(w,h))
surucu.set_window_size(500, 200)
print(size)
time.sleep(2)
position=surucu.get_window_position()
x=position.get('x')
y=position.get('y')
print("Tarayıcı sol uzaklığı {} px, üst  {} px'dir.".format(x,y))
surucu.set_window_position(400,400)
time.sleep(2)
surucu.maximize_window()
surucu.save_screenshot("./images/ekrangoruntusu.png")
time.sleep(2)

surucu.close()