from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 创建 Safari WebDriver 实例
driver = webdriver.Safari()

# 打开百度网站
driver.get("http://www.baidu.com")

# 找到搜索框元素并输入内容
search_box = driver.find_element(By.NAME, "wd")  # 百度搜索框的 name 属性通常是"wd"
search_query = "Python programming"  # 要填充的搜索内容
search_box.send_keys(search_query)

# 模拟键盘按下Enter键以执行搜索
search_box.send_keys(Keys.RETURN)

# 等待一段时间，方便查看搜索结果
# import time
#time.sleep(5)x

 
