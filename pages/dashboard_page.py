import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(BasePage):

    PAGE_URL = Links.HOST

    PROJECTS_BUTTON = ("xpath", "//a[@href='/projects']")

    @allure.step("Click on 'PROJECT' link")
    def click_projects_link(self):
        self.wait.until(EC.element_to_be_clickable(self.PROJECTS_BUTTON)).click()