from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time



browser = webdriver.Chrome('./chromedriver')

flag=0

for i in range(0,3):
    url = 'https://meteologix.com/tw/satellite/taiwan/stop-alert-10min/20200919-0'+str(i)+'00z.html'
    browser.get(url)

    # input("Press Enter after the game is started...")

    if flag==0:
        time.sleep(1)
        browser.find_element_by_css_selector('.nx3Fpp8U.nx3gnDVX').click()
        flag=1
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/div/div/div[1]/div[1]/div[3]/div[1]/div[13]/div[9]/button[4]').click() 
    browser.find_element_by_css_selector('.btn-group').click() 
    time.sleep(0.5)
    # ActionChains(browser).click('<li onclick="save_as();" title="Save as...">').perform()
    browser.find_element_by_xpath('/html/body/div[1]/div/div[6]/div/div[1]/div/div/div[1]/div[1]/div[3]/div[1]/div[1]/div/div/ul/li[3]/span[2]').click() 
    print('done!')
