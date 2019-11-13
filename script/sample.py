
#!/usr/local/bin/python3
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import datetime
import threading
import random

NODE_NUM = 4

def execSearch(browser: webdriver):
    """
    Googleで検索を実行する
    :param browser: webdriver
    """
    # スクリーンショットのファイル名用に日付を取得
    dt = datetime.datetime.today()
    dtstr = dt.strftime("%Y%m%d%H%M%S")

    # Googleにアクセス
    browser.get('https://www.google.co.jp/')
    sleep(1)

   # キーワードの入力
    search_box = browser.find_element_by_name("q")
    search_box.send_keys('docker selenium')

    # 検索実行
    search_box.submit()
    sleep(1)

    # スクリーンショット
    browser.save_screenshot('images/' + dtstr + '_' + str(random.randrange(10000)) + '.png')

def start_webdriver():
    try:
        browser = webdriver.Remote(
            command_executor='http://selenium-hub:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        # Googleで検索実行
        execSearch(browser)
    finally:
        browser.close()
        browser.quit()

if __name__ == '__main__':
    for i in range(NODE_NUM):
        thread = threading.Thread(target=start_webdriver)
        thread.start()