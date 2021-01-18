from selenium import webdriver
from utils.seleniumtools import find_element
from utils.log import logging
import time

driver=driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://www.geron-e.com:8081/course/index.html")
driver.add_cookie({"name":"sessionId","value":"08a1ace966104355983e3a8305533702"})
driver.refresh()


time.sleep(3)
enter_plan=find_element("xpath",'//*[@id="course-list"]/div/div[1]/div/div[3]/a')
enter_question=find_element("xpath",'//*[@id="study"]/div[2]/div/div/div[3]/div[2]/a')
enter_plans=find_element("xpath",'//*[@id="continueExercise"]/p')
question1=find_element("xpath",'//*[@id="subject-1-12825"]/div[1]/div[3]/div/div/div')
submit_answers1=find_element("id","nextTestQuestions")
next_question=find_element("id","nextTestQuestions")

find_element(driver,enter_plan).click()
find_element(driver,enter_question).click()
find_element(driver,enter_plans).click()
find_element(driver,question1).click()
find_element(driver,submit_answers1).click()
find_element(driver,next_question).click()

