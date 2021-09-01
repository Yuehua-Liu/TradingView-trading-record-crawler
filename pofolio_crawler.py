# %%
import os
import sys
import time
from datetime import datetime

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# store personal account
account = ''
password = ''
with open("./personal_account.txt", "r") as f:
    account = f.readline().splitlines()[0]
    password = f.readline().splitlines()[0]

# target url
web_url = 'https://tw.tradingview.com'

PATH = r'.\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument('ignore-certificate-errors')
# options.add_argument('headless')  # 隱藏瀏覽器

try:
    driver = webdriver.Chrome(executable_path=PATH, options=options)
except:
    return_msg = 'Chrome driver version need to update. Please try again.'
    print("Sys Info: " + return_msg)

try:
    driver.get(web_url)
except:
    show_msg = 'Something wrong, program will catch the url again.'
    print("Sys Info: " + show_msg)

    try:
        driver.get(web_url)
    except:
        return_msg = 'Wrong URL, please check again.'
        print("Sys Info: " + return_msg)
        driver.close()

# 工具選單(menu)
driver.execute_script(
    "document.getElementsByClassName('tv-header__user-menu-button tv-header__user-menu-button--anonymous js-header-user-menu-button')[0].click();"
)
time.sleep(0.5)
# 登入(login button)
driver.execute_script(
    "document.getElementsByClassName('labelRow-2IihgTnv labelRow-89Fo62DY')[0].click();"
)
time.sleep(0.5)
# Email 登入 (email login)
driver.execute_script(
    "document.getElementsByClassName('tv-signin-dialog__social tv-signin-dialog__toggle-email js-show-email')[0].click();"
)
time.sleep(0.5)
# 輸入帳號 (account)
driver.execute_script(
    f"document.getElementsByClassName('tv-control-material-input tv-signin-dialog__input tv-control-material-input__control')[0].value='{account}';"
)
time.sleep(0.5)
# 輸入密碼 (password)
driver.execute_script(
    f"document.getElementsByClassName('tv-control-material-input tv-signin-dialog__input tv-control-material-input__control')[1].value='{password}';"
)
time.sleep(0.5)
# 登入按鈕 (login)
driver.execute_script(
    "document.getElementsByClassName('tv-button__loader')[0].click();"
)
time.sleep(3)
# 圖表 (chart page)
driver.execute_script(
    "document.querySelectorAll('[data-type]')[0].click();"
)
time.sleep(4)
# connect Paper trading account
driver.execute_script(
    "document.getElementsByClassName('button-1iktpaT1 size-l-2NEs9_xt intent-primary-1-IOYcbg appearance-default-dMjF_2Hu full-width-1wU8ljjC button-1fGT2JpL')[0].click();"
)
time.sleep(3)
# 帳戶歷史 (account history)
driver.execute_script(
    "document.getElementsByClassName('tv-tabs__tab js-tab')[3].click();"
)
time.sleep(4)
# 刷新帳戶歷史資料 (Scroll account history page)
# can modify the num of loop yourself, it depends on how many data you want.
for i in range(0, 10):
    driver.execute_script(
        "document.getElementsByClassName('ka-table-wrapper tableWrapper-VzPHU7U0')[3].scrollTop+=5000;"
    )
    time.sleep(1.5)

# %%
# 抓帳戶歷史表格資料 (crawl account hisory table data)
el = driver.find_element_by_xpath(
    "//table[@class='ka-table table-VzPHU7U0 balances']")

# 輸出帳戶歷史資料 (parse table data)(can filter specific date here)
df = pd.read_html(el.get_attribute('outerHTML'))
df = df[0]
# print(df[df['時間'] > '2021-08-31'])

# 匯出 CSV 檔案 (export to csv)
df.to_csv(f'./portfolio_record_archieve/portfolio_record_{datetime.today().date()}.csv', index=False)

# 匯出 XLSX 檔案 (export to xlsx)
# df.to_excel(f'./portfolio_record_archieve/portfolio_record_{datetime.today().date()}.xlsx', index=False)


