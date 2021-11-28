import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import winreg
def desktop_path():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    desktop = winreg.QueryValueEx(key, "Desktop")[0]
    # print(desktop)
    return desktop
url = input('请输入网址:')
# url = 'https://h5.cyol.com/special/daxuexi/byw1m1kn1s/m.html'
driver = webdriver.Chrome()
driver.get(url)
# 窗口最大化
driver.maximize_window()
time.sleep(1)
# 进入iframe
driver.switch_to.frame(0)
# driver.find_element_by_css_selector('#province').click()
# 根据索引
# Select(driver.find_element_by_id('province')).select_by_index(11)
# 根据值
# Select(driver.find_element_by_id('province')).select_by_value('11')
time.sleep(1)
# 根据文本
Select(driver.find_element_by_css_selector('#province')).select_by_visible_text('浙江省')
# time.sleep(1)
Select(driver.find_element_by_css_selector('#city')).select_by_visible_text('绍兴市')
# time.sleep(1)
driver.find_element_by_xpath('/html/body/div[2]/div[3]').click()
# driver.find_element_by_css_selector('body > div.section00 > div.sure').click()
# 倍速
time.sleep(3)
driver.execute_script("document.querySelector('video').playbackRate = 15.0;")
driver.find_element_by_css_selector('body > div.section0.topindex > div.start_btn').click()

while True:
    try:
        # 是否出现题目
        driver.find_element_by_css_selector('body > div.section1.topindex1')
        time.sleep(0.1)
        # 选A
        driver.find_element_by_css_selector('body > div.section1.topindex1 > div.w1.option').click()
        time.sleep(0.1)
        # 确认按钮
        driver.find_element_by_css_selector('body > div.section1.topindex1 > div.button').click()
        time.sleep(2.5)

        driver.find_element_by_css_selector('body > div.section1.topindex1 > div.continue').click()
    except:
        pass
    try:
        driver.find_element_by_css_selector('body > div.section2.topindex1')
        time.sleep(0.1)
        driver.find_element_by_css_selector('body > div.section2.topindex1 > div.w1.option').click()
        time.sleep(0.1)
        driver.find_element_by_css_selector('body > div.section2.topindex1 > div.button').click()
        time.sleep(2.5)
        driver.find_element_by_css_selector('body > div.section2.topindex1 > div.continue').click()
    except:
        pass
    try:
        if driver.find_element_by_css_selector('body > div.section3.topindex1'):
            time.sleep(1)
            a = time.time()
            # driver.get_screenshot_as_file(r'C:\Users\knighthood\OneDrive\桌面\{}.png'.format(a))
            driver.get_screenshot_as_file(r'{}\{}.png'.format(desktop_path(), a))
            break
    except:
        pass
driver.close()
