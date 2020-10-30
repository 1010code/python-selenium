from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
from datetime import datetime

from selenium.webdriver.chrome.options import Options

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

url = 'http://ms7.fhsh.tp.edu.tw/%E6%95%99%E8%82%B2%E9%83%A8AI%E6%95%99%E6%9D%90%E5%9C%8B%E5%B0%8Fplan1.pdf'
browser.get(url)