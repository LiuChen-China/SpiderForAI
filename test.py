from Spider import LocalFirefoxBrowser
import time

driverPath = 'geckodriver.exe'
browserPath = 'D:/火狐浏览器/firefox.exe'
GUI = True

browser = LocalFirefoxBrowser(driverPath=driverPath,browserPath=browserPath,GUI=GUI)
browser.goto('https://www.baidu.com')
time.sleep(10)
