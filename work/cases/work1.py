# 第一步：导入selenium
from selenium import webdriver
import time

# 第二步：打开谷歌浏览器
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

driver.get("http://www.geron-e.com/")

time.sleep(3)
driver.maximize_window()
driver.add_cookie({'name':'sessionId','value':'2ce8cbfed87a489db35f447d1a1b8ca2'})
#driver.quit()