import time  # 导入强制等待模块
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 导入显示等待模块
from selenium.webdriver.support import expected_conditions as EC  # 导入显示等待条件
from selenium.webdriver.support.ui import Select  # 导入下拉框操作模块
from selenium.webdriver import ActionChains  # 导入action模块


class Selenium():
    def setUp(self):  # 测试固件，前置条件,打开浏览器
        # 关闭chrome正受到自动测试软件的控制
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # 调用浏览器
        self.driver = webdriver.Chrome(options=chrome_options)
        # 打开链接
        self.driver.get('https://www.baidu.com/')
        self.driver.implicitly_wait(10)  # 全局隐式等待10秒

    # 下拉框操作：此方法针对于下拉框为select的情况
    # select = driver.find_element(By.ID,'s-usersetting-top')#定为下拉框元素的位置
    # options_list = Select(select).options#获取下拉框元素内容
    # for list in options_list:#遍历下拉框元素内容
    #     print(list)#展示下拉框元素


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
