import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('chromedriver')
driver.get('https://www.google.com/search?q=%EA%B3%A0%EC%96%91%EC%9D%B4&tbm=isch&tbs=il:ol&hl=ko&sa=X&ved=0CAAQ1vwEahcKEwiQsrKb76T7AhUAAAAAHQAAAAAQAw&biw=966&bih=850')

firstImage = driver.find_element(By.CSS_SELECTOR,'.rg_i.Q4LuWd')
firstImage.click()

time.sleep(0.2)
image = driver.find_element(By.CSS_SELECTOR,'.rg_i.Q4LuWd')
imageSrc = image.get_attribute('src')
urllib.request.urlretrieve(imageSrc, 'cat_image.jpg')

nextButton = driver.find_element(By.CSS_SELECTOR, '.t0PEec')
nextButton.click()

time.sleep(5)
driver.quit()