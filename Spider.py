from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from lxml import etree
import platform



class RemoteChormeBrowser(webdriver.Remote):
    def __init__(self,):
        '''创建谷歌浏览器控制器'''
        remoteUrl = 'http://docker-selenium-1:4444/wd/hub' if "linux" in platform.platform().lower() else 'http://localhost:4444/wd/hub'
        options = Options()
        options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--start-maximized')
        options.add_argument('log-level=3')
        options.add_argument('--no-sandbox')
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
        options.add_argument('--disable-dev-shm-usage')
        super(Browser, self).__init__(command_executor=remoteUrl, options=options)
        self.maximize_window()

    def goto(self, url, timeout=20):
        '''
        访问网址
        :param url:网址
        :param timeout:超时
        '''
        self.set_page_load_timeout(timeout)  # 页面加载时间
        try:
            self.get(url)
        except:
            self.execute_script("window.stop()")

    def scroll(self, num=100000):
        '''
        向下滑动滚动条
        :param num:0为顶部 越大越往下
        '''
        js = "var q=document.documentElement.scrollTop=%d" % num
        self.execute_script(js)

    def clickNode(self, node):
        if type(node) is str:
            node = self.find_element(By.XPATH, node)
        self.execute_script('arguments[0].click();', node)

    @property
    def tree(self):
        html = self.page_source
        tree = etree.HTML(html)
        return tree

    def __del__(self):
        self.quit()


class LocalFirefoxBrowser(webdriver.Firefox):
    def __init__(self,driverPath,browserPath,GUI=True):
        '''
        创建本地火狐浏览器控制器
        :param driverPath:驱动路径
        :param browserPath:浏览器路径
        :param GUI:是否显示浏览器
        '''        
        options = Options()
        if not GUI:
            options.add_argument('--headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('--start-maximized')
        options.add_argument('log-level=3')
        options.add_argument('--no-sandbox')
        options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
        options.add_argument('--disable-dev-shm-usage')
        options.binary_location = browserPath
        service  = Service(executable_path=driverPath)
        super(LocalFirefoxBrowser, self).__init__(
            service=service,
            options=options
        )
        self.maximize_window()

    def goto(self, url, timeout=20):
        '''
        访问网址
        :param url:网址
        :param timeout:超时
        '''
        self.set_page_load_timeout(timeout)  # 页面加载时间
        try:
            self.get(url)
        except:
            self.execute_script("window.stop()")

    def scroll(self, num=100000):
        '''
        向下滑动滚动条
        :param num:0为顶部 越大越往下
        '''
        js = "var q=document.documentElement.scrollTop=%d" % num
        self.execute_script(js)

    def clickNode(self, node):
        if type(node) is str:
            node = self.find_element(By.XPATH, node)
        self.execute_script('arguments[0].click();', node)

    @property
    def tree(self):
        html = self.page_source
        tree = etree.HTML(html)
        return tree

