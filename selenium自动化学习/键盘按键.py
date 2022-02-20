#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  #需要引入keys包
import os,time

# driver = webdriver.Chrome()
# driver.get("https://mail.qq.com/")
#
# time.sleep(3)
# driver.maximize_window() # 浏览器全屏显示driver.find_element_by_id("user_name").clear()
# driver.switch_to.frame("login_frame")
# driver.find_element_by_name("u").send_keys("1157290948@qq.com")#tab的定位相相于清除了密码框的默认提示信息，等同上面的clear()
# driver.find_element_by_id("u").send_keys(Keys.TAB)
# time.sleep(3)
# driver.find_element_by_id("p").send_keys("Ting.1106")#通过定位密码框，enter（回车）来代替登陆按钮driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)'''#也可定位登陆按钮，通过enter（回车）代替click()
# driver.find_element_by_id("p").send_keys(Keys.ENTER)
#
#
# time.sleep(3)
# driver.quit()
# =======================******************************+++++++++++++++++++++++++


driver = webdriver.Chrome()

driver.get("http://www.baidu.com")#输入框输入内容
driver.find_element_by_id("kw").send_keys("selenium")
time.sleep(3)#ctrl+a 全选输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
time.sleep(3)#ctrl+x 剪切输入框内容
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
time.sleep(3)#输入框重新输入内容，搜索
driver.find_element_by_id("kw").send_keys(u"虫师 cnblogs")
driver.find_element_by_id("su").click()

time.sleep(3)
driver.quit()