import asyncio
import time
from walkoff_app_sdk.app_base import AppBase

class News(AppBase):
    __version__ = "1.0.0"
    app_name = "news"  # this needs to match "name" in api.yaml

    def __init__(self, redis, logger, console_logger=None):

        super().__init__(redis, logger, console_logger)

    async def sendNews(self, title, context):
        try:
            from selenium import webdriver
            from selenium.webdriver.common.keys import Keys
        except:
            mystr = "no selenium"
            return mystr
        option = webdriver.ChromeOptions()
        # option.add_argument('--user-data-dir=/Users/apple/Library/Application Support/Google/Chrome/Default')
        option.add_argument('--headless')
        option.add_argument('--no-sandbox')
        option.add_argument('--disable-gpu')
        option.add_argument('--disable-dev-shm-usage')
        browser = webdriver.Chrome(chrome_options=option)
        # browser=webdriver.Chrome()

        browser.get("http://10.245.142.98:84")
        browser.set_window_size(1920, 1080)
        browser.maximize_window()

        browser.find_element_by_xpath('/html/body/div/div/nav/a[2]').click()
        browser.find_element_by_xpath('/html/body/div/div/div/div[1]/input').send_keys(title)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div[2]').send_keys(context)
        browser.find_element_by_xpath('/html/body/div/div/div/button').click()

        return "news"


if __name__ == "__main__":
    asyncio.run(News.run(), debug=True)
