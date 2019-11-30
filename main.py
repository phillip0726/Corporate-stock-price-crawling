#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import urllib
import time
#import pandas as pd
#from pandas import DataFrame, Series
import re
from urllib.request import urlopen
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import csv
import openpyxl

driver = wd.Chrome('./chromedriver.exe')
driver.maximize_window()

url = 'https://finance.naver.com/item/sise_day.nhn?code=%%CODE%%&page=%%PAGE_NUM%%'
dayCssSelector = 'body > table.type2 > tbody > tr:nth-child(%%NUM%%) > td:nth-child(1) > span'
stockCssSelector = 'body > table.type2 > tbody > tr:nth-child(%%NUM%%) > td:nth-child(2) > span'

maxPage = 50
while True:
    print('회사 코드를 입력하세요 (종료 : 0) : ', end = '')
    code = input()
    if code == '0':
        break

    print('회사명을 입력하세요 : ', end = '')
    name = input()

    fileName = name + '(' + code + ').xlsx'

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = '주가'

    new_url = url.replace('%%CODE%%', code)


    for page in range(1, maxPage + 1):
        driver.get(new_url.replace('%%PAGE_NUM%%', str(page)))

        for num in range(3, 8):
            day = driver.find_element_by_css_selector(dayCssSelector.replace('%%NUM%%', str(num))).text
            stock = driver.find_element_by_css_selector(stockCssSelector.replace('%%NUM%%', str(num))).text
            sheet.append([day, stock])
        for num in range(11, 16):
            day = driver.find_element_by_css_selector(dayCssSelector.replace('%%NUM%%', str(num))).text
            stock = driver.find_element_by_css_selector(stockCssSelector.replace('%%NUM%%', str(num))).text
            sheet.append([day, stock])

    # sheet2.append([입력값1, 입력값2, 입력값3, 입력값 4])

    wb.save('./' + fileName)

driver.close()