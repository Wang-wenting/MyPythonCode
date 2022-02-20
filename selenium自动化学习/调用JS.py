#coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
#给用户名的输入框标红
js = "var q=document.getElementById(\"su\");q.style.border=\"1px solid red\";"
#调用js
driver.execute_script(js)
time.sleep(3)

# driver.find_element_by_id("user_name").send_keys("username")
# driver.find_element_by_id("user_pwd").send_keys("password")
# driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)

driver.quit()