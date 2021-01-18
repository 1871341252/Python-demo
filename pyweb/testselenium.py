from selenium import webdriver
import time
#driver = selenium.webdriver.Chrome(executable_path='chromedriver.exe')
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.baidu.com/")
#1.id定位
#e = driver.find_element_by_id("kw")
#e.send_keys("iphone12")
driver.find_element_by_id("kw").send_keys("iphone12")
#e1 = driver.find_element_by_id("su")
#e1.click()
driver.find_element_by_id("su").click()
time.sleep(5)

#2.xpath定位
#driver.find_element_by_xpath('//*[@id="kw"]').send_keys("iphone12")
#driver.find_element_by_xpath('//*[@id="su"]').click()

#3.name定位
#driver.find_element_by_name('wd').send_keys("iphone12")
#driver.find_element_by_xpath('//*[@id="su"]').click()

#4.classname定位
#driver.find_element_by_class_name('s_ipt').send_keys("iphone12")
#driver.find_element_by_xpath('//*[@id="su"]').click()

#5.css selector
#driver.find_element_by_css_selector('#kw').send_keys("iphone12")
#driver.find_element_by_xpath('//*[@id="su"]').click()

#6.link_text 只能用于超链接 a标签
#driver.find_element_by_link_text('新闻').click()

#7. partial_link_text 只能用于超链接 a标签
#driver.find_element_by_partial_link_text("hao").click()

#8. tag_name
#driver.find_elements_by_tag_name('div')

assert driver.title =="iphone12_百度搜索"
print("测试通过！！！")

driver.quit()
