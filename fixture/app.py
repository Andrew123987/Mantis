from selenium import webdriver
from fixture.session_helper import SessionHelper


class App:
    def __init__(self, browser, base_url):
        self.session = SessionHelper(self)
        self.base_url = base_url
        self.browser = browser
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        ##options = webdriver.FirefoxOptions()  ## Включение headless режима
        ##options.add_argument('--headless')  ## Включение headless режима
        ##self.wd = webdriver.Firefox(options=options) ## Включение headless режима
        ##self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/manage_proj_create_page.php/') and len(
                wd.find_elements_by_class_name('fdTableSortTrigger')) > 0):
            wd.get(self.base_url)

    def stop(self):
        self.wd.quit()