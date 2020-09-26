from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time

# 自定義函式，小於10的數字補0 ex: 3 -> 03
"""
    args:
        num (int)
    returm:
        string format.
"""
def formatNumber(num):
    if num<10:
        return '0'+str(num)
    else:
        return str(num)

# 載入瀏覽器驅動，以 Chrome 為例。請下載與電腦所安裝的瀏覽器版本相同的對應驅動。
# Download source: https://chromedriver.chromium.org/downloads
browser = webdriver.Chrome('./chromedriver')

# 首次開啟網頁時需要點選 Accept 按鈕，因此透過 flag 變數來判斷是否首次執行。
flag=0

# 年份
yearList=[2020]
# 月份
monthList=[1,2,3,4,5,6,7,8]
# 每月有幾天
dayList=[31,28,31,30,31,30,31,31]
# 迴圈存入指定的日期格式 年月日-時 ex: 20200926-08  
queryList=[]
# satellite-hd-10min、top-alert-10min、satellite-water-vapor-10min
mode= 'satellite-hd-10min'

for i in yearList:
    for j in monthList:
        for k in range(1, dayList[j-1]+1):
            for hour in range(24):
                queryList.append(str(i)+formatNumber(j)+formatNumber(k)+'-'+formatNumber(hour))

# print(queryList)
print('爬取總天數: ',len(queryList))



for i in queryList:
    # 輸入欲爬取網頁
    url = 'https://meteologix.com/tw/satellite/taiwan/'+str(mode)+'/'+str(i)+'00z.html'
    browser.get(url)

    # 判斷是否首次執行(首次開啟網頁需要點選Anncept按鈕)
    if flag==0:
        time.sleep(1)
        browser.find_element_by_css_selector('.nx3Fpp8U.nx3gnDVX').click()
        flag=1
    time.sleep(0.5)
    # city name disable by class name
    browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/div/div/div[1]/div[1]/div[3]/div[1]/div[13]/div[9]/button[4]').click() 
    # click menu by xpath
    browser.find_element_by_css_selector('.btn-group').click() 
    time.sleep(0.5)
    # click download image by xpath
    browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/div/div/div[1]/div[1]/div[3]/div[1]/div[1]/div/div/ul/li[3]/span[2]').click() 
    print(str(i), ' done!')
