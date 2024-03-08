import uuid


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def move_to_projects_list(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Manage').click()
        wd.find_element_by_link_text('Manage Projects').click()

    def project_add(self, a):
        wd = self.app.wd
        wd.find_element_by_xpath('//table[3]/tbody/tr/td/form/input[2]').click()
        wd.find_element_by_name('name').click()
        wd.find_element_by_name('name').send_keys(a)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//tr[3]/td/a').click()
        wd.find_element_by_xpath('//input[3]').click()
        wd.find_element_by_xpath('//input[4]').click()
