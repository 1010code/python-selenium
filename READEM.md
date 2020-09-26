# Python Selenium 自動化爬取大量圖片

![](./screenshot/demo.gif)

透過 Python 自動化工具 Selenium 來完成爬蟲。

此範例爬取衛星雲圖資料，透過爬蟲模擬下載圖片。
- https://meteologix.com/tw/satellite/taiwan/satellite-water-vapor-10min/20200926-0740z.html

## 安裝Selenium
```
pip install selenium
```

## 下載 Webdriver 驅動
Selenium 透過網頁瀏覽器來模擬畫面，因此需要下載瀏覽器的驅動才能模擬。Webdriver 包括 Chrome、Safari、Firefox 等瀏覽器可以使用。下面範例以 Chrome 做示範。

首先我們先查看目前電腦裡的 chrome 瀏覽器是什麼版本，需要下載對應版本的 webdriver。ChromeDriver 可以來[這裏](https://chromedriver.chromium.org/downloads)下載。

![](./screenshot/img01.png)

## 設定欲爬取的年月日陣列
請在程式中將以下陣列進行初始化，假設要查詢2020年1~8月的每天。

```py
# 年份
yearList=[2020]
# 月份
monthList=[1,2,3,4,5,6,7,8]
# 每月有幾天
dayList=[31,28,31,30,31,30,31,31] 
```

## 設定下載類別

```py
# 三種不同衛星圖
# satellite-hd-10min、top-alert-10min、satellite-water-vapor-10min
mode= 'satellite-hd-10min'
```

## Running the Project
After completing the installation step and config setting, you're ready to start the project.

```bash
python helper.py
```