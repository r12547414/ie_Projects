#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by iFantastic on 2019/4/11

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
class main():
    dr = webdriver.Firefox()
    dr.maximize_window()
    sleep(5)
    url = "https://www.imooc.com/user/newlogin"

    dr.get(url)

    sleep(3)
    dr.find_element(By.XPATH('//*[@id="sigin"]/div[1]/h1/span[1]'))
    sleep(3)
    dr.find_element(By.NAME("email")).click()
    sleep(3)
    dr.find_element(By.NAME("email")).send_keys("fzdchina@126.com")
    dr.find_element(By.NAME("password")).send_keys("f12547414")
    dr.find_element(By.value("登录")).click()



if __name__ == '__main__':
    main()