from selenium import webdriver
from fixture.james import JamesHelper
from fixture.mail import MailHelper
from fixture.session_helper import SessionHelper
from fixture.project_helper import ProjectHelper
from fixture.signup import SignupHelper
from fixture.soap import SoapHelper


class App:
    def __init__(self, browser, config):
        self.base_url = config['web']['base_url']
        self.service = config['soap']['address']
        self.soap = SoapHelper(self)
        self.james = JamesHelper(self)
        self.project = ProjectHelper(self, base_url=config['web']['base_url'])
        self.session = SessionHelper(self)
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.config = config
        self.browser = browser
        self.username = config['web_admin']['username']
        self.password = config['web_admin']['password']
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        self.wd.implicitly_wait(5)
        self.wd.get(self.base_url)

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
