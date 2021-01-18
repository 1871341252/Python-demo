import selenium
from selenium import webdriver
from seleniumtools import find_element
import time

driver=driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://test.geron-e.com:8096/")
driver.add_cookie({"name":"sessionId","value":"8a9a13e715fa43c3b3abdc2a284d8ddb"})
driver.refresh()
# driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[1]/a/div/div/div/h3').click()
# wins = driver.window_handles
# driver.switch_to.window(wins[-1])
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/ul/li[3]').click()
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/textarea').click
# time.sleep(2)
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/textarea').send_keys("测试内容")
# driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[2]/button').click()
# assert driver.title =="聚融e在线学习、培训、考试官网"
# print("测试通过！！！")
# time.sleep(5)
# driver.quit()
test_video=("xpath",'/html/body/div[6]/div/div/div[1]/div/div[1]/a/div/div/div/h3')
course_review=("xpath",'/html/body/div[3]/div[2]/div[1]/div[3]/ul/li[3]')
comments=("xpath",'/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/textarea')
write_comment=("xpath",'/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[1]/textarea')
publish_comment=("xpath",'/html/body/div[3]/div[2]/div[1]/div[3]/div/div[3]/form/div/div[2]/button')

find_element(driver,test_video).click()
wins = driver.window_handles
driver.switch_to.window(wins[-1])
find_element(driver,course_review).click()
find_element(driver,comments).click()
find_element(driver,write_comment).send_keys("测试内容")
find_element(driver,publish_comment).click()


assert driver.title =="聚融e在线学习、培训、考试官网"
print("测试通过！！！")

driver.quit()