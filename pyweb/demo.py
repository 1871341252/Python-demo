import selenium
from selenium import webdriver
import time
driver =selenium.webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://test.geron-e.com:8096/")
driver.add_cookie({"name":"sessionId","value":"133b63d0e20744c2bd81e1b2c7e120e5"})
driver.refresh()
driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[1]/a/div/div/div/h3').click()
wins = driver.window_handles
driver.switch_to.window(wins[-1])
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[2]/div[2]/a/i').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="layui-layer1"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
# driver.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
assert driver.title =="聚融e在线学习、培训、考试官网"
print("测试通过！！！")
time.sleep(2)
driver.quit()
