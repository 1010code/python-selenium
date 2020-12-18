from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from datetime import datetime

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": './',
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "plugins.always_open_pdf_externally": True
    }
)


# 載入瀏覽器驅動，以 Chrome 為例。請下載與電腦所安裝的瀏覽器版本相同的對應驅動。
# Download source: https://chromedriver.chromium.org/downloads
browser = webdriver.Chrome('./chromedriver',options = chrome_options)
# set windows size
browser.set_window_size(1024, 768)

url = 'https://doc.twse.com.tw/server-java/t57sb01?step=1&colorchg=1&co_id=2330&year=108&mtype=F&'
browser.get(url)
# click menu by xpath
browser.find_element_by_xpath('/html/body/center/form/table[2]/tbody/tr[2]/td[8]/a').click() 
time.sleep(1)
windows=browser.window_handles  #獲得當前瀏覽器所有視窗
browser.switch_to.window(windows[-1])
browser.find_element_by_xpath('/html/body/center/a').click()
    


